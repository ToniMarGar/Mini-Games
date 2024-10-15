import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import random
from memory.model import Carta

class Tablero:

    carta_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

    def __init__(self,board_size):
        self.board_size = board_size
        self.board=[]
        match board_size:
            case 2:
                self.types_list=Tablero.carta_list[0:2]
            case 4:
                self.types_list=Tablero.carta_list[0:8]
            case 6:
                self.types_list=Tablero.carta_list[0:18]
        self.types_list+=self.types_list
        self.create_board()

    def create_board(self):
        for i in range(self.board_size):
            new_board=[]
            for j in range(self.board_size):
                if len(self.types_list)!=0:
                    random_number=random.randint(0,len(self.types_list)-1)
                    new_board.append(self.types_list[random_number])
                    del self.types_list[random_number]

            self.board.append(new_board)

    def get_value(self,fila,columna):
        return self.board[fila][columna]