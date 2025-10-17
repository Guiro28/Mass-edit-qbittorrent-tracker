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
```

---

## ⚙️ Configuration

Tout se fait **directement dans le script** (`CONFIG` en haut du fichier) :

```python
CONFIG = {
    "host": "http://127.0.0.1:8080",
    "username": "admin",
    "password": "adminadmin",
    "verify_cert": False,
    "action": "replace",  # "replace", "add" ou "remove"
    "find": "http://old-tracker.example/announce",
    "replace": "https://new-tracker.example/announce",
    "add_url": "https://tracker.example/announce",
    "use_regex": False,
    "dry_run": True,
    "only_category": None,
}
```

---

## ▶️ Utilisation

```bash
python bulk_qbittorrent_trackers.py
```

### 🔁 Exemple : remplacer un tracker
```python
"action": "replace",
"find": "http://old-tracker.com/announce",
"replace": "https://new-tracker.net/announce",
```

### ➕ Exemple : ajouter un tracker
```python
"action": "add",
"add_url": "https://tracker.example/announce",
```

### 🗑️ Exemple : supprimer un tracker
```python
"action": "remove",
"find": "https://dead-tracker.com/announce",
```

---

## 🧠 Bonnes pratiques

- **Commence toujours par `dry_run=True`** pour vérifier les modifications avant exécution.
- Utilise `"use_regex": True` pour matcher plusieurs domaines (ex. `*.example.org`).
- En cas de connexion HTTPS auto-signée, laisse `"verify_cert": False`.

---

## 🧩 Exemple de sortie (mode dry-run)

```
✅ Connecté à qBittorrent (http://127.0.0.1:8080)
📦 42 torrents trouvés.
🔁 Film1.torrent : http://old-tracker.example/announce → https://new-tracker.example/announce
🔁 Serie2.torrent : http://old-tracker.example/announce → https://new-tracker.example/announce
✅ Terminé.
```

---

## 🪪 Licence

Ce projet est distribué sous licence **MIT**.  
Vous êtes libre de l’utiliser, le modifier et le redistribuer avec attribution.


