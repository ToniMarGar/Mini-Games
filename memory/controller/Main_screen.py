import random
import sys
import os

from Game_screen import Game_screen
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow 
from PyQt6.uic import loadUi
from memory.model.Tablero import Tablero
from memory.model.Carta import Carta
import time

class Main_screen(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("memory/view/menu.ui", self)

        self.easy_button.clicked.connect(lambda: self.exec_method(1))
        self.medium_button.clicked.connect(lambda: self.exec_method(2))
        self.hard_button.clicked.connect(lambda: self.exec_method(3))

    def exec_method(self,option):
        
        match option:
            case 1:
                tablero = Tablero(2)    
            case 2:
                tablero = Tablero(4)        
            case 3:
                tablero = Tablero(6)  
        self.second_window = Game_screen(tablero) 
        self.second_window.show()
        self.close()

def main():
    app = QApplication(sys.argv)
    window = Main_screen()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()