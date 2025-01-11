import requests
import subprocess
import json
import time
import os
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem
from bs4 import BeautifulSoup
from colorama import *
from pystyle import * 

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
    except KeyboardInterrupt:
        Write.Print("Au revoir 🖐️", Colors.red_to_white)
    except requests.exceptions.RequestException as e:
        print(f"🔍 | OpenSpy | [LOG🔴] Erreur lors de la récupération des informations : {e}")

        input("🔍 | OpenSpy | [LOG🟢] Appuyez sur Entrée pour revenir au menu...")


def recherche_allintext(query):
    query = query.replace(" ", "+")
    url = f"https://www.google.com/search?q=allintext:{query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except KeyboardInterrupt:
        Write.Print("Au revoir 🖐️", Colors.red_to_white)
    except requests.exceptions.RequestException as e:
        print(f"❌ | Erreur lors de la requête HTTP : {e}")
        return None

def analyser_resultats(page_html):
    try:
        if not page_html:
            print("⚠️ | Aucun contenu HTML à analyser.")
            return []
        soup = BeautifulSoup(page_html, "html.parser")
        results = []
        items = soup.find_all("div", class_="tF2Cxc")
        for item in items:
            link = item.find("a")
            title = link.text if link else "Titre non trouvé"
            url = link.get("href") if link else "URL non trouvée"
            snippet = item.find("span", class_="aCOpRe")
            snippet_text = snippet.text if snippet else "Extrait non trouvé"
            results.append({
                "title": title.strip(),
                "url": url.strip(),
                "snippet": snippet_text.strip()
            })
        return results
    except KeyboardInterrupt:
        Write.Print("Au revoir 🖐️", Colors.red_to_white)

def effectuer_recherche(query):
    try:
        page_html = recherche_allintext(query)
        results = analyser_resultats(page_html)
        if results:
            print("\n🔍 | Résultats de la recherche :")
            for idx, result in enumerate(results, start=1):
                print(f"#{idx}")
                print(f"   ➡️ Titre : {result['title']}")
                print(f"   ➡️ Lien : {result['url']}")
                print(f"   ➡️ Extrait : {result['snippet']}\n")
            choix = input("Voulez-vous enregistrer ces résultats dans un fichier ? (oui/non) : ").strip().lower()
            if choix == "oui":
                enregistrer_resultats(results)
        else:
            print("🔍 | Aucun résultat trouvé.")
            time.sleep(2)
    except KeyboardInterrupt:
        Write.Print("Au revoir 🖐️", Colors.red_to_white)

def enregistrer_resultats(results):
    try:
        if not os.path.exists("save"):
            os.makedirs("save")
        timestamp = int(time.time())
        file_path = f"save/results_{timestamp}.json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
        print(f"🔍 | Les résultats ont été enregistrés dans le fichier : {file_path}")
    except KeyboardInterrupt:
        Write.Print("Au revoir 🖐️", Colors.red_to_white)

def main():
    menu = ConsoleMenu("Menu principal 🔍 | OpenSpy ")
    item_ip = FunctionItem("Recherche IP", rechercher_ip)
    item_allintext = FunctionItem("Recherche allintext", lambda: effectuer_recherche(input("Entrez votre requête allintext: ")))
    menu.append_item(item_ip)
    menu.append_item(item_allintext)
    menu.show()
try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    Write.Print("Au revoir 🖐️", Colors.red_to_white)
