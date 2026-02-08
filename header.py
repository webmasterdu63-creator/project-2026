from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class Header(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 10, 15, 10)
        layout.setSpacing(20)

        # ===== LOGO =====
        logo = QLabel()
        pix = QPixmap("assets/logo.png")  # Mets ton logo ici
        pix = pix.scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo.setPixmap(pix)
        layout.addWidget(logo)

        # ===== TITRE =====
        title = QLabel("IT Job Finder 2026")
        title.setStyleSheet("font-size: 22px; font-weight: bold; color: #00ff99;")
        layout.addWidget(title)

        layout.addStretch()

        # ===== BARRE DE RECHERCHE GLOBALE =====
        self.global_search = QLineEdit()
        self.global_search.setPlaceholderText("Recherche rapide...")
        self.global_search.setFixedWidth(300)
        layout.addWidget(self.global_search)

        self.setStyleSheet("""
            QWidget {
                background-color: #111;
                border-bottom: 1px solid #222;
            }
            QLineEdit {
                background-color: #1f1f1f;
                border: 1px solid #333;
                padding: 6px;
                border-radius: 4px;
                color: white;
            }
            QLineEdit:focus {
                border: 1px solid #00ff99;
            }
        """)
