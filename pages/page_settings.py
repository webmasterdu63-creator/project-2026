from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QCheckBox
from PySide6.QtCore import Qt

class PageSettings(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Paramètres")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 22px; font-weight: bold;")

        darkmode = QCheckBox("Activer le thème sombre")
        notifications = QCheckBox("Activer les notifications")

        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(darkmode)
        layout.addWidget(notifications)
        layout.addStretch()
