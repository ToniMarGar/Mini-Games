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
import time

class Game_screen(QMainWindow):

    def __init__(self,tablero):
        super().__init__()
        loadUi("memory/view/memory.ui", self)

        self.pair=[]
        self.pair_buttons=[]
        self.buttons=[]

        self.tablero=tablero
        self.set_tablero_grid()

        self.intentos=0
        self.parejas_hechas=0



    def set_tablero_grid(self):
        for fila in range(self.tablero.board_size):
            for columna in range(self.tablero.board_size):
                valor=self.tablero.board[fila][columna]
                button = QPushButton(f"Voltear")
                button.clicked.connect(lambda captured_value, v=valor, b=button: self.funcion_boton(v,b))
                self.buttons.append(button)
                self.grid_botones.addWidget(button,fila,columna)
        
    def funcion_boton(self,carta,button):
        print(str(carta))
        
        if len(self.pair)<1:
            list(button_y.setText("Voltear") for button_y in self.buttons)

            self.pair.append(carta)
            self.pair_buttons.append(button)

            button.setText(str(carta))
        else:
            button.setText(str(carta))

            self.intentos+=1
            self.label_points.setText(str(self.intentos))

            if self.pair_buttons[0]!=button:
                self.pair.append(carta)
                self.pair_buttons.append(button)
                if self.pair[0]==self.pair[1]:
                    print("Pareja")
                    list(button_x.hide() for button_x in self.pair_buttons)          
                    self.parejas_hechas+=1         
                else:
                    print("Try again")
                    #time.sleep(1)
                    
                    
                
                self.pair=[]
                self.pair_buttons=[]
            
        if self.parejas_hechas>=self.tablero.num_parejas:
            self.finish_game()

    def finish_game(self):
        self.close()
        print("ADJASJIDA")