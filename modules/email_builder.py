# email_builder.py
import os
from modules.utils import render_template

def list_templates(template_dir="assets/email_templates"):
    templates = [f for f in os.listdir(template_dir) if f.endswith(".txt")]
    return templates

def choose_template(template_dir="assets/email_templates"):
    templates = list_templates(template_dir)
    print("\n[+] Templates disponibles :")
    for idx, name in enumerate(templates):
        print(f"  [{idx}] {name}")
    while True:
        choice = input("\nSélectionnez le numéro du template à utiliser : ")
        if choice.isdigit() and int(choice) in range(len(templates)):
            return os.path.join(template_dir, templates[int(choice)])
        else:
            print("[!] Choix invalide. Réessayez.")

def build_email(template_path, variables):
    return render_template(template_path, variables)

def generate_emails(contacts, config):
    template_path = choose_template()
    emails = []
    for contact in contacts:
        email = contact["email"]
        domain = contact["domain"]
        body = build_email(template_path, {
            "nom": config.get("nom", ""),
            "prenom": config.get("prenom", ""),
            "email": config.get("email", ""),
            "entreprise": domain
        })
        emails.append({
            "email": email,
            "domain": domain,
            "body": body
        })
    return emails
