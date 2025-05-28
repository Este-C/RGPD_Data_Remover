#!/bin/bash
set -e  # Stop the script on error

# Colors
CYAN='\033[1;36m'
GREEN='\033[1;32m'
NC='\033[0m'

# Title
echo -e "${CYAN}"
echo "======================================================"
echo "     Installation de RGPD_DataRemover by 6sco"
echo "======================================================"
echo -e "${NC}"

echo -e "${GREEN}[+] Mise à jour des paquets...${NC}"
sudo apt update

echo -e "${GREEN}[+] Installation de Python3, pip et venv...${NC}"
sudo apt install -y python3 python3-pip python3-venv

echo -e "${GREEN}[+] Création de l'environnement virtuel...${NC}"
python3 -m venv venv

echo -e "${GREEN}[+] Activation de l'environnement virtuel et installation des dépendances...${NC}"
# Run the following commands in a subshell
(
    source ./venv/bin/activate
    echo -e "${GREEN}[+] Installation des dépendances Python...${NC}"
    pip install --upgrade pip
    pip install -r requirements.txt
)

echo -e "${GREEN}[✓] Installation terminée.${NC}"
echo -e "${GREEN}[!] N'oubliez pas d'activer l'environnement virtuel avec 'source ./venv/bin/activate' avant d'exécuter le projet.${NC}"
echo -e "${GREEN}[!] Lançez l'app avec 'python3 main.py'${NC}"