import random
import time

def spin_row():
    pass
    symbols = ['🍇', '🍍', '🍓', '⭐', '🔔']
    #result = []

    #for symbol in range(3):
        #result.append(random.choice(symbols))

    return [random.choice(symbols) for _ in range(3)]



def print_row(row):
    print("#############")
    print(" | ".join(row))
    print("#############")

def get_payout(row, bet):
    pass
    if row[0] == row[1] ==row[2]:
        if row[0] == '🍇':
            return bet * 2
        elif row[0] == '🍍':
            return bet * 4
        elif row[0] == '🍓':
            return bet * 6
        elif row[0] == '⭐':
            return bet * 8
        elif row[0] == '🔔':
            return bet * 10
    return 0


def main():
    
    balance = 100

    print("#######################################")
    print("🍇🍍🍓FRUITSLOT MACHINE🍇🍍🍓")
    print("Symbols: 🍇🍍🍓⭐🔔")
    print("#######################################")


    while balance > 0:
        print(f"Current balance: {balance} Php")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please Enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient Funds")
            continue
        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning......\n")
        time.sleep(2)
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You Won {payout}Php")
        else:
            print("Sorry You Lose This Round")

        balance += payout


if __name__=='__main__':
    main()