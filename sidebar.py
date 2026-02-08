from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QSize

class SideBar(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("SideBar")

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)

        # Liste des boutons (pour la navigation)
        self.buttons = []

        # Nom + icône
        buttons = [
            ("Accueil", "assets/icons/home.png"),
            ("Recherche", "assets/icons/search.png"),
            ("Favoris", "assets/icons/star.png"),
            ("Paramètres", "assets/icons/settings.png"),
        ]

        for name, icon_path in buttons:
            btn = QPushButton(name)
            btn.setIcon(QIcon(icon_path))
            btn.setIconSize(QSize(24, 24))
            btn.setFixedHeight(45)
            btn.setCheckable(True)

            btn.setStyleSheet("""
                QPushButton {
                    background-color: #2d2d2d;
                    color: white;
                    border: none;
                    text-align: left;
                    padding-left: 15px;
                }
                QPushButton:hover {
                    background-color: #3a3a3a;
                }
                QPushButton:checked {
                    background-color: #00ff99;
                    color: #000;
                    font-weight: bold;
                }
            """)

            layout.addWidget(btn)
            self.buttons.append(btn)

        self.setFixedWidth(180)
        self.setStyleSheet("background-color: #252525;")
