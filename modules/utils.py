# modules/utils.py
import os
import json
import re
from datetime import datetime

def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name)

def load_domains(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[!] Fichier {filepath} introuvable.")
        return []



def archive_email(domain, body):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_domain = sanitize_filename(domain)
    filename = f"archives/{timestamp}_{safe_domain}.txt"
    os.makedirs("archives", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(body)
    print(f"[+] Email archivé : archives/{filename}")



def load_config():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("[!] Fichier de configuration 'config.json' introuvable.")
        return {}

def save_draft(emails, draft_file):
    with open(draft_file, 'w', encoding='utf-8') as f:
        json.dump(emails, f, indent=4, ensure_ascii=False)

def load_draft(draft_file):
    try:
        with open(draft_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("[!] Aucun brouillon trouvé.")
        return []
    
def render_template(template_path, variables):
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    for key, value in variables.items():
        content = content.replace(f"{{{{{key}}}}}", value)
    return content