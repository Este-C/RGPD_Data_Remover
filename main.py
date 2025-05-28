# main.py
import os
from modules.utils import load_domains, load_config, archive_email, save_draft, load_draft
from modules.crawler import crawl_domains
from modules.email_builder import generate_emails
from modules.sender import send_all_emails
from tqdm import tqdm
from colorama import init, Fore, Style

init(autoreset=True)

def main():
    print(Fore.CYAN + r"""
██████╗  ██████╗ ██████╗ ██████╗     ██████╗  █████╗ ████████╗ █████╗     ██████╗ ███████╗███╗   ███╗ ██████╗ ██╗   ██╗███████╗██████╗ 
██╔══██╗██╔════╝ ██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗    ██╔══██╗██╔════╝████╗ ████║██╔═══██╗██║   ██║██╔════╝██╔══██╗
██████╔╝██║  ███╗██████╔╝██║  ██║    ██║  ██║███████║   ██║   ███████║    ██████╔╝█████╗  ██╔████╔██║██║   ██║██║   ██║█████╗  ██████╔╝
██╔══██╗██║   ██║██╔═══╝ ██║  ██║    ██║  ██║██╔══██║   ██║   ██╔══██║    ██╔══██╗██╔══╝  ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
██║  ██║╚██████╔╝██║     ██████╔╝    ██████╔╝██║  ██║   ██║   ██║  ██║    ██║  ██║███████╗██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═════╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
        by 6sco
    """ + Style.RESET_ALL)

    config = load_config()
    auto_select = config.get("auto_select_first_email", False)
    threads = config.get("threads", 10)

    if os.path.exists("drafts/emails_draft.json"):
        print(Fore.YELLOW + "[!] Un brouillon précédent a été trouvé.")
        print("Souhaitez-vous le charger ? (o/N) : ", end="")
        if input().strip().lower() == 'o':
            emails = load_draft("drafts/emails_draft.json")
            print(Fore.GREEN + f"[✓] {len(emails)} email(s) chargé(s) depuis le brouillon.")
        else:
            emails = None
    else:
        emails = None

    if emails is None:
        domains = load_domains("domains.txt")

        print(Fore.YELLOW + "[+] Veuillez choisir le niveau de profondeur du crawl (1-3) :")
        while True:
            try:
                depth = int(input("> "))
                if 1 <= depth <= 3:
                    break
                else:
                    print("[!] Veuillez entrer un nombre entre 1 et 3.")
            except ValueError:
                print("[!] Entrée invalide, veuillez entrer un nombre.")

        print(Fore.BLUE + "[+] Démarrage du crawl...")
        contact_map = crawl_domains(domains, depth, threads)

        final_contacts = []
        for domain, emails_found in contact_map.items():
            if not emails_found:
                continue
            if len(emails_found) == 1 or auto_select:
                selected_email = emails_found[0]
            else:
                print(Fore.YELLOW + f"\n[?] Plusieurs emails trouvés pour {domain}:")
                for i, e in enumerate(emails_found):
                    print(f"  [{i}] {e}")
                while True:
                    try:
                        choice = int(input("Choisissez l'email à utiliser : "))
                        if 0 <= choice < len(emails_found):
                            selected_email = emails_found[choice]
                            break
                        else:
                            print("[!] Numéro invalide.")
                    except ValueError:
                        print("[!] Entrée invalide.")
            final_contacts.append({"email": selected_email, "domain": domain})

        if not final_contacts:
            print(Fore.RED + "[!] Aucun contact valide trouvé.")
            return

        emails = generate_emails(final_contacts, config)

    print(Fore.GREEN + f"\n[+] {len(emails)} email(s) prêt(s). Aperçu avec modification possible :")
    for idx, email in enumerate(emails):
        print(Fore.MAGENTA + f"\n--- Email {idx+1} vers {email['email']} ({email['domain']}) ---")
        print(Style.BRIGHT + email["body"])
        print(Fore.YELLOW + "Souhaitez-vous modifier ce mail ? (o/N) : ", end="")
        choice = input().strip().lower()
        if choice == 'o':
            print(Fore.CYAN + "\nEntrez le nouveau contenu de l'email. Terminez avec une ligne vide :")
            lines = []
            while True:
                line = input()
                if line == '':
                    break
                lines.append(line)
            email["body"] = "\n".join(lines)

    print(Fore.YELLOW + "\nSouhaitez-vous envoyer ces emails ? (o/N) : ", end="")
    confirmation = input().strip().lower()
    if confirmation == "o":
        for email in tqdm(emails, desc="Envoi en cours", unit="email"):
            send_all_emails(email, config)
    else:
        print(Fore.CYAN + "[!] Envoi annulé. Sauvegarde du brouillon en cours...")
        save_draft(emails, "drafts/emails_draft.json")
        print(Fore.GREEN + "[✓] Brouillon sauvegardé avec succès.")

if __name__ == "__main__":
    main()
