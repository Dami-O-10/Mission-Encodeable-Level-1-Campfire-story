# This program will:

# ----------------
# Subprograms
# ----------------

def generate_story(weather, snack, adjective1, building, tool, mythical_creature, adjective2, plural_noun, noise, verb):
    story = "It was a " + weather + " evening, and we were gathered around the campfire, munching on " + snack + ". "
    story += "Suddenly, we heard a " + adjective1 + " sound coming from the old " + building + " nearby. "
    story += "With a " + tool + " in hand, we cautiously approached. "
    story += "Inside, we found a " + mythical_creature + " guarding a " + adjective2 + " chest filled with " + plural_noun + ". "
    story += "The " + mythical_creature + " gnashed its teeth and " + noise + ", "
    story += "but instead of running away, we offered the " + mythical_creature + " some " + snack + ". "
    story += "For a moment, we thought it was going to " + verb + ", but instead, it snatched the rest of the " + snack + " and disappeared, "
    story += "leaving us with the treasure chest."
    
    return story

# ----------------
# Main program
# ----------------

print("Welcome to the Magical Story Generator!")
print("Please answer the following questions to help create your adventure.\n")

weather = input("Enter a type of weather (e.g. stormy, sunny): ")
snack = input("Enter a snack: ")
adjective1 = input("Enter an adjective: ")
building = input("Enter a type of building: ")
tool = input("Enter a tool: ")
mythical_creature = input("Enter a mythical creature: ")
adjective2 = input("Enter another adjective: ")
plural_noun = input("Enter a plural noun: ")
noise = input("Enter a type of noise: ")
verb = input("Enter a verb: ")

story = generate_story(weather, snack, adjective1, building, tool, mythical_creature, adjective2, plural_noun, noise, verb)

print("Here is your story:")
print(story)
