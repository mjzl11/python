import random

def playGame(playerChoice):
    choices = ['rock', 'paper', 'scissors']
    opponentChoice = random.choice(choices)
    
    print("Your choise:", playerChoice)
    print("Oponent choise:", opponentChoice)

    if playerChoice == opponentChoice:
        result = "Draw"
    elif (playerChoice == 'rock' and opponentChoice == 'scissors') or \
         (playerChoice == 'paper' and opponentChoice == 'rock') or \
         (playerChoice == 'scissors' and opponentChoice == 'paper'):
        result = "¡Win!"
    else:
        result = "¡Lose!"
    
    print(result)

playerChoice = input("Choise 'rock', 'paper' o 'scissors': ").lower()

if playerChoice in ['rock', 'paper', 'scissors']:
    playGame(playerChoice)
else:
    print("Bad choise. Please choise 'rock', 'paper' o 'scissors': ")