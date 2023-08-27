import sys
import time
import keyboard 


def main():
# Run all program functions 
    textPrint(text)
    introScene()
    oaxacaBeach()
    gillnetRescue()
    tangedExit()
    swimWithFriends()


def textPrint(text):
# Format the text type effect on users screen
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print('')


# Constant with a list of options for user/ player 
keys = [
    "down",
    "up",
    "left",
    "right"
]

# Customise exception class for wrong key pressed
class wrongKey(KeyError):
    pass


def exit():

if __name__ == "__main__":
    # Print introductory text,
    # Ask user to input name 
    # Start introScene function
    print("Welcome to the Save the Sea Turtle Game!")
    print("Ahoy! As an endagered seaturtle, you are peacefully riding the Pacific Ocean. We are going to take you on a mini adventure, watch out for the Great White shark, and be aware of other terrors.")
    print("First, let's start with your name!")
    name = input("Please enter your name:")
    print(name + ", great. Now you have 4 directions to choose from.")
    print("Which way will you go next?")
    print("Options(Key) - Up, down, Left, Right")

def introScene():
    # Add options for directions the user/ player can choose from
    # Ask user to select key
    directions = ["down", "up", "left", "right"]
    print(name + ", great. Now you have 4 directions to choose from.")
    print("Which way will you go next?")
    userInput = ""
    while userInput not in directions:
            print("Options(Key) - Up/ Down/ Left/ Right")
            userInput = input()
            if userInput == "Up":
                gillnetRescue()
            elif userInput == "Down":
                tangedExit()
            elif userInput == "Left":
                oaxacaBeach()
            elif userInput == "Right":
                swimWithFriends()
            else:
                print("Please enter valid key option for the Save the Sea Turtle Game.")


def oaxacaBeach():
    # Present option for left "arriving at Oaxaca Beach"
    # Set function for vulturesLurk with options to select
    # Call functions for babiesSafe and fleeExit
    print("Wow mama! You have many eggs to lay, you've ended up swimming to Oaxaca Beach! Lets see if you can protect them all!")
    def vultureLurk():
        print("Watch out! Vultures are out to attact!")
        print(name + "Select your next option: Up or Right!")
        userInput = input()
            if userInput == "Up":
                fleeExit()
            elif userInput == "Right":
                babiesSafe()
            else:
                print("Please enter valid key option for the Save the Sea Turtle Game.")


def babiesSafe(exit):
    print("Phew! You dug a deep nest and all the babies are safe! You tried so hard in the heat and wading through the thick sand. Amazing, you have 100 baby turtle eggs protected!")
    exit()


def fleeExit(exit):
    print("Vultures visciously circled and you quickly fled back to the ocean! You're so lucky! You made it back to ride the tide and can try again tomorrow.")
    exit()


def gillnetRescue():
    # Present option for up "being caputred by gillnets"
    # Set function for rescueExit 
    # Call function for rescueExit 
    print("Oh no! Unfortunatley you have been accidentally captured by gillnets! Fishermen are so sorry and have called ocean rescue!")
        def rescueExit(exit):
            print("Yay! The rescue team are taking you to rehab, looks like your injuries will be fixed and you are going back to the open ocean!")
            exit()
        rescueExit()


def tangedExit(exit)
    # Present option for down "bad storms mean you're tangled"
    # Call function for Exit 
    print("Bad storms mean that fishermens nets are no longer drying on the beach and made it in to the water! Ooops, you got tangled. You are on your own in the deep ocean and nobody can help this time! :(")
            exit()


def swimWithFriends()
    def greatWhite()
        def sharkBait(exit)
            exit()
        def freedomExit(exit)
            exit()


#main() 