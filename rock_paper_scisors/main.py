import random
from user_functions import *



total_wins = 0
total_loses = 0

options = ['Rock', 'Paper', 'Scissors']
print("Rock, Paper or Scissors")
choice_User = input("What do you choose? ")
   
for i in range(1):
   choice_PC = random.choice(options)

while count_wins < 3 or count_loses < 3:
   if choice_User == "Rock":
      user_rock()
   elif choice_User == "Paper":
      user_paper()
   elif choice_User == "Scissors":
      user_scissors()
   else:
      print("Do you know to play this game? ")
   
   print(f"W{count_wins}, D{count_deuce}, L{count_loses}")