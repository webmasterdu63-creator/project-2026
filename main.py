from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.splash_screen import SplashScreen
import sys
import time

def main():
    app = QApplication(sys.argv)

    # Splash screen
    splash = SplashScreen()
    splash.show()

    # Simulation du chargement (API, config, etc.)
    time.sleep(2)

    # Lancement de la fenêtre principale
    window = MainWindow()
    window.show()

    splash.finish(window)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
