import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

def save_results_to_file(email, social_media, breach_data, public_records, affiliated_domains):
    filename = f"{email.replace('@', '_').replace('.', '_')}_info.txt"
    with open(filename, "w") as file:
        file.write(f"Information gathered for email: {email}\n")
        file.write("\nSocial Media Profiles:\n")
        file.writelines(f"- {profile}\n" for profile in social_media)

        file.write("\nBreach Data:\n")
        file.writelines(f"- {breach}\n" for breach in breach_data)

        file.write("\nPublic Records:\n")
        file.writelines(f"- {record}\n" for record in public_records)

        file.write("\nAffiliated Domains:\n")
        file.writelines(f"- {domain}\n" for domain in affiliated_domains)

    print(f"\nResults saved to {filename}")

def find_social_media(email):
    print("\n[+] Searching for social media profiles...")
    search_query = f"{email} site:facebook.com OR site:twitter.com OR site:linkedin.com"
    url = f"https://www.google.com/search?q={search_query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = [a.get('href') for a in soup.find_all('a', href=True)]
        return results
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def find_breach_data(email):
    print("\n[+] Searching for breach data...")
    url = f"https://haveibeenpwned.com/unifiedsearch/{email}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        breaches = [breach['Title'] for breach in data.get('Breaches', [])]
        return breaches
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []
    except ValueError:
        print("No breach data found.")
        return []

def find_public_records(email):
    print("\n[+] Searching for public records...")
    search_query = f"{email} public records"
    url = f"https://www.google.com/search?q={search_query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = [a.get('href') for a in soup.find_all('a', href=True)]
        return results
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def find_affiliated_domains(email):
    print("\n[+] Searching for affiliated domains...")
    search_query = f"{email} domain"
    url = f"https://www.google.com/search?q={search_query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = [a.get('href') for a in soup.find_all('a', href=True)]
        return results
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def main(email):
    print(f"Gathering information for email: {email}\n")

    social_media_results = find_social_media(email)
    breach_data = find_breach_data(email)
    public_records = find_public_records(email)
    affiliated_domains = find_affiliated_domains(email)

    print("\nSocial Media Profiles:")
    for result in social_media_results:
        print(f"- {result}")

    print("\nBreach Data:")
    for breach in breach_data:
        print(f"- {breach}")

    print("\nPublic Records:")
    for record in public_records:
        print(f"- {record}")

    print("\nAffiliated Domains:")
    for domain in affiliated_domains:
        print(f"- {domain}")

    save_results_to_file(email, social_media_results, breach_data, public_records, affiliated_domains)

if __name__ == "__main__":
    email = input("Enter the email address: ")
    main(email)
