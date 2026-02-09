import json
import os

FAV_FILE = "data/favorites.json"

# Création du dossier si nécessaire
os.makedirs("data", exist_ok=True)

# Création du fichier si nécessaire
if not os.path.exists(FAV_FILE):
    with open(FAV_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=4)


def load_favorites():
    with open(FAV_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_favorites(favs):
    with open(FAV_FILE, "w", encoding="utf-8") as f:
        json.dump(favs, f, indent=4)


def add_favorite(offer):
    favs = load_favorites()

    # éviter les doublons
    if offer not in favs:
        favs.append(offer)
        save_favorites(favs)


def remove_favorite(offer):
    favs = load_favorites()
    favs = [f for f in favs if f != offer]
    save_favorites(favs)
