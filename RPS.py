import random
import time

while True:
    player = input('Rock, Paper, or Scissors?: ')

    if player in ["Rock", "Paper", "Scissors"]:
        print("You: " + player)
        break  # Exit the loop if the input is valid
    else:
        print('Wrong input. Please enter Rock, Paper, or Scissors.')

# noinspection SpellCheckingInspection
ailist = ["Rock", "Paper", "Scissors"]
ai = random.choice(ailist)
time.sleep(0.9)
print("Computer:" + " " + ai)

# Results
if player == ai:
    print('DRAW')
# player wins
elif player == "Rock" and ai == "Scissors":
    print('Player wins')
elif player == "Paper" and ai == "Rock":
    print('Player wins')
elif player == "Scissors" and ai == "Paper":
    print('Player wins')
# Computer
elif player == "Scissors" and ai == "Rock":
    print('Computer wins')
elif player == "Rock" and ai == "Paper":
    print('Computer wins')
elif player == "Paper" and ai == "Scissors":
    print('Computer wins')
