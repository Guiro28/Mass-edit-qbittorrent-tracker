#!/usr/bin/env python3
"""
bulk_qbittorrent_trackers.py
-------------------------------------------------
Modifie en masse les trackers des torrents dans qBittorrent
via son API Web.
-------------------------------------------------
"""

import re
from qbittorrentapi import Client, LoginFailed

# =====================================================
# === CONFIGURATION ===================================
# =====================================================

CONFIG = {
    # --- Connexion WebUI ---
    "host": "http://127.0.0.1:8080",  # Adresse du WebUI (avec port)
    "username": "admin",
    "password": "adminadmin",
    "verify_cert": False,  # True = vérifier certificat SSL, False = ignorer (utile self-signed)

    # --- Action à exécuter ---
    # "replace" / "add" / "remove"
    "action": "replace",

    # --- Paramètres selon l’action ---
    "find": "http://old-tracker.example/announce",
    "replace": "https://new-tracker.example/announce",
    "add_url": "https://new-tracker.example/announce",

    # --- Options ---
    "use_regex": False,
    "dry_run": False,
    "only_category": None,
}
# =====================================================


def connect():
    qb = Client(
        host=CONFIG["host"],
        username=CONFIG["username"],
        password=CONFIG["password"],
        VERIFY_WEBUI_CERTIFICATE=CONFIG["verify_cert"],  # ✅ paramètre correct
    )
    try:
        qb.auth_log_in()
    except LoginFailed as e:
        raise SystemExit(f"❌ Erreur de connexion au WebUI : {e}")
    print(f"✅ Connecté à qBittorrent ({CONFIG['host']})")
    return qb


def replace_tracker(qb, torrent_hash, original, new):
    qb.torrents_edit_tracker(torrent_hash=torrent_hash, original_url=original, new_url=new)


def add_tracker(qb, torrent_hash, url):
    qb.torrents_add_trackers(torrent_hashes=torrent_hash, urls=url)


def remove_tracker(qb, torrent_hash, url):
    qb.torrents_remove_trackers(torrent_hash=torrent_hash, urls=url)


def main():
    qb = connect()
    torrents = qb.torrents_info()
    print(f"📦 {len(torrents)} torrents trouvés.")

    for t in torrents:
        if CONFIG["only_category"] and getattr(t, "category", "") != CONFIG["only_category"]:
            continue

        try:
            trackers_info = qb.torrents_trackers(t.hash)
            trackers = [tr["url"] for tr in trackers_info]
        except Exception:
            print(f"⚠️  Impossible de lire les trackers pour {t.name}")
            continue

        if CONFIG["action"] == "replace":
            for tr in trackers:
                match = (
                    re.search(CONFIG["find"], tr)
                    if CONFIG["use_regex"]
                    else CONFIG["find"] == tr
                )
                if match:
                    print(f"🔁 {t.name}: {tr} → {CONFIG['replace']}")
                    if not CONFIG["dry_run"]:
                        replace_tracker(qb, t.hash, tr, CONFIG["replace"])

        elif CONFIG["action"] == "add":
            if CONFIG["add_url"] not in trackers:
                print(f"➕ {t.name}: ajout {CONFIG['add_url']}")
                if not CONFIG["dry_run"]:
                    add_tracker(qb, t.hash, CONFIG["add_url"])

        elif CONFIG["action"] == "remove":
            for tr in trackers:
                match = (
                    re.search(CONFIG["find"], tr)
                    if CONFIG["use_regex"]
                    else CONFIG["find"] == tr
                )
                if match:
                    print(f"🗑️  {t.name}: suppression {tr}")
                    if not CONFIG["dry_run"]:
                        remove_tracker(qb, t.hash, tr)

    print("✅ Terminé.")


if __name__ == "__main__":
    main()
