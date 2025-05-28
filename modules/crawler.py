# modules/crawler.py
import requests
from bs4 import BeautifulSoup
import re
import concurrent.futures
from tqdm import tqdm

EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; PentesterBot/1.0)"}

POSSIBLE_PATHS = [
    "mentions-legales", "legal", "legal-notice", "impressum",
    "contact", "about", "a-propos", "privacy", "confidentialite"
]

def find_emails_in_url(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        if response.status_code == 200:
            return re.findall(EMAIL_REGEX, response.text)
    except requests.RequestException:
        pass
    return []

def crawl_single_domain(domain, depth):
    base_url = f"https://{domain.strip()}"
    urls_to_check = [base_url] + [f"{base_url}/{path}" for path in POSSIBLE_PATHS]

    checked = set()
    emails_found = set()
    current_level = 0

    while urls_to_check and current_level < depth:
        new_urls = []
        for url in urls_to_check:
            if url in checked:
                continue
            checked.add(url)
            emails_found.update(find_emails_in_url(url))
            try:
                response = requests.get(url, headers=HEADERS, timeout=5)
                soup = BeautifulSoup(response.text, 'html.parser')
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    if href.startswith("/"):
                        full_url = base_url + href
                    elif href.startswith("http") and domain in href:
                        full_url = href
                    else:
                        continue
                    if full_url not in checked:
                        new_urls.append(full_url)
            except requests.RequestException:
                continue
        urls_to_check = new_urls
        current_level += 1

    return domain, list(emails_found)

def crawl_domains(domains, depth=1, max_workers=10):
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(crawl_single_domain, domain, depth): domain for domain in domains}
        
        # Ajout de tqdm pour suivre la progression des résultats des futurs
        for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Crawl des domaines", unit="domaine"):
            domain = futures[future]
            try:
                domain, emails = future.result()
                results[domain] = emails
            except Exception as e:
                print(f"[!] Erreur lors du crawl de {domain} : {e}")
                results[domain] = []
    return results
