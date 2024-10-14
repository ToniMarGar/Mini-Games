import random

class Game():

    options = ['Rock', 'Paper', 'Scissors']
    total_win = 0
    total_lose = 0

    def __init__(self):
        self.count_loses = 0
        self.count_wins = 0
        self.count_deuce = 0

    def user_rock(self,choice_pc):

        if choice_pc == "Paper":
            self.count_loses += 1
        elif choice_pc == "Scissors":
            self.count_wins += 1
        elif choice_pc == "Rock":
            self.count_deuce += 1

        print(f"W{self.count_wins}, D{self.count_deuce}, L{self.count_loses}")
        
    def user_paper(self,choice_pc):

        if choice_pc == "Paper":
            self.count_deuce += 1
        elif choice_pc == "Scissors":
            self.count_loses += 1
        elif choice_pc == "Rock":
            self.count_wins += 1
        print(f"W{self.count_wins}, D{self.count_deuce}, L{self.count_loses}")

    def user_scissors(self,choice_pc):

        if choice_pc == "Paper":
            self.count_wins += 1
        elif choice_pc == "Scissors":
            self.count_deuce += 1
        elif choice_pc == "Rock":
            self.count_loses += 1
        print(f"W{self.count_wins}, D{self.count_deuce}, L{self.count_loses}")
    
    def update_stats(self):
        return [self.count_wins,self.count_deuce,self.count_loses]
        
    def compare_finish_game(self):
        if self.count_wins==3:
            Game.total_finish_count(True)
            return 1
        elif self.count_loses == 3:
            Game.total_finish_count(False)
            #save json
            return 1
        else:
            return 0
        
    @classmethod
    def total_finish_count(cls, win_condition):
        if win_condition is True:
            cls.total_win += 1
        else:
            cls.total_lose += 1
