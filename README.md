# 🧩 bulk_qbittorrent_trackers.py

> 🌀 Script Python pour modifier en masse les *trackers* des torrents dans **qBittorrent**, via son API Web.

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![qBittorrent](https://img.shields.io/badge/qBittorrent-4.1%2B-0099cc.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 🚀 Description

Ce script permet d’ajouter, remplacer ou supprimer des **trackers** pour tous vos torrents dans **qBittorrent**, en une seule commande.

Il utilise l’API Web officielle (`qbittorrent-api`) pour se connecter à votre instance locale ou distante de qBittorrent.  
Idéal pour :

- Migrer vers un nouveau tracker ;
- Nettoyer des trackers morts ;
- Ajouter un même tracker à tous les torrents d’un dossier ou d’une catégorie.

---

## ⚙️ Fonctionnalités

| Action | Description |
|:-------|:-------------|
| 🔁 `replace` | Remplace un tracker existant par un autre |
| ➕ `add` | Ajoute un nouveau tracker si absent |
| 🗑️ `remove` | Supprime un tracker donné |
| 🧩 `use_regex` | Support des expressions régulières |
| 🧱 `only_category` | Applique les changements uniquement à une catégorie |
| 🧪 `dry_run` | Mode test — affiche les actions sans les exécuter |

---

## 🧰 Installation

### 1️⃣ Pré-requis

- Python **3.8 ou plus récent**
- qBittorrent **4.1+**

### 2️⃣ Installation de la dépendance

```bash
pip install qbittorrent-api
