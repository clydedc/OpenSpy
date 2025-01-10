import requests
import subprocess
import json
import time
import os
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem
from bs4 import BeautifulSoup

def rechercher_ip():
    ip = input("Entrez l'adresse IP à rechercher : ")
    print(f"Recherche d'informations sur l'adresse IP {ip}...\n")

    url = f"http://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        data = response.json()

        print(f"🔍 | OpenSpy | Adresse IP: {data.get('ip')}")
        print(f"🔍 | OpenSpy | Ville: {data.get('city')}")
        print(f"🔍 | OpenSpy | Région: {data.get('region')}")
        print(f"🔍 | OpenSpy | Pays: {data.get('country')}")
        print(f"🔍 | OpenSpy | Organisation: {data.get('org')}")
        print(f"🔍 | OpenSpy | Localisation: {data.get('loc')}")
        print(f"🔍 | OpenSpy | Code postal: {data.get('postal')}")
        print(f"🔍 | OpenSpy | Hostname: {data.get('hostname')}")
    except requests.exceptions.RequestException as e:
        print(f"🔍 | OpenSpy [LOG🔴] Erreur lors de la récupération des informations : {e}")

    input("🔍 | OpenSpy [LOG🟢] Appuyez sur Entrée pour revenir au menu...")

if not os.path.exists("save"):
    os.makedirs("save")

def recherche_allintext(query):
    query = query.replace(" ", "+")
    url = f"https://www.google.com/search?q=allintext:{query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        print(f"🔍 | OpenSpy | Réponse reçue pour la recherche allintext : {url}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"🔍 | OpenSpy [LOG🔴] Erreur lors de la recherche : {e}")
        return None

def analyser_resultats(page_html):
    if not page_html:
        return []

    soup = BeautifulSoup(page_html, "html.parser")
    results = []

    for item in soup.find_all("div", class_="BVG0Nb"):
        link = item.find("a")
        if link:
            title = link.text
            url = link.get("href")
            snippet = item.find_next("div", class_="B5oP8c")
            snippet_text = snippet.text if snippet else "Aucun extrait"
            results.append({
                "title": title,
                "url": url,
                "snippet": snippet_text
            })

    if not results:
        print("🔍 | OpenSpy | Aucun résultat trouvé.")
    return results

def effectuer_recherche_et_enregistrer(query):
    page_html = recherche_allintext(query)
    results = analyser_resultats(page_html)

    if results:
        timestamp = int(time.time())
        file_path = f"save/results_{timestamp}.json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=4)

        print(f"🔍 | OpenSpy [LOG🟢] Les résultats ont été enregistrés dans {file_path}")
    else:
        print("🔍 | OpenSpy [LOG🔴] Aucun résultat à enregistrer.")

def main():
    menu = ConsoleMenu("Menu principal 🔍 | OpenSpy ")

    item_ip = FunctionItem("Recherche IP", rechercher_ip)

    item_allintext = FunctionItem("Recherche allintext", lambda: effectuer_recherche_et_enregistrer(input("Entrez votre requête allintext: ")))

    menu.append_item(item_ip)
    menu.append_item(item_allintext)

    menu.show()

if __name__ == "__main__":
    main()
