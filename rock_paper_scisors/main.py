import random


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