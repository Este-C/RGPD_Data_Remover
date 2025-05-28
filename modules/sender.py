# modules/sender.py
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_all_emails(contact, config):
    smtp_server = config.get("smtp_server", "smtp.gmail.com")
    smtp_port = config.get("smtp_port", 587)
    sender_email = config.get("email")
    password = config.get("password")

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = contact["email"]
    msg["Subject"] = "Demande de suppression de données personnelles (RGPD)"

    msg.attach(MIMEText(contact["body"], "plain"))

    # Pièce jointe éventuelle (copie de pièce d'identité)
    identity_path = config.get("piece_identite")
    if identity_path and os.path.exists(identity_path):
        with open(identity_path, "rb") as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename=\"{os.path.basename(identity_path)}\"",
            )
            msg.attach(part)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.send_message(msg)
            print(f"[+] Email envoyé à {contact['email']} pour le domaine {contact['domain']}")
    except Exception as e:
        print(f"[!] Erreur lors de l'envoi à {contact['email']} : {e}")
