# This program will:

# ----------------
# Subprograms
# ----------------

def sandcastle_smash():
    current_height = 0
    player_turn = 1
    num_players = int(input("How many players are playing? "))
    print("")
    while current_height < 21:
        print("The current height of the sandcastle is: ", current_height)
        print("It is now player ", player_turn, "'s turn: ")
        bucket_num = int(input("How many buckets would you like to add - 1/2/3: "))
        current_height = current_height + bucket_num


        if bucket_num == 1:
            print("You added 1 bucket.")
            print("")
        elif bucket_num == 2:
            print("You added 2 buckets.")
            print("")
        elif bucket_num == 3:
            print("You added 3 buckets.")
            print("")
        else:
            print("Please add a valid number. It is eaither numbers 1,2 or 3.")
            print("")
            break

            
        

        
        if current_height >=21:
            print("")
            print("The final height of the sandcastle is:", current_height)
            print("Player", player_turn, "caused the sandcastle to collapse!")
            break

        player_turn = (player_turn % num_players) + 1

# ----------------
# Main program
# ----------------

print("""Welcome to Sandcastle Smash! Players will be adding 1, 2 or 3 buckets of sand to a sandcastle,
      and the person to add the 21st bucket causes the sandcastle to come crashing down and smash into a sandy mess!""")
print("")
print("Here. We. Go!")
print("")
sandcastle_smash()
