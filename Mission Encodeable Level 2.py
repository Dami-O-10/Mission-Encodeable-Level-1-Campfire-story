# This program will:
# ----------------
# Subprograms
# ----------------

def ask_questions():
    octopus = 0
    dolphin = 0
    turtle = 0
    fish = 0

    print("")

    ask1 = input("""Are you more active in the day,
    the night,
    or does it vary? Enter day/night/varied: """)

    if ask1 == "day":
        octopus += 1
        dolphin += 1
        turtle += 1
        fish += 1
    elif ask1 == "night":
        octopus += 1
        dolphin += 1
        turtle += 1
        fish += 1
    elif ask1 == "varied":
        octopus += 1
        dolphin += 1
        turtle += 1
        fish += 1

    print("")

    ask2 = input("""Do you prefer to stay in one place,
                 or are you more adventurous? Enter stay/explore: """)
    if ask2 == "explore":
        octopus += 1
        dolphin += 1
        fish += 1
    elif ask2 == "stay":
        turtle += 1

    print("")

    ask3 = input("""Do you have a big group of friends,
                 a small group of friends,
                 or do you prefer to be alone? Enter big/small/alone: """)
    if ask3 == "big":
        fish += 1
        dolphin += 1
    elif ask3 == "small":
        turtle += 1
    elif ask3 == "alone":
        octopus += 1

    return octopus, dolphin, turtle, fish



def find_highest_match(octopus, dolphin, turtle, fish):
    highest = max(octopus, dolphin, turtle, fish)

    if octopus == highest:
        return "You are most like an octopus!"
    elif dolphin == highest:
        return "You are most like a dolphin!"
    elif turtle == highest:
        return "You are most like a turtle!"
    elif fish == highest:
        return "You are most like a fish!"



    
# ----------------
# Main program
# ----------------

print("""This program will give you a quiz to decide what
      animal you would be if you were a sea creature!""")
print("")
print("Let's get started!")
print("")

octopus, dolphin, turtle, fish = ask_questions()

result = find_highest_match(octopus, dolphin, turtle, fish)
print(result)
