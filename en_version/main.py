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
from googleapiclient.discovery import build

API_KEY = ""
CSE_ID = ""

try:
    os.system("cls || clear")
    print(Fore.GREEN, "[+] Please set the time for the results to be displayed --> ", Style.RESET_ALL, end='')
    clock_time = int(input())
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

def main():
    """
    Main menu of the application.
    """
    menu = ConsoleMenu("Main Menu 🔍 | OpenSpy ")
    item_ip = FunctionItem("IP Search", search_ip)
    item_phone = FunctionItem("Phone Number Search", phone_number)
    item_dns = FunctionItem("DNS Lookup", dns_lookup)
    item_allintext = FunctionItem("Allintext Search", lambda: perform_search(input("Enter your allintext query: ")))
    item_whois = FunctionItem("WHOIS Search", search_whois)
    menu.append_item(item_ip)
    menu.append_item(item_phone)
    menu.append_item(item_allintext)
    menu.append_item(item_dns)
    menu.append_item(item_whois)
    menu.show()

def search_ip():
    ip = input("Enter the IP address to search: ")
    print(f"Searching for information on IP address {ip}...\n")

    url = f"http://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        data = response.json()

        print(f"🔍 | OpenSpy | IP Address: {data.get('ip')}")
        print(f"🔍 | OpenSpy | City: {data.get('city')}")
        print(f"🔍 | OpenSpy | Region: {data.get('region')}")
        print(f"🔍 | OpenSpy | Country: {data.get('country')}")
        print(f"🔍 | OpenSpy | Organization: {data.get('org')}")
        print(f"🔍 | OpenSpy | Location: {data.get('loc')}")
        print(f"🔍 | OpenSpy | Postal Code: {data.get('postal')}")
        print(f"🔍 | OpenSpy | Hostname: {data.get('hostname')}")
        print(f"⏰ | OpenSpy | The result will be deleted after the set time.")
        time.sleep(clock_time)
    except requests.exceptions.RequestException as e:
        print(f"🔍 | OpenSpy | [LOG🔴] Error retrieving information: {e}")
    
    input("🔍 | OpenSpy | [LOG🟢] Press Enter to return to the menu...")

def search_whois():
    domain = input("Enter the domain name to search: ")
    print(f"Searching for WHOIS information for domain {domain}...\n")

    try:
        w = whois.whois(domain)
        print(f"🔍 | OpenSpy | Domain: {w.domain_name}")
        print(f"🔍 | OpenSpy | Registrar: {w.registrar}")
        print(f"🔍 | OpenSpy | Creation Date: {w.creation_date}")
        print(f"🔍 | OpenSpy | Expiration Date: {w.expiration_date}")
        print(f"🔍 | OpenSpy | Name Servers: {w.name_servers}")
        print(f"⏰ | OpenSpy | The result will be deleted after the set time.")
        time.sleep(clock_time)
    except Exception as e:
        print(f"🔍 | OpenSpy | [LOG🔴] Error retrieving WHOIS information: {e}")
    
    input("🔍 | OpenSpy | [LOG🟢] Press Enter to return to the menu...")

def phone_number():
    number = input("Enter the phone number to search: ")
    try:
        parsed_number = phonenumbers.parse(number)
        print(f"🔍 | OpenSpy | Country Code: {parsed_number.country_code}")
        print(f"🔍 | OpenSpy | National Number: {parsed_number.national_number}")
        print(f"🔍 | OpenSpy | Number Type: {phonenumbers.number_type(parsed_number)}")
        print(f"🔍 | OpenSpy | Possible Number: {phonenumbers.is_possible_number(parsed_number)}")
        print(f"🔍 | OpenSpy | Valid: {phonenumbers.is_valid_number(parsed_number)}")
        print(f"⏰ | OpenSpy | The result will be deleted after the set time.")
        time.sleep(clock_time)
    except phonenumbers.NumberParseException as e:
        print(f"🔍 | OpenSpy | [LOG🔴] Error parsing the number: {e}")
        input("🔍 | OpenSpy | [LOG🟢] Press Enter to return to the menu...")

def dns_lookup():
    """
    Perform a DNS lookup for a given domain.
    """
    domain = input("Enter the domain to search: ")
    print(f"Performing DNS lookup for domain {domain}...\n")
    dns_lookup_url = f"https://dns.google/query?name={domain}&type=A"
    try:
        response = requests.get(dns_lookup_url)
        data = response.json()
        print(f"🔍 | OpenSpy | DNS lookup results for domain {domain}:")
        for record in data["Answer"]:
            print(f"🔍 | OpenSpy | Type: {record['type']}")
            print(f"🔍 | OpenSpy | Name: {record['name']}")
            print(f"🔍 | OpenSpy | TTL: {record['TTL']}")
            print(f"🔍 | OpenSpy | Data: {record['data']}\n")
        print(f"⏰ | OpenSpy | The result will be deleted after the set time.")
        time.sleep(clock_time)
    except requests.exceptions.RequestException as e:
        print(f"🔍 | OpenSpy | [LOG🔴] Error retrieving DNS information: {e}")
        input("🔍 | OpenSpy | [LOG🟢] Press Enter to return to the menu...")

def perform_search(query):
    """
    Perform a Google search with the allintext parameter using the Google Custom Search API.
    """
    try:
        service = build("customsearch", "v1", developerKey=API_KEY)
        res = service.cse().list(q=f"allintext:{query}", cx=CSE_ID).execute()

        if "items" in res:
            time.sleep(clock_time)
            return res["items"]
        else:
            print("🔍 | No results found.")
            time.sleep(clock_time)
            return []

    except Exception as e:
        print(f"❌ | An error occurred during the search: {e}")
        time.sleep(clock_time)
        return []

def analyze_results(results):
    """
    Analyze and reformat the results obtained from the Google Custom Search API.
    """
    formatted_results = []
    for result in results:
        title = result.get("title", "Title not found")
        url = result.get("link", "Link not found")
        snippet = result.get("snippet", "Snippet not found")
        formatted_results.append({
            "title": title.strip(),
            "url": url.strip(),
            "snippet": snippet.strip()
        })
        time.sleep(clock_time)
    return formatted_results

def perform_search(query):
    """
    Perform the Google search and display the results.
    """
    results = perform_search(query)
    formatted_results = analyze_results(results)
    if formatted_results:
        print("\n🔍 | Search results:")
        for idx, result in enumerate(formatted_results, start=1):
            print(f"#{idx}")
            print(f"   ➡️ Title: {result['title']}")
            print(f"   ➡️ Link: {result['url']}")
            print(f"   ➡️ Snippet: {result['snippet']}\n")
        choice = input("Do you want to save these results to a file? (yes/no): ").strip().lower()
        if choice == "yes":
            save_results(formatted_results)
            time.sleep(clock_time)
    else:
        print("🔍 | No results found.")

def save_results(results):
    """
    Save the results to a JSON file.
    """
    if not os.path.exists("save"):
        os.makedirs("save")
    timestamp = int(time.time())
    file_path = f"save/results_{timestamp}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    print(f"🔍 | Results have been saved to the file: {file_path}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        Write.Print("\nGoodbye 🖐️", Colors.red_to_white)
        sys.exit(1)