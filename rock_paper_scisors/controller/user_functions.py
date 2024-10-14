count_deuce = 0
count_wins = 0
count_loses = 0

def user_rock():
   if choice_PC == "Paper":
      count_loses += 1
   elif choice_PC == "Scissors":
      count_wins += 1
   if choice_PC == "Rock":
      count_deuce += 1

def user_paper():
   if choice_PC == "Paper":
      count_deuce += 1
   elif choice_PC == "Scissors":
      count_loses += 1
   if choice_PC == "Rock":
      count_wins += 1

def user_scissors():
   if choice_PC == "Paper":
      count_wins += 1
   elif choice_PC == "Scissors":
      count_deuce += 1
   if choice_PC == "Rock":
      count_loses += 1