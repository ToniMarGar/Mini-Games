import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow 

from PyQt6.uic import loadUi

class Main_screen(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("rock_paper_scisors/view/main_screen.ui", self)  # Cargar el diseño desde un archivo .ui
 
def main():
    app = QApplication(sys.argv)
    window = Main_screen()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()