import requests
import json
import time
import os, sys
import phonenumbers
import whois
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem
from bs4 import BeautifulSoup
from colorama import *
from pystyle import *
from phonenumbers import *
from googleapiclient.discovery import build



API_KEY = ""
CSE_ID = ""

try:
    os.system("cls || clear")
    print(Fore.GREEN, "[+] Veuillez définir le temps des résultat qui seront affiché --> ", Style.RESET_ALL, end='')
    clock_time = int(input())
except Exception as e:
    print(f"Erreur : {e}")
    sys.exit(1)

    def main():
        """
        Menu principal de l'application.
        """
        menu = ConsoleMenu("Menu principal 🔍 | OpenSpy ")
        item_ip = FunctionItem("Recherche IP", rechercher_ip)
        item_phone = FunctionItem("Recherche numéro de téléphone", phone_number)
        item_dns = FunctionItem("Recherche DNS", dns_lookup)
        item_allintext = FunctionItem("Recherche allintext", lambda: effectuer_recherche(input("Entrez votre requête allintext: ")))
        item_whois = FunctionItem("Recherche WHOIS", rechercher_whois)
        menu.append_item(item_ip)
        menu.append_item(item_phone)
        menu.append_item(item_allintext)
        menu.append_item(item_dns)
        menu.append_item(item_whois)
        menu.show()


    def recherche_allintext(query):
        """
        Effectue une recherche Google avec le paramètre allintext en utilisant l'API Google Custom Search.
        """
        try:
            service = build("customsearch", "v1", developerKey=API_KEY)
            res = service.cse().list(q=f"allintext:{query}", cx=CSE_ID).execute()

            if "items" in res:
                time.sleep(clock_time)
                return res["items"]
            else:
                print("🔍 | Aucun résultat trouvé.")
                time.sleep(clock_time)
                return []

        except Exception as e:
            print(f"❌ | Une erreur s'est produite lors de la recherche : {e}")
            time.sleep(clock_time)
            return []

    def enregistrer_resultats(results):
        """
        Enregistre les résultats dans un fichier JSON.
        """
        if not os.path.exists("save"):
            os.makedirs("save")
        timestamp = int(time.time())
        file_path = f"save/results_{timestamp}.json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
        print(f"🔍 | Les résultats ont été enregistrés dans le fichier : {file_path}")

    def analyser_resultats(results):
        """
        Analyse et reformate les résultats obtenus depuis l'API Google Custom Search.
        """
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
            time.sleep(clock_time)
        return formatted_results

    def effectuer_recherche(query):
        """
        Effectue la recherche Google et affiche les résultats.
        """
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
                time.sleep(clock_time)
        else:
            print("🔍 | Aucun résultat trouvé.")

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
            print(f"⏰ | OpenSpy | Le résultat se supprimera au bout du temps déterminé choisi. ")
            time.sleep(clock_time)
        except requests.exceptions.RequestException as e:
            print(f"🔍 | OpenSpy | [LOG🔴] Erreur lors de la récupération des informations : {e}")
        
            input("🔍 | OpenSpy | [LOG🟢] Appuyez sur Entrée pour revenir au menu...")

    def rechercher_whois():
        whois = input("Entrez le nom de domaine à rechercher : ")
        print(f"Recherche d'informations WHOIS pour le domaine {whois}...\n")

        try:
            w = whois.whois(whois)
            print(f"🔍 | OpenSpy | Domaine: {w.domain_name}")
            print(f"🔍 | OpenSpy | Registre: {w.registre}")
            print(f"🔍 | OpenSpy | Date de création: {w.creation_date}")
            print(f"🔍 | OpenSpy | Date d'expiration: {w.expiration_date}")
            print(f"🔍 | OpenSpy | Serveurs de noms: {w.name_servers}")
            print(f"⏰ | OpenSpy | Le résultat se supprimera au bout du temps déterminé choisi. ")
            time.sleep(clock_time)
        except Exception as e:
            print(f"🔍 | OpenSpy | [LOG🔴] Erreur lors de la récupération des informations WHOIS : {e}")
        
            input("🔍 | OpenSpy | [LOG🟢] Appuyez sur Entrée pour revenir au menu...")


    def phone_number():
        number = input("Entrez le numéro de téléphone à rechercher : ")
        try:
            parsed_number = phonenumbers.parse(number)
            print(f"🔍 | OpenSpy | Indicatif pays : {parsed_number.country_code}")
            print(f"🔍 | OpenSpy | Numéro national : {parsed_number.national_number}")
            print(f"🔍 | OpenSpy | Type de numéro : {phonenumbers.number_type(parsed_number)}")
            print(f"🔍 | OpenSpy | Possibilité de numéro valide : {phonenumbers.is_possible_number(parsed_number)}")
            print(f"🔍 | OpenSpy | Valide : {phonenumbers.is_valid_number(parsed_number)}")
            print(f"⏰ | OpenSpy | Le résultat se supprimera au bout du temps déterminé choisi. ")
            time.sleep(clock_time)
        except phonenumbers.NumberParseException as e:
            print(f"🔍 | OpenSpy | [LOG🔴] Erreur lors de l'analyse du numéro : {e}")
            input("🔍 | OpenSpy | [LOG🟢] Appuyez sur Entrée pour revenir au menu...")


