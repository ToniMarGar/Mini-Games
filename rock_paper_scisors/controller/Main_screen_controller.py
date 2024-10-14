import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow 
from PyQt6.uic import loadUi
from rock_paper_scisors.model.Game import Game

class Main_screen(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("rock_paper_scisors/view/main_screen.ui", self)  # Cargar el diseño desde un archivo .ui

        self.game=Game()

        #conectar botones
        self.piedra_button.clicked.connect(lambda:self.exec_method(self.game.user_rock))
        self.tijera_button.clicked.connect(lambda:self.exec_method(self.game.user_scissors))
        self.papel_button.clicked.connect(lambda:self.exec_method(self.game.user_paper))

    def exec_method(self,func):
        random_enemy= random.choice(Game.options)
        func(random_enemy)
        self.feedback_label.setText(random_enemy)
        actual_stats = self.game.update_stats()

        self.update_labels(actual_stats)
        self.continue_playing()

    def update_labels(self,actual_stats):
        self.count_win_label.setText(str(actual_stats[0]))
        self.count_deuce_label.setText(str(actual_stats[1]))
        self.count_loses_label.setText(str(actual_stats[2]))
    
    def continue_playing(self):
        result=self.game.compare_finish_game()
        match result:
            case 1:
                self.finish_game()
            case 0:
                pass
    
    def finish_game(self):
        self.game=Game()

    
def main():
    app = QApplication(sys.argv)
    window = Main_screen()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()