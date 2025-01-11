import requests
import json
import time
import os
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem
from bs4 import BeautifulSoup
from colorama import *
from pystyle import *
from googleapiclient.discovery import build


API_KEY = "AIzaSyCwy21rJUyetjzCE_SqSGpXTc0rre6LUKk"
CSE_ID = "1128edad0e91c4a6b"  


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
    """
    Effectue une recherche Google avec le paramètre allintext en utilisant l'API Google Custom Search.
    """
    try:

        service = build("customsearch", "v1", developerKey=API_KEY)

        res = service.cse().list(q=f"allintext:{query}", cx=CSE_ID).execute()

        if "items" in res:
            return res["items"]
        else:
            print("🔍 | Aucun résultat trouvé.")
            return []
    except KeyboardInterrupt:
        Write.Print("Au revoir 🖐️", Colors.red_to_white)
    except Exception as e:
        print(f"❌ | Une erreur s'est produite lors de la recherche : {e}")
        return []


def analyser_resultats(results):
    """
    Analyse et reformate les résultats obtenus depuis l'API Google Custom Search.
    """
    try:
        formatted_results = []
        for result in results:
            title = result.get("title", "Titre non trouvé")
            url = result.get("link", "Lien non trouvé")
            snippet = result.get("snippet", "Extrait non trouvé")
            formatted_results.append({
                "title": title.strip(),
                "url": url.strip(),
                "snippet": snippet.strip()
            })
        return formatted_results
    except KeyboardInterrupt:
        Write.Print("Au revoir 🖐️", Colors.red_to_white)


def effectuer_recherche(query):
    """
    Effectue la recherche Google et affiche les résultats.
    """
    try:
        results = recherche_allintext(query)
        formatted_results = analyser_resultats(results)
        if formatted_results:
            print("\n🔍 | Résultats de la recherche :")
            for idx, result in enumerate(formatted_results, start=1):
                print(f"#{idx}")
                print(f"   ➡️ Titre : {result['title']}")
                print(f"   ➡️ Lien : {result['url']}")
                print(f"   ➡️ Extrait : {result['snippet']}\n")
            choix = input("Voulez-vous enregistrer ces résultats dans un fichier ? (oui/non) : ").strip().lower()
            if choix == "oui":
                enregistrer_resultats(formatted_results)
        else:
            print("🔍 | Aucun résultat trouvé.")
            time.sleep(2)
    except KeyboardInterrupt:
        Write.Print("Au revoir 🖐️", Colors.red_to_white)


def enregistrer_resultats(results):
    """
    Enregistre les résultats dans un fichier JSON.
    """
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
    """
    Menu principal de l'application.
    """
    menu = ConsoleMenu("Menu principal 🔍 | OpenSpy ")
    item_ip = FunctionItem("Recherche IP", rechercher_ip)
    item_allintext = FunctionItem("Recherche allintext", lambda: effectuer_recherche(input("Entrez votre requête allintext: ")))
    menu.append_item(item_ip)
    menu.append_item(item_allintext)
    menu.show()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        Write.Print("Au revoir 🖐️", Colors.red_to_white)