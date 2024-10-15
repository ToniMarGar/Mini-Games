import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow 
from PyQt6.uic import loadUi
from memory.model.Tablero import Tablero
from memory.model.Carta import Carta
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton

class Game_screen(QMainWindow):

    def __init__(self,tablero):
        super().__init__()
        loadUi("memory/view/memory.ui", self)

        self.pair=[]
        self.pair_buttons=[]
        self.tablero=tablero
        self.set_tablero_grid()

    def set_tablero_grid(self):
        for fila in range(self.tablero.board_size):
            for columna in range(self.tablero.board_size):
                valor=self.tablero.board[fila][columna]
                button = QPushButton(f"Voltear")
                button.clicked.connect(lambda captured_value, v=valor, b=button: self.funcion_boton(v,b))

                self.grid_botones.addWidget(button,fila,columna)
        
    def funcion_boton(self,carta,button):
        
        print(carta)
        if len(self.pair)<1:
            self.pair.append(carta)
            self.pair_buttons.append(button)
        else:
            if self.pair_buttons[0]!=button:
                self.pair.append(carta)
                self.pair_buttons.append(button)
                if self.pair[0]==self.pair[1]:
                    print("Pareja")
                    list(button_x.hide() for button_x in self.pair_buttons)
                else:
                    print("Try again")
                
                self.pair=[]
                self.pair_buttons=[]