import random

def is_valid_player(text):
    if text == "x" or text == "o":
        return True
    else:
        return False

def is_valid_choice(grid, choice):
    if grid[choice-1] == " ":
        return True
    else:
        return False

def show_tip():
    print("")
    print("[ 1 | 2 | 3 ]")
    print("[ 4 | 5 | 6 ]")
    print("[ 7 | 8 | 9 ]")
    print("")
    print("Pick an empty cell that corresponds with the same cell as shown in the grid above.")

def player_turn(grid):
    choice = None
    valid_choice = False
    while not valid_choice:
        show_tip()
        show_grid(grid)
        choice = int(input("Which cell do you choose? (Enter the corresponding number.) "))
        valid_choice = is_valid_choice(grid, choice)
    grid[choice-1] = player
    show_grid(grid)


def computer_turn(grid):
    choice = None
    valid_choice = False
    while not valid_choice:
        choice = random.randint(1, 9)
        valid_choice = is_valid_choice(grid, choice)
    grid[choice-1] = computer

def calculate_cat(grid):
    if " " not in grid:
        return "cat"
    else:
        return None

def calculate_winner(grid):
    choices = ("x", "o")
    possibilities = (
        (grid[0], grid[1], grid[2]),
        (grid[0], grid[3], grid[6]),
        (grid[0], grid[4], grid[8]),
        (grid[1], grid[4], grid[7]),
        (grid[2], grid[4], grid[6]),
        (grid[2], grid[5], grid[8]),
        (grid[3], grid[4], grid[5]),
        (grid[6], grid[7], grid[8]),
    )
    for choice in choices:
        for possibility in possibilities:
            if all(item == choice for item in possibility):
                return choice
    else:
        return None

def show_grid(grid):
    print("")
    print(f"[ {grid[0]} | {grid[1]} | {grid[2]} ]")
    print(f"[ {grid[3]} | {grid[4]} | {grid[5]} ]")
    print(f"[ {grid[6]} | {grid[7]} | {grid[8]} ]")
    print("")

winner = None

grid = [" "," "," "," "," "," "," "," "," "]

print("Welcome to Tic-Tac-Toe")

valid_player = False

while (not valid_player):
    player = input("Do you want to be x or o? ").lower()
    print("")
    valid_player = is_valid_player(player)

print(f"You are player: {player}")

if (player == "x"):
    computer = "o"
    switch_turn = False
else:
    computer = "x"
    switch_turn = True

print(f"The computer is: {computer}")

while (not winner):

    if not switch_turn:
        player_turn(grid)
    else:
        computer_turn(grid)

    if calculate_winner(grid):
        winner = calculate_winner(grid)
    elif calculate_cat(grid):
        winner = calculate_cat(grid)
    else:
        winner = None

    switch_turn = not switch_turn

if winner == player:
    show_grid(grid)
    print("Congratulations, you've won.")
else:
    print("Sorry, try again.")
