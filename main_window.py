from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QStackedWidget
)
from PySide6.QtCore import Qt

from .sidebar import SideBar
from .header import Header
from .pages.page_home import PageHome
from .pages.page_search import PageSearch
from .pages.page_favorites import PageFavorites
from .pages.page_settings import PageSettings


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("IT Job Finder 2026")
        self.setMinimumSize(1100, 700)

        # ===== LAYOUT PRINCIPAL VERTICAL =====
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ===== HEADER =====
        self.header = Header()
        main_layout.addWidget(self.header)

        # ===== CONTENU (SIDEBAR + PAGES) =====
        content_layout = QHBoxLayout()
        main_layout.addLayout(content_layout)

        # Sidebar
        self.sidebar = SideBar()
        content_layout.addWidget(self.sidebar)

        # Zone centrale
        self.stack = QStackedWidget()
        content_layout.addWidget(self.stack, stretch=1)

        # Pages
        self.page_home = PageHome()
        self.page_search = PageSearch()
        self.page_favorites = PageFavorites()
        self.page_settings = PageSettings()

        self.stack.addWidget(self.page_home)
        self.stack.addWidget(self.page_search)
        self.stack.addWidget(self.page_favorites)
        self.stack.addWidget(self.page_settings)

        self.setCentralWidget(main_widget)

        # Navigation
        self.sidebar.buttons[0].clicked.connect(lambda: self.switch_page(0))
        self.sidebar.buttons[1].clicked.connect(lambda: self.switch_page(1))
        self.sidebar.buttons[2].clicked.connect(lambda: self.switch_page(2))
        self.sidebar.buttons[3].clicked.connect(lambda: self.switch_page(3))

        self.sidebar.buttons[0].setChecked(True)
        self.stack.setCurrentIndex(0)

    def switch_page(self, index):
        self.stack.setCurrentIndex(index)
        for btn in self.sidebar.buttons:
            btn.setChecked(False)
        self.sidebar.buttons[index].setChecked(True)
        from core.logger import logger
