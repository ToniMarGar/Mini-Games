import random

count_deuce = 0
count_wins = 0
count_loses = 0

posibilities = ['Rock', 'Paper', 'Scisors']
print("Rock, Paper or Scisors? ")
choice_User = input("What do you choose? ")

for i in range(1):
   choice_PC = random.choice(posibilities)
    
if choice_PC == choice_User:
   count_deuce += 1

print(count_deuce)