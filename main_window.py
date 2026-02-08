from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
)
from PySide6.QtCore import Qt
from .sidebar import SideBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("IT Job Finder 2026")
        self.setMinimumSize(1100, 700)

        # Layout principal
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)

        # Barre latérale
        self.sidebar = SideBar()
        main_layout.addWidget(self.sidebar)

        # Zone centrale
        self.content = QLabel("Bienvenue dans IT Job Finder 2026")
        self.content.setAlignment(Qt.AlignCenter)
        self.content.setStyleSheet("font-size: 22px; color: white;")

        main_layout.addWidget(self.content, stretch=1)

        self.setCentralWidget(main_widget)

        # Style sombre temporaire
        self.setStyleSheet("""
            QMainWindow { background-color: #1e1e1e; }
            QLabel { color: #e0e0e0; }
        """)

