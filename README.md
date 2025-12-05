🕷️ Smart Web Automation Agent
Scraping + Compréhension d’Objectif + Actions Réelles en Temps Réel

Scraper automatiquement n’importe quel site web (via URL entrée par l’utilisateur).

Analyser le contenu extrait pour identifier les éléments clés (images, textes, boutons, div…).

Comprendre un objectif utilisateur en langage naturel (ex. “supprimer toutes les images de sacs”, “effacer le mot promo”, “enlever les bannières rouges”…).

Exécuter réellement l’action sur le site, en temps réel, via une extension navigateur.

Montrer une démonstration live dans l’interface UI.
🚀 Fonctionnalités Principales
✔️ 1. Scraper un site web

Entrer une URL

Le système collecte la structure HTML complète

Nettoyage intelligent + extraction de structure

Visualisation dans l’interface UI

✔️ 2. Compréhension automatique d’objectif

Grâce à DeepSeek, l’agent peut comprendre automatiquement :

ce que l’utilisateur veut faire

quelles parties du site sont concernées

quels sélecteurs CSS/HTML correspondent à l’objectif

Exemples :

“Supprimer toutes les images de chaussures”

“Retirer la phrase ‘Nouveau produit’”

“Effacer la bannière en haut du site”

“Masquer les publicités”

“Enlever le mot SOLDES partout”

✔️ 3. Actions en temps réel

L’agent peut :

supprimer des images

supprimer un texte ou phrase précise

retirer des div

masquer des sections

modifier le style

restructurer l’interface

➡️ Le tout se réalise visuellement dans la démo grâce à l’intégration extension navigateur.


🧠 Technologies Utilisées
Backend

Python 3.12

Flask (API)

BeautifulSoup4 (scraping HTML)

requests (HTTP client)

DeepSeek API (LLM for objective understanding)

Frontend

HTML / JS simple

Extension navigateur (Chrome) pour exécution en direct

Modèle IA

DeepSeek V3.1 Terminus, via API :

from openai import OpenAI
client = OpenAI(base_url="...", api_key="...")





# Crawl - Scraper Crawl4AI : Défi Platon Formation – Nuit de l’Info

## Description
Crawl est un projet de scraping web interactif utilisant Flask et BeautifulSoup.  
Il permet de scrapper une page web, afficher son contenu et appliquer des actions intelligentes comme supprimer des images, boutons, logos, barres de recherche, etc.

---

## Prérequis
- Python 3.10 ou supérieur
- Git (pour cloner le projet)
- Connexion Internet

---

## Installation et setup

### 1. Cloner le dépôt
```bash
git clone https://github.com/Khatib-imen/Crawl.git
cd Crawl
