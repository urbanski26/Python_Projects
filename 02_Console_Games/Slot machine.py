import random

def spin_row():
    symbols = ['🌶', '🎲', '🪩', '❤', "💩"]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("********")
    print("|".join(row))
    print("********")
    print()

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        print("You won!")
        return bet * 100
    else:
        print("You failed")
        return 0


def main():
    balance = 100

    print("**************************")
    print("Welcome to the Slots Machine")
    print("Symbols: 🌶️🎲🪩❤️💩")
    print("**************************")

    while balance > 0:
        print(f"Current balance: ${balance:.2f}")

        bet = input("Enter your bet: ")

        if not bet.isdigit():
            print("Please enter a valid bet")
            continue

        bet = int(bet)

        if balance < bet >= 0:
            print("Please enter a valid bet")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)
        balance += payout

        if balance == 0:
            print("No more bets")
            break


if __name__ == "__main__":
    main()