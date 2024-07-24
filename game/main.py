import matplotlib.pyplot as plt

"""Piedra, papel o tijera!


Piedra, papel o tijera hecho en Python en espaniol.
"""

import random


def computer_choice():
    """Obtiene una elección aleatoria entre las opciones."""

    computer= random.choice(options)
    return computer


def user_choice():
    """Obtiene la entrada del usuario."""

    user= str(input("Elije! round: Piedra, papel o tiejra.\n"))
    user= user.lower()
    if user in options:
        return user
    else:
        raise Exception("Elige bien, cuyeyo.")


def run_game():
    """Inicia el juego y lo maneja hasta el final."""

    rounds= 3
    user_win= 0
    computer_win= 0

    print("*" * 15)
    print("¡Prepárate!.")
    print("*" * 15)
    
    while True:

        computer= computer_choice()
        user= user_choice()
        print(f"{user} vs {computer}, ")
            

        if user == computer:

            rounds -= 1
            print(f"""

            ¡Empate!
            Los dos escogieron {user}.
            {rounds} rondas por jugar.

            """)


        if (user == "tijera" and computer == "papel") or (user == "piedra" and computer == "tijera") or (user == "papel" and computer == "piedra"):
        
            rounds -= 1
            user_win += True

            print(f"""
            
            ¡Ganaste esta ronda!
            {user} vence {computer}!
            {rounds} rondas por jugar.

            """)


        if (computer == "tijera" and user == "papel") or (computer == "piedra" and user == "tijera") or (computer == "papel" and user == "piedra"):
    
            rounds -= 1
            computer_win += True
            
            print(f"""
            
            Perdiste esta ronda.
            {computer} vence a {user}!
            {rounds} rondas por jugar.

            """)

        
        if rounds <= 0:
            if user_win == computer_win:
                print("Empate entre la computadora y el juegador.")
                break
            if computer_win > user_win:
                print(f"Perdiste, la computadora obtuvo {computer_win} puntos.")
                break
            if computer_win < user_win:
                print(f"¡Ganaste con {user_win} puntos!")
                break

            plt.plot()

        


if __name__ == "__main__":
    # Global choice options.
    options= ("piedra", "papel", "tijera")
    run_game()