import requests
from core.logger import logger

API_TOKEN_URL = "https://entreprise.francetravail.fr/connexion/oauth2/access_token?realm=/partenaire"
API_SEARCH_URL = "https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search"

# Tes identifiants France Travail
CLIENT_ID = "PAR_itjobfinder2026_9e348be54947551c54dcb05b0c802b95848270cb80f062d9f6cd4226927b8dbd"
CLIENT_SECRET = "74ab1b5fa26760ab13042b7ef027bb21e4b55fd18f93e832f461de69743c88a"


def get_token():
    """Récupère un token OAuth2 France Travail."""
    logger.info("Demande d'un token France Travail")

    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "api_offresdemploiv2"
    }

    response = requests.post(API_TOKEN_URL, data=data)
    response.raise_for_status()

    token = response.json().get("access_token")
    logger.info("Token France Travail obtenu")
    return token


def search_france_travail(job, location, contract):
    """Recherche réelle via l'API France Travail."""
    logger.info(f"Recherche France Travail : job={job}, location={location}, contract={contract}")

    token = get_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    params = {
        "motsCles": job,
        "commune": location,
        "typeContrat": contract if contract != "Tous" else None,
        "range": "0-20"
    }

    params = {k: v for k, v in params.items() if v}

    response = requests.get(API_SEARCH_URL, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()

    results = []

    for offer in data.get("resultats", []):
        results.append({
            "source": "France Travail",
            "title": offer.get("intitule"),
            "location": offer.get("lieuTravail", {}).get("libelle"),
            "contract": offer.get("typeContrat"),
            "url": offer.get("origineOffre", {}).get("urlOrigine")
        })

    logger.info(f"{len(results)} offres France Travail récupérées")
    return results
