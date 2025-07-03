# Summer project: Sun, Sand, Sea
# This program will:

# ----------------
# Import libraries
# ----------------
import random
# ----------------
# Subprograms
# ----------------

def get_player_choice():
    userAsk = input("Which one will you pick: Sun    Sand    Sea? ")
    while userAsk not in ["Sun", "Sand", "Sea"]:
        userAsk = input("Please type in a valid choice: Sun    Sand   Sea ")
    return userAsk

def get_computer_choice():
    game_choices = ["Sun", "Sand", "Sea"]
    selected = random.choice(game_choices)
    return selected

def who_won(get_player_choice, get_computer_choice):
    if get_player_choice == get_computer_choice:
        return "It's a tie!"
    elif (get_player_choice == "Sun" and get_computer_choice == "Sea") or \
         (get_player_choice == "Sea" and get_computer_choice == "Sand") or \
         (get_player_choice == "Sand" and get_computer_choice == "Sun"):
        return "You win!"
    else:
        return "Computer wins!"
    

def play_game():
    player = get_player_choice()
    computer = get_computer_choice()
    result = who_won(player, computer)

    print("You chose:", player)
    print("Computer chose:", computer)
    print(result)
    
    
# ----------------
# Main program
# ----------------

print("""Welcome to Sun Sand and Sea! The game is like rock paper scissors ( but better ;) ). Here are the rules:
Sun wins against sea
Sand wins against sun
Sea wins against sand
If the player and the computer choose the same item, it's a draw""")
print("")
print("Here. We. Go!")
print("")

play_game()
