from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QComboBox, QListWidget
)
from PySide6.QtCore import Qt


class PageSearch(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)

        # ====== TITRE ======
        title = QLabel("Recherche d'offres")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 22px; font-weight: bold;")
        main_layout.addWidget(title)
        main_layout.addSpacing(15)

        # ====== FILTRES ======
        filters_layout = QHBoxLayout()

        # Poste recherché
        self.input_job = QLineEdit()
        self.input_job.setPlaceholderText("Poste (ex: Administrateur Systèmes, DevOps...)")
        filters_layout.addWidget(self.input_job)
from core.favorites import add_favorite

        # Localisation
        self.input_location = QLineEdit()
        self.input_location.setPlaceholderText("Lieu (ex: Paris, Remote...)")
        filters_layout.addWidget(self.input_location)

        # Type de contrat
        self.combo_contract = QComboBox()
        self.combo_contract.addItems([
            "Tous",
            "CDI",
            "CDD",
            "Alternance",
            "Stage",
            "Freelance"
        ])
        filters_layout.addWidget(self.combo_contract)

        main_layout.addLayout(filters_layout)
        main_layout.addSpacing(10)

        # ====== BOUTON RECHERCHE ======
        self.btn_search = QPushButton("Lancer la recherche")
        self.btn_search.setFixedHeight(40)
        main_layout.addWidget(self.btn_search)

        # ====== RÉSULTATS ======
        results_label = QLabel("Résultats :")
        results_label.setStyleSheet("font-size: 18px; font-weight: bold; margin-top: 15px;")
        main_layout.addWidget(results_label)
self.results_list.itemDoubleClicked.connect(self.add_to_favorites)

        self.results_list = QListWidget()
        main_layout.addWidget(self.results_list)

        # ====== ACTION DU BOUTON ======
        self.btn_search.clicked.connect(self.fake_search)

   def fake_search(self):
    self.results_list.clear()

    job = self.input_job.text() or "Poste"
    location = self.input_location.text() or "Lieu"
    contract = self.combo_contract.currentText()

    logger.info("Recherche API lancée")

    results = search_all(job, location, contract)

    for offer in results:
        self.results_list.addItem(
            f"[{offer['source']}] {offer['title']} - {offer['location']} ({offer['contract']})"
        )

        # Résultats simulés
        fake_results = [
            f"{job} - {location} ({contract})",
            f"{job} Junior - {location} ({contract})",
            f"{job} Senior - {location} ({contract})",
        ]

        self.results_list.addItems(fake_results)
from api.search_engine import search_all
from core.logger import logger
