
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import random
from memory.model import Carta

class Tablero:

    carta_list=[0,0]

    def __init__(self,board_size):
        self.board_size = board_size
        self.board=[]
        match board_size:
            case 2:
                self.types_list=Tablero.carta_list[0:1]
            case 4:
                self.types_list=Tablero.carta_list[0:7]
            case 6:
                self.types_list=Tablero.carta_list[0:15]
        self.types_list.append(self.types_list)
        print(self.types_list)

    def create_board(self):
        
        for i in range(self.board_size):
            new_board=[]
            for j in range(self.board_size):
                random_number=random.randint(0,len(self.types_list))
                print(random_number)
                new_board.append(self.types_list[random_number])
                self.types_list.remove(random_number)

            self.board.append(new_board)



objeto = Tablero(2)
objeto.create_board()

        
