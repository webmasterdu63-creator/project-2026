from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QComboBox, QListWidget
)
from PySide6.QtCore import Qt
from core.favorites import add_favorite


class PageSearch(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        main_layout = QVBoxLayout(self)

        # Titre
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

        # ====== BOUTON RECHERCHER ======
        self.btn_search = QPushButton("Rechercher")
        self.btn_search.setStyleSheet("padding: 8px; font-size: 16px;")
        main_layout.addWidget(self.btn_search)

        # ====== LISTE DES RÉSULTATS ======
        self.results_list = QListWidget()
        main_layout.addWidget(self.results_list)

        # ====== BOUTON FAVORIS ======
        self.btn_favorite = QPushButton("Ajouter aux favoris")
        self.btn_favorite.setStyleSheet("padding: 6px;")
        main_layout.addWidget(self.btn_favorite)

        # Connexions
        self.btn_search.clicked.connect(self.fake_search)
        self.btn_favorite.clicked.connect(self.add_selected_to_favorites)

    # ====== MÉTHODES ======

    def fake_search(self):
        """Simule une recherche (en attendant l'intégration API)."""
        self.results_list.clear()

        job = self.input_job.text()
        location = self.input_location.text()
        contract = self.combo_contract.currentText()

        # Résultats fictifs
        results = [
            f"{job} - {location} ({contract})",
            f"{job} Junior - {location} ({contract})",
            f"{job} Senior - {location} ({contract})"
        ]

        self.results_list.addItems(results)

    def add_selected_to_favorites(self):
        """Ajoute l'offre sélectionnée aux favoris."""
        selected = self.results_list.currentItem()
        if selected:
            add_favorite(selected.text())
