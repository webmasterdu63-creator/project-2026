from core.logger import logger

from .linkedin_api import search_linkedin
from .indeed_api import search_indeed
from .wttj_api import search_wttj
from .poleemploi_api import search_pole_emploi


def search_all(job, location, contract):
    logger.info(f"Recherche globale : job='{job}', location='{location}', contract='{contract}'")

    results = []

    try:
        results += search_linkedin(job, location, contract)
    except Exception as e:
        logger.error(f"Erreur LinkedIn : {e}")

    try:
        results += search_indeed(job, location, contract)
    except Exception as e:
        logger.error(f"Erreur Indeed : {e}")

    try:
        results += search_wttj(job, location, contract)
    except Exception as e:
        logger.error(f"Erreur WTTJ : {e}")

    try:
        results += search_pole_emploi(job, location, contract)
    except Exception as e:
        logger.error(f"Erreur Pôle Emploi : {e}")

    return results

