# 🕷️ Smart Web Automation Agent  
 *Scraping + Compréhension d’Objectif + Actions Réelles en Temps Réel**
<p align="center"> <img src="https://img.shields.io/badge/AI-Agent-black?style=for-the-badge"/> <img src="https://img.shields.io/badge/DeepSeek-Powered-blue?style=for-the-badge"/> <img src="https://img.shields.io/badge/Web_Automation-Active-green?style=for-the-badge"/> </p>

---

 ## 🌐 Description du Projet
 **Smart Web Automation Agent** est un agent IA capable de :
 - 🔍 Scraper automatiquement n’importe quel site web  
 - 🧠 Comprendre un objectif utilisateur en langage naturel  
 - 🕹️ Exécuter des actions réelles en temps réel via extension navigateur  
 - 🧷 Identifier dynamiquement les bons sélecteurs CSS  
 - 🎥 Afficher les résultats en démo live dans une interface UI  

 Le tout **sans règles codées manuellement** :  
 → L’IA choisit *elle-même* la meilleure stratégie.

---

 ## 🚀 Fonctionnalités Principales

### ✔️ 1. Scraper un site web
 - Entrer une **URL**  
 - Extraction complète de la structure HTML  
 - Nettoyage intelligent  
 - Prévisualisation immédiate dans l’UI  

### ✔️ 2. Compréhension intelligente d'objectif
 L’agent comprend automatiquement les intentions :
 - “Supprimer toutes les images de chaussures”  
 - “Retirer le mot promo”  
 - “Enlever la bannière rouge”  
 - “Effacer la phrase Nouveau produit”  

 L’IA déduit :
 - 🎯 L’objectif exact  
 - 🧩 Les éléments visés  
 - 🧷 Les sélecteurs CSS  
 - ⚡ Le plan d'exécution  

### ✔️ 3. Actions en temps réel
 Capable de :  
 - 🖼️ Supprimer images spécifiques  
 - 📝 Effacer mots/phrases dans la page  
 - 🎨 Modifier couleur/style/structure  
 - 🗑️ Retirer sections, pubs, divs  
 - 🔧 Refaire la mise en page  

 Tout cela **se produit directement sur le site réel**, visible par l’utilisateur.

---

> ## 🧠 Technologies Utilisées

### Backend
 - Python 3.12  
 - Flask  
 - BeautifulSoup4  
 - requests  
 - dotenv  

### IA / LLM
 - DeepSeek V3.1 Terminus  
 ```python
 from openai import OpenAI
 client = OpenAI(base_url="...", api_key="...")
 ```

### Frontend
 - HTML + JavaScript  
 - UI simple et rapide  

### Extension Navigateur
 - Chrome Extension  
 - Manipulation DOM en temps réel
 - 
### 🎬 Démonstration — Étapes en Images
🖼️ Étape 1 : Entrée de l’URL pour scraping
<img width="1795" height="788" alt="capt1" src="https://github.com/user-attachments/assets/e3d4838b-4507-4bce-8b5b-4d7f2721562e" />


🖼️ Étape 2 : L'utilisateur saisit son objectif

<img width="1792" height="787" alt="capt2" src="https://github.com/user-attachments/assets/9515da81-86b5-4870-82b9-72c2f3f7f240" /><img width="1797" height="792" alt="capt4" src="https://github.com/user-attachments/assets/ccba14c0-9296-460a-8edf-c6ba26788ca1" />


🖼️ Étape 3 : L’IA comprend, génère les sélecteurs et exécute

<img width="1787" height="805" alt="capt3" src="https://github.com/user-attachments/assets/4cf5d3a7-8472-481c-b41b-dc1285242351" /> <img width="1786" height="791" alt="capt5" src="https://github.com/user-attachments/assets/13c82319-0514-4c09-9036-70d57c835813" />

---

## 🛠️ Installation & Exécution
📥 1. Cloner le projet
```bash
git clone https://github.com/Khatib-imen/Smart_Web_Automation_Agent.git
cd Smart_Web_Automation_Agent
🧰 2. Créer un environnement virtuel

bash
Copier le code
python -m venv .venv
🔌 3. Activer l’environnement
Windows :

bash
Copier le code
.venv\Scripts\activate
Mac/Linux :

bash
Copier le code
source .venv/bin/activate
📦 4. Installer les dépendances

bash
Copier le code
pip install -r requirements.txt
▶️ 5. Lancer le backend

bash
Copier le code
python backend/app.py
🖥️ 6. Ouvrir l’interface utilisateur
Ouvrir le fichier :

bash
Copier le code
frontend/index.html
🧩 7. Installer l’extension navigateur
Dans Chrome :

Ouvrir : chrome://extensions

Activer Mode développeur

Cliquer sur Charger l’extension non empaquetée

Sélectionner le dossier : extension/


🤝 Contribuer
Les contributions sont les bienvenues :
✔️ Amélioration du scraping
✔️ Ajout d’actions DOM
✔️ Intégration avec d’autres IA
✔️ Optimisation Front/Back
✔️ Support Firefox & Edge

---



👨‍💻 Auteur

Imen Khatib
