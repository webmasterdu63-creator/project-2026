from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PySide6.QtCore import Qt

class PageSearch(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Recherche d'offres")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 22px; font-weight: bold;")

        search_input = QLineEdit()
        search_input.setPlaceholderText("Rechercher un poste (ex: Administrateur Systèmes, DevOps...)")

        btn_search = QPushButton("Lancer la recherche")

        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(search_input)
        layout.addWidget(btn_search)
        layout.addStretch()
