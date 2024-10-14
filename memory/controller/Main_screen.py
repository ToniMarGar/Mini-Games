import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow 
from PyQt6.uic import loadUi


class Main_screen(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("memory/view/memory.ui", self)  # Cargar el diseño desde un archivo .ui
        
        #conectar botones
     

    def exec_method(self,func):
       pass
    

def main():
    app = QApplication(sys.argv)
    window = Main_screen()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()