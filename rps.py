from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False

while player == False:
    player = input("Rock, Paper, Scissors? ")
    if player == computer:
        print("👍ITS A TIE👍")
    elif player == "Rock":
        if computer == "Paper":
            print(f"You Lose!!!😆 {computer} covers {player}")
        else:
            print(f"You Win!!!🥳 {player} destroys {computer}")
    elif player == "Paper":
        if computer == "Scissors":
            print(f"You Lose!!!😆 {computer} cuts {player}")
        else:
            print(f"You Win!!!🥳 {player} covers {computer}")
    elif player == "Scissors":
        if computer == "Rock":
            print(f"You Lose!!!😆 {computer} destroys {player}")
        else:
            print(f"You Win!!!🥳 {player} cuts {computer}")
    elif player == "Niño Amos":
        print("Ewww Bigaon🤮")
    else:
        print("Invalid Input, Check Your Spelling")

    player = False
    computer = t[randint(0,2)]