import random
print("!GUESSING GAME!")
print("Guess The Number from 1-100")

number = random.randrange(100)

guesses = 0

chances = 5


while chances > guesses:
    try:
        guess = int(input("Enter Your Guess: "))
    
    except ValueError:
        print("Invalid Input. Enter a whole number")
        continue
    guesses+=1

    if number == guess:
        print(f"{guess} = {number} YOU WIN")
        break

    elif number > guess:
        print(f"{guess} Guess Higher")

    else:
        print(f"{guess} Guess Lower")
    

    print(f"Number of Guesses {guesses}/{chances}")

if number != guess:
    print(f"{guess}:{number} YOU LOSE") 

