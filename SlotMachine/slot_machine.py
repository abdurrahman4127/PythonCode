# to import module
import random

# define constant
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

# deposit mula
def deposit():
    while True:
        amount = input("what would you like to deposit? $")
        
        # check if it's some digit or shit
        if amount.isdigit():
            amount = int(amount) # convert to int

            if amount > 0:
                break
            else:
                print("amount must be greater than 0")
        
        else:
            print("please enter a number")
    
    return amount


# number of line
def get_number_of_line():
    while True:
        lines = input("enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")

        if lines.isdigit():
            lines = int(lines)

            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter a valid number of lines")
        
        else:
            print("please enter a number")
    
    return lines


# make bet
def get_bet():
    while True:
        amount = input("how much would you like to bet on each line? $")

        if amount.isdigit():
            amount = int(amount)

            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET} - ${MAX_BET}")
        
        else:
            print("please enter a number")
    
    return amount


# winnnings checking
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    
    for line in range(lines):
        symbol = columns[0][line]

        for column in columns:
            symbol_to_check = column[line]

            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


# to make a dictionary
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)


    columns = []
    for _ in range(cols):
        column = []
        
        #to copy
        current_symbols = all_symbols[:]  

        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns


# printing the slot machine
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ") # line ends with |
            else:
                print(column[row], end="")

        print() # new line


def spin(balance):
    lines = get_number_of_line()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"you don't have enough to bet that amount; your current balance is ${balance}")
        else:
            break
 
    print(f"you're betting ${bet} on ${lines}. total bet is equal to: ${total_bet}")
   

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}")
    print(f"you won on line:", * winning_lines)

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"current balance is: ${balance}")
        ans = input("press enter to spin (q to quit)")

        if ans == "q":
            break 
        balance += spin(balance)
    
    print(f"you left with ${balance}")


main()