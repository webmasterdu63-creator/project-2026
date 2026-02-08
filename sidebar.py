from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt

class SideBar(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)

        buttons = [
            "Accueil",
            "Recherche",
            "Favoris",
            "Paramètres"
        ]

        for name in buttons:
            btn = QPushButton(name)
            btn.setFixedHeight(40)
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
            """)
            layout.addWidget(btn)

        self.setFixedWidth(180)
        self.setStyleSheet("background-color: #252525;")
