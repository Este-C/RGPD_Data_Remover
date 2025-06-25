# 🛡️ RGPD Data Remover | 🇬🇧 GDPR Data Remover

**🇫🇷 Automatisez vos demandes de suppression de données personnelles conformément au RGPD**
**🇬🇧 Automate your personal data deletion requests in compliance with GDPR**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GDPR Compliant](https://img.shields.io/badge/GDPR-Compliant-green.svg)](https://gdpr.eu/)


---

## 📁 Structure du Projet

```
RGPD_Data_Remover/
├── assets/
│   ├── email_templates/        # Templates de demandes RGPD
│   │   ├── account_deletion.txt
│   │   └── deletion_request.txt
│   └── identite/              # Vos données d'identité
│       └── carte d'identitée
├── domains.txt                # Liste des domaines à traiter
├── drafts/                   # Brouillons des emails
│   └── emails_draft.json
├── emails_sent/              # Historique des envois
├── modules/                  # Modules Python
│   ├── crawler.py           # Extraction des emails
│   ├── email_builder.py     # Construction des messages
│   ├── sender.py            # Envoi des emails
│   └── utils.py             # Utilitaires
├── INSTALL.sh               # Script d'installation
├── main.py                  # Point d'entrée principal
├── requirements.txt         # Dépendances Python
└── README.md               # Cette documentation
```
---
## 🚀 Installation et Lancement Initial

### Prérequis
- **Python 3.8+** installé sur votre système
- **Compte Gmail** avec l'authentification à deux facteurs activée
- **Connexion Internet** stable

### Installation Automatique

```bash
# Clonez le repository
git clone https://github.com/Este-C/RGPD_Data_Remover.git
cd RGPD_Data_Remover

# Lancez l'installation automatique
bash INSTALL.sh
```

Le script `INSTALL.sh` va automatiquement :
- ✅ Vérifier la version de Python
- ✅ Créer un environnement virtuel
- ✅ Installer toutes les dépendances
- ✅ Configurer les permissions nécessaires

### Configuration Gmail

**⚠️ Important** : Pour envoyer des emails via Gmail, vous devez générer un mot de passe d'application.

1. **Activez l'authentification à deux facteurs** sur votre compte Google
2. **Générez un mot de passe d'application** :
   - Suivez ce guide officiel : [Comment générer un mot de passe d'application Gmail](https://support.google.com/mail/answer/185833)
   - Sélectionnez "Autre (nom personnalisé)" et nommez-le "RGPD Data Remover"
3. **Utilisez ce mot de passe** dans l'application (pas votre mot de passe Gmail habituel)

**Ressources Gmail :**
- [Configuration SMTP Gmail](https://support.google.com/a/answer/176600?hl=en)
- [Sécurité des comptes Google](https://support.google.com/accounts/answer/6010255)

---

## 🎮 Utilisation

### Lancement de l'Application

```bash
# Activez l'environnement virtuel (si pas déjà fait)
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Lancez l'application
python3 main.py
```

### Configuration Initiale

1. **Configurez vos informations personnelles** dans `assets/identite/`
2. **Ajoutez vos domaines cibles** dans `domains.txt`
3. **Personnalisez les templates** dans `assets/email_templates/` si nécessaire

### Processus d'Envoi

1. L'application crawle automatiquement les domaines
2. Extrait les adresses email de contact/DPO
3. Génère des emails personnalisés conformes au RGPD
4. Envoie les demandes et enregistre l'historique


---

## ⚖️ Cadre Juridique RGPD

### Vos Droits Fondamentaux

Cette application s'appuie sur vos droits garantis par le **Règlement Général sur la Protection des Données (RGPD)** :

- **Article 17 - Droit à l'effacement** : [Lire le texte officiel](https://gdpr-info.eu/art-17-gdpr/)
- **Article 12 - Modalités d'exercice des droits** : [Lire le texte officiel](https://gdpr-info.eu/art-12-gdpr/)
- **Article 21 - Droit d'opposition** : [Lire le texte officiel](https://gdpr-info.eu/art-21-gdpr/)

### Références Légales

- 📚 **Texte complet du RGPD** : [EUR-Lex](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32016R0679)
- 🏛️ **Commission Européenne - RGPD** : [Site officiel](https://ec.europa.eu/info/law/law-topic/data-protection/data-protection-eu_fr)
- 🇫🇷 **CNIL - Guide pratique** : [Vos droits](https://www.cnil.fr/fr/les-droits-pour-maitriser-vos-donnees-personnelles)
- 🌍 **EDPB - Lignes directrices** : [Site officiel](https://edpb.europa.eu/guidelines_fr)

### Ressources Utiles
- [Guide RGPD pour les particuliers](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre2#Article12)
- [Modèles de demandes RGPD](https://www.cnil.fr/fr/modeles/courrier)
- [Vos droits numériques en Europe](https://digital-strategy.ec.europa.eu/en/policies/digital-rights)

---

## 📄 Licence et Mentions Légales

### Licence MIT
Ce projet est distribué sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

### Disclaimer
Cette application est fournie à des fins éducatives et d'automatisation personnelle. L'auteur ne peut être tenu responsable de l'usage qui en est fait. Vérifiez toujours la conformité de vos demandes avec la législation applicable.

### Crédits
- **Développeur** : [Este-C](https://github.com/Este-C)
---

**Protégez votre vie privée. C'est votre droit. 🛡️**


*Dernière mise à jour : Juin 2025*
*Version : 1.0.0*
