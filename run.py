import sys
import time
import keyboard
import pyfiglet

# Use pyfiglet module 
result = pyfiglet.figlet_format("Save the Sea Turtle", font="digital")
print(result)


def main():
    introScene()


def exit():
    # Exit function exits the game
    print("GAME OVER" + name)
    print("Well done on getting that far. I'm sure you've worked out by now")
    print("that unfortunately sea turtles face many threats to their survival")
    print("and although some are natural - most are human threats.")
    print("If you survived, you're made of strong stuff. It's estimated that")
    print("only 1 in 1000 sea turtles make it to adult turtle.")
    sys.exit()


def oaxacaBeach():
    # Offer user right or down keys to continue game 
    # Based on right, proceed to vultureLurk 
    # Based on down, proceed to disoriented
    print("Wow mama! You have many eggs to lay, you've ended up swimming")
    print("to Oaxaca Beach! Lets see if you can protect them all!")
    userInput = input().lower()
    if userInput == keyboard.KP_RIGHT:
        vultureLurk()
    elif userInput == keyboard.KP_DOWN:
        disoriented()
    else:
        raise KeyError
        print("Please enter a valid key option.")


def vultureLurk():
    # Offer user up or right keys to continue game
    # Based on up, proceed to fleeExit
    # Based on right, proceed to babiesSafe
    print("Watch out! Vultures are out to attack!")
    print(name + ", select your next option: Up or Right!")
    userInput = input().lower()
    if userInput == keyboard.KP_UP:
        fleeExit()
    elif userInput == keyboard.KP_RIGHT:
        babiesSafe()
    else:
        raise KeyError
        print("Please enter a valid key option.")
        vultureLurk()


def babiesSafe():
    # Exit game
    print("Phew! You dug a deep nest and all the babies are safe!")
    print("You tried so hard in the heat and wading through the thick sand.")
    print("Amazing, you have 100 baby turtle eggs protected!")
    exit()


def fleeExit():
    # Exit game 
    print("Vultures viciously circled and you fled back to the ocean!")
    print("You're so lucky! You made it back to ride the tide!")
    print("You can try again tomorrow.")
    exit()


def disoriented():
    # Continue to beachPartExit
    print("You seem a bit disorientated! Humans like to surf here and")
    print("this means the beach has changed so much since you were")  
    print("first here, 20 years ago. Will you find a quiet place") 
    print("to protect your eggs?")
    beachPartyExit()


def beachPartyExit():
    # Exit game 
    print("Blast! The people are startling you.")
    print("There is a beach party. There's nowhere to lay!")


def gillnetRescue():
    # Continue to rescueExit
    print("Oh! Unfortunately, you have been accidentally captured!")
    print("You are stuck in gillnets and struggling to get out")
    print("means you have deep cuts on your flippers...")
    print("Fishermen are so sorry and have called ocean rescue!")
    rescueExit()


def rescueExit():
    # Exit game 
    print("Yay! The rescue team are taking you to rehab, looks like your")
    print("injuries will be fixed and you are going back")
    print("to the open ocean!")
    exit()


def tangledExit():
    # Exit game 
    print("Bad storms mean that fishermen's nets are no longer drying")
    print("on the beach and made it into the water!")
    print("Oops, you got tangled. You are on your")
    print("own in the deep ocean and nobody can help this time! :(")
    exit()


def swimWithFriends():
    # Offer user up or left keys to continue game
    # Based on up, proceed to greatWhite
    # Based on left, proceed to oilSpill
    print("Looks like you've found some friends! you are swimming around")
    print("kelp, little fishes and terrible claw lobsters.") 
    print("Woah!There is lots of food here!")
    print("Which way will you go?")
    print("Enter your option: Up or Left")
    userInput = input().lower()
    if userInput == "KP_UP":
        greatWhite()
    elif userInput == "KP_LEFT":
        oilSpill()
    else:
        raise KeyError
        print("Please enter a valid key option.")


def greatWhite():
    # Offer user up or left keys to continue game
    # Based on up, proceed to sharkBaitExit
    # Based on left, proceed to balloonExit
    print("Can you hide from the great white shark? He's spotted you!")
    print(name + ", select your next option: Up or Left!")
    userInput = input().lower()
    if userInput == "KP_UP":
        sharkBaitExit()
    elif userInput == "KP_LEFT":
        balloonExit()
    else:
        raise KeyError
        print("Please enter a valid key option.")


def sharkBaitExit():
    # Exit game
    print("He got you! You tried to get away but he's too fast.")
    print("You're dead.")
    exit()


def balloonExit():
    # Exit game
    print("You swam up and out of sight!")
    print("But oops! You accidentally swallowed a balloon")
    print("You thought it was a jellyfish! Unlucky...")
    print("Let's hope that get's recycled out of your body")
    print("or it will be fatal..")
    exit()

def oilSpill():
    # Continue to vesselStrikeExit
    print("There's been an oil spill affecting your favourite")
    print("corals! You are going to have to rest by the") 
    print("mangroves instead. Take a five minute rest and get")
    print("back to swimming.")
    vesselStrikeExit()

def vesselStrikeExit():
    # Exit game 
    print("Poor you! A boat came to watch sealions near by your")
    print("new favourite spot! the boat It's colided with a pod")
    print("of seals. You haven't been able to reach the surface this time!")
    exit()

def introScene():
    # Make name recognised as global 
    global name
    name = input("Please enter your name: ")
    print(name + ", great. Now you have 4 directions to choose from.")
    print("Which way will you go next?")
    userInput = input().lower()

    # Based on option user selects, proceed to correct destination function
    directions = ["KP_UP", "KP_DOWN", "KP_Right", "KP_LEFT"]
    while userInput not in directions:
        print(name + ", your options are: Up, Down, Left, Right")
        userInput = input().lower()
        if userInput == "KP_UP":
            gillnetRescue()
        elif userInput == "KP_DOWN":
            tangledExit()
        elif userInput == "KP_LEFT":
            oaxacaBeach()
        elif userInput == "KP_RIGHT":
            swimWithFriends()


if __name__ == "__main__":
    print("Welcome to the Save the Sea Turtle Game!")
    # ... [introductory text]
    print("Ahoy! As an endangered sea turtle, you are peacefully riding")
    print("the Pacific Ocean. We are going to take you on an adventure!")
    print("Watch out for the Great White Shark and other great terrors.")
    main()