def dns_lookup():
    """
    Effectue une recherche DNS pour un domaine donné.
    """
    domain = input("Entrez le domaine à rechercher : ")
    print(f"Recherche DNS pour le domaine {domain}...\n")
    dns_lookup : f"https://dns.google/query?name={domain}&type=A"
    try:
        response = requests.get(dns_lookup)
        data = response.json()
        print(f"🔍 | OpenSpy | Résultats de la recherche DNS pour le domaine {domain} :")
        for record in data["Answer"]:
            print(f"🔍 | OpenSpy | Type : {record['type']}")
            print(f"🔍 | OpenSpy | Nom : {record['name']}")
            print(f"🔍 | OpenSpy | TTL : {record['TTL']}")
            print(f"🔍 | OpenSpy | Données : {record['data']}\n")
        print(f"⏰ | OpenSpy | Le résultat se supprimera au bout du temps déterminé choisi. ")
        time.sleep(clock_time)
    except requests.exceptions.RequestException as e:
        print(f"🔍 | OpenSpy | [LOG🔴] Erreur lors de la récupération des informations DNS : {e}")
        input("🔍 | OpenSpy | [LOG🟢] Appuyez sur Entrée pour revenir au menu...")


    def recherche_allintext(query):
        """
        Effectue une recherche Google avec le paramètre allintext en utilisant l'API Google Custom Search.
        """
        try:
            service = build("customsearch", "v1", developerKey=API_KEY)
            res = service.cse().list(q=f"allintext:{query}", cx=CSE_ID).execute()

            if "items" in res:
                time.sleep(clock_time)
                return res["items"]
            else:
                print("🔍 | Aucun résultat trouvé.")
                time.sleep(clock_time)
                return []

        except Exception as e:
            print(f"❌ | Une erreur s'est produite lors de la recherche : {e}")
            time.sleep(clock_time)
            return []

    def analyser_resultats(results):
        """
        Analyse et reformate les résultats obtenus depuis l'API Google Custom Search.
        """
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
            time.sleep(clock_time)
        return formatted_results

    def effectuer_recherche(query):
        """
        Effectue la recherche Google et affiche les résultats.
        """
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
                time.sleep(clock_time)
        else:
            print("🔍 | Aucun résultat trouvé.")

    def enregistrer_resultats(results):
        """
        Enregistre les résultats dans un fichier JSON.
        """
        if not os.path.exists("save"):
            os.makedirs("save")
        timestamp = int(time.time())
        file_path = f"save/results_{timestamp}.json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
        print(f"🔍 | Les résultats ont été enregistrés dans le fichier : {file_path}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        Write.Print("\nAu revoir 🖐️", Colors.red_to_white)
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        Write.Print("\nAu revoir 🖐️", Colors.red_to_white)
        sys.exit(1)
