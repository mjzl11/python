import random

def play_game(player_choice):
    # Generar la elección del oponente de forma aleatoria
    choices = ['rock', 'paper', 'scissors']
    opponent_choice = random.choice(choices)
    
    # Mostrar las elecciones
    print("Tu elección:", player_choice)
    print("Elección del oponente:", opponent_choice)
    
    # Determinar el resultado del juego
    if player_choice == opponent_choice:
        result = "Empate"
    elif (player_choice == 'rock' and opponent_choice == 'scissors') or \
         (player_choice == 'paper' and opponent_choice == 'rock') or \
         (player_choice == 'scissors' and opponent_choice == 'paper'):
        result = "¡Ganaste!"
    else:
        result = "¡Perdiste!"
    
    # Mostrar el resultado
    print(result)

# Obtener la elección del jugador
player_choice = input("Elige 'rock', 'paper' o 'scissors': ").lower()

# Verificar la elección del jugador y jugar el juego
if player_choice in ['rock', 'paper', 'scissors']:
    play_game(player_choice)
else:
    print("Elección inválida. Debes elegir 'rock', 'paper' o 'scissors'.")