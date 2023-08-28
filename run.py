# Import modules 
import sys
import time
import keyboard
import pyfiglet
from emojis import emoji
from general import slowprint

# Use pyfiglet module 
result = pyfiglet.figlet_format("Save the Sea Turtle", font="digital")
print(result)

# Declare emojis variable
emoji_choice = emoji()

def main():
    # Introduce main start screen
    introScene()


def exit():
    # Exit function exits the game
    slowprint("GAME OVER" + name +
        emoji_choice.skull()
    "Well done on getting that far. I'm sure you've worked out by now"
    "that unfortunately sea turtles face many threats to their survival"
    "and although some are natural - most are human threats." +
    emoji_choice.pirateflag()
    "If you survived, you're made of strong stuff. It's estimated that"
    "only 1 in 1000 sea turtles make it to adult turtle." + emoji_choice.seaturtle())
    sys.exit()


def oaxacaBeach():
    # Offer user right or down keys to continue game 
    # Based on right, proceed to vultureLurk 
    # Based on down, proceed to disoriented
    slowprint("Wow mama! You have many eggs to lay, you've ended up swimming"
    + emoji_choice.egg()
    "to Oaxaca Beach! Lets see if you can protect them all!"
    +emoji_choice.mexico())
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
    slowprint("Watch out! Vultures are out to attack!" +
    emoji_choice.vulture()
    + name + ", select your next option: Up or Right!")
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
    slowprint("Phew! You dug a deep nest and all the babies are safe!" +
    emoji_choice.whiteheart
    You tried so hard in the heat and wading through the thick sand."
    + emoji_choice.clapping()
    "Amazing, you have 100 baby turtle eggs protected!" +
    emoji_choice.blowfish())
    exit()


def fleeExit():
    # Exit game 
    slowprint("Vultures viciously circled and you fled back to the ocean!"
    + emoji_choice.wave 
    + "You're so lucky! You made it back to ride the tide!"
    + emoji_choice.lightblueheart
    + "You can try again tomorrow.")
    exit()


def disoriented():
    # Continue to beachPartExit
    slowprint("You seem a bit disorientated! Humans like to surf here and"
    + emoji_choice.divingmask()
    + "this means the beach has changed so much since you were"
    + emoji_choice.compass()
    + "first here, 20 years ago. Will you find a quiet place"
    "to protect your eggs?")
    beachPartyExit()


def beachPartyExit():
    # Exit game 
    slowprint("Blast! The people are startling you."
    "There is a beach party. There's nowhere to lay!")


def gillnetRescue():
    # Continue to rescueExit
    slowprint("Oh! Unfortunately, you have been accidentally captured!"
    + emoji_choice.motorboat()
    + "You are stuck in gillnets and struggling to get out"
    + emoji_choice_buoy()
    + "means you have deep cuts on your flippers..."
    "Fishermen are so sorry and have called ocean rescue!")
    rescueExit()


def rescueExit():
    # Exit game 
    slowprint("Yay! The rescue team are taking you to rehab, looks like your"
    "injuries will be fixed and you are going back"
    "to the open ocean!" + emoji_choice.squid())
    exit()


def tangledExit():
    # Exit game 
    slowprint("Bad storms mean that fishermen's nets are no longer drying"
    "on the beach and made it into the water!" 
    + emoji_choice.tropicalfish
    + "Oops, you got tangled. You are on your"
    "own in the deep ocean and nobody can help this time! :(")
    exit()


def swimWithFriends():
    # Offer user up or left keys to continue game
    # Based on up, proceed to greatWhite
    # Based on left, proceed to oilSpill
    slowprint("Looks like you've found some friends! you are swimming around"
    + emoji_choice.jellyfish()
    + "kelp, little fishes and terrible claw lobsters."
    + emoji_choice.lobster()
    + "Woah!There is lots of food here!"
    + emoji_choice.crab()
    + "Which way will you go?"
    "Enter your option: Up or Left")
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
    slowprint("Can you hide from the great white shark? He's spotted you!"
    + emoji_choice.shark()
    + name + ", select your next option: Up or Left!")
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
    slowprint("He got you! You tried to get away but he's too fast."
    "You're dead.")
    exit()


def balloonExit():
    # Exit game
    slowprint("You swam up and out of sight!"
    + emoji_choice.shell()
    + "But oops! You accidentally swallowed a balloon"
    "You thought it was a jellyfish! Unlucky..."
    + emoji_choice.jellyfish()
    + "Let's hope that get's recycled out of your body"
    + "or it will be fatal..")
    exit()

def oilSpill():
    # Continue to vesselStrikeExit
    slowprint("There's been an oil spill affecting your favourite"
    + emoji_choice.biohazard()
    + "corals! You are going to have to rest by the"
    + emoji_choice.reef()
    + "mangroves instead. Take a five minute rest and get"
    + "back to swimming.")
    vesselStrikeExit()

def vesselStrikeExit():
    # Exit game 
    slowprint("Poor you! A boat came to watch sealions near by your"
    + "new favourite spot! the boat It's colided with a pod"
    + "of seals. You haven't been able to reach the surface this time!"
    + emoji_choice.seal())
    exit()

def introScene():
    # Make name recognised as global 
    global name
    name = input("Please enter your name: ")
    slowprint(name + ", great. Now you have 4 directions to choose from."
    +"Which way will you go next?")
    userInput = input().lower()

    # Based on option user selects, proceed to correct destination function
    directions = ["KP_UP", "KP_DOWN", "KP_Right", "KP_LEFT"]
    while userInput not in directions:
        slowprint(name + ", your options are: Up, Down, Left, Right")
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
    slowprint("Welcome to the Save the Sea Turtle Game!"
    # ... [introductory text]
    + "Ahoy! As an endangered sea turtle, you are peacefully riding"
    + emoji_choice.whale()
    + "the Pacific Ocean. We are going to take you on an adventure!"
    + emoji_choice.dolphin()
    + "Watch out for the Great White Shark and other great terrors."
    + emoji_choice.okay())
    main()
