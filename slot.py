import random
import time

def spin_grid():
    symbols = ['🍇', '🍍', '🍓', '⭐', '🔔']
    #result = []

    #for symbol in range(3):
        #result.append(random.choice(symbols))

    return [[random.choice(symbols) for _ in range (3)] for _ in range(3)]



def print_slot_machine(grid):
    print("#############")
    for row in grid:
        print(" | ".join(row))
    print("#############")

def payout_symbol(symbol, bet):
    if symbol == '🍇':
        return bet * 2
    elif symbol == '🍍':
        return bet * 4
    elif symbol == '🍓':
        return bet * 6
    elif symbol == '⭐':
        return bet * 8
    elif symbol == '🔔':
        return bet * 10
    return 0

def get_payout(grid, bet):
    total_payout = 0
    winning_lines = []
    for i, row in enumerate(grid):
        if row[0] == row[1] == row[2]:
           p = payout_symbol(row[0], bet)
           total_payout += p
           winning_lines.append(f"Row {i+1} matched {row[0]} (+{p} Php)")

    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col]:
            p = payout_symbol(grid[0][col], bet)
            total_payout += p
            winning_lines.append(f"Column {col+1} matched {grid[0][col]} (+{p} Php)")

    if grid[0][0] == grid[1][1] == grid[2][2]:
        p = payout_symbol(grid[0][0], bet)
        total_payout += p
        winning_lines.append(f"Diagonal (\\) matched {grid[0][0]} (+{p} Php)")
    
    if grid[0][2] == grid[1][1] == grid[2][0]:
        p = payout_symbol(grid[0][2], bet)
        total_payout += p
        winning_lines.append(f"Diagonal (/) matched {grid[0][2]} (+{p} Php)")

    return total_payout, winning_lines
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

        grid = spin_grid()
        print("Spinning......\n")
        time.sleep(2)
        print_slot_machine(grid)

        payout, win_lines = get_payout(grid, bet)
        
        if payout > 0:
            for line in win_lines:
                print("Winning Lines: >>", line)
                #print(f"Number of Winning Lines: {lines}")
            print(f"You Won {payout}Php\n")
        else:
            print("Sorry You Lose This Round\n")

        balance += payout


if __name__=='__main__':
    main()
