import random
from time import sleep

choices = ["charmander","Squritle","bulbasar"]

computer = random.choice(choices)

player = False
name = input("Hello, please enter your name :")

while player == False:
    print(f"Hello, {name} welcome to pokeman Game!!")
    player = input("Which pokemon do you want to choose?\n'Charmander': 'Charmander'\n'Squirtle': 'Squirtle'\n'Bulbasur': 'Bulbasur'\n'Stop the game': 'Stop': ")


    if player == computer:
        print("Tie!!")
    elif player == "charmander":
        if computer == "Squirtle":
            print("\nplease,wait we are loading")
            sleep(2)
            print("You lose!!")
        else:
            print("\nplease,wait we are loading")
            sleep(2)
            print("You win!!")

    elif player == "squirtle":
        if computer == "bulbasar":
            print("\nplease,wait we are loading")
            sleep(2)
            print("You lose!!")
        else:
            print("\nplease,wait we are loading")
            sleep(2)
            print("You win!!")

    elif player == "bulbasar":
        if computer == "charmander":
            print("\nplease,wait we are loading")
            sleep(2)
            print("You lose!!")
        else:
            print("\nplease,wait we are loading")
            sleep(2)
            print("You win!!")

    elif player == "stop":
        print("Thanks for playing!!")
        break
    else:
        print("That's not a valid play!!")


    player = False

#This program is created by: Annapurna
