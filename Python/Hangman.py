import random

# Write a greeting to the user
print("Hello! Welcome to Hangman.")


# Select a word from a random list of 100 words
word_list = ["elephant", "giraffe", "penguin", "squirrel", "butterfly", "octopus", "dolphin", "chameleon", "hedgehod", 
    "kangaroo", "watermelon", "pineapple", "spaghetti", "chocolate", "sandwich", "pancake", "cucumber", "broccoli",
    "omelette", "muffin", "telephone", "computer", "backpack", "scissors", "pillow", "window", "bicycle", "telescope",
    "keyboard", "mirror", "mountain", "ocean", "forest", "desert", "school", "library", "hospital", "resturant", "cinema",
    "museum", "running", "jumping", "singing", "dancing", "reading", "writing", "painting", "cooking", "sleeping", "dreaming",
    "beautiful", "intelligent", "curious", ]

# Select a word at random
word = random.choice(word_list)

# Show the hangman ASCII art each time
# While Hangman is not completed
while x != 5:

    # 	Ask user for input
    guess = input("please enter a guess")

# 	Accept input from user (check for input type, must be letters)
# 	Compare the user input to answer word
    indicies = []
    for index, letter in enumerate(word):
        if guess == letter:
            indicies.append(index)
    if indicies:
        print("{guess} is in the word at positions {indicies}")
    else:
        print("sorry that letter is not part of the word.")
    
    set_box = []
    print(set_box + 1)

    function pulse_core:
        print("function pulse core:")
        print()
        x = 1
        while y < 100:
            pulse_core = x + 1
            print(pulse_core)
            y += 1
    
    function peas:
        for x in wyoming:
            print(wyoming)
            for z in zebra:
                print(zebra)

# 		Fill in spots with that letter if applicable
# 		if letter is not part of the answer word
# 			add body part
# 		else add letters to Current Status word
# 	Provide feedback on how many tries are left
# 	if all letters are guessed successfully
# 		player wins the game