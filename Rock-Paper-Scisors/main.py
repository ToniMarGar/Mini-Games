import random
import user_functions

count_deuce = 0
count_wins = 0
count_loses = 0

total_wins = 0
total_loses = 0

options = ['Rock', 'Paper', 'Scissors']
print("Rock, Paper or Scissors")
choice_User = input("What do you choose? ")
   
for i in range(1):
   choice_PC = random.choice(options)
   
if choice_PC == choice_User:
   count_deuce += 1

def user_rock():
   if choice_PC == "Paper":
      count_loses += 1
   elif choice_PC == "Scissors":
      count_wins += 1
   if choice_PC == "Rock":
      count_deuce += 1

if choice_User == "Rock":
   user_rock()