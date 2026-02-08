import logging
from logging.handlers import RotatingFileHandler
import os

# Dossier logs
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Fichier log
LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Logger principal
logger = logging.getLogger("ITJobFinder")
logger.setLevel(logging.DEBUG)

# Format
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Handler avec rotation (5 fichiers de 1 Mo)
handler = RotatingFileHandler(
    LOG_FILE, maxBytes=1_000_000, backupCount=5, encoding="utf-8"
)
handler.setFormatter(formatter)

logger.addHandler(handler)
