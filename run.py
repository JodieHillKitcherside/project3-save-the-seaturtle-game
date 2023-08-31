import sys
import time
from pyglet import key
import pyfiglet
from emojis import emoji
from general import (
    slowprint,
    escape,
    check_user_input
)


"""
Use pyfiglet module
"""
result = pyfiglet.figlet_format("Save the Sea Turtle", font="digital")
print(result)


"""
Declare emojis variable
"""
emoji_choice = emoji


def main():
    # Introduce main start screen
    introScene()


def exit():
    # Exit function exits the game
    slowprint(
        "GAME OVER" + name + emoji_choice.skull() +
        "Well done on getting that far. I'm sure you've worked out by now" +
        "that unfortunately sea turtles face many threats to their survival" +
        "and although some are natural - most are human threats." +
        emoji_choice.pirateflag() +
        "If you survived, you're made of strong stuff. It's estimated that" +
        "only 1 in 1000 sea turtles make it to adult turtle."
        + emoji_choice.seaturtle())
    sys.exit()


def oaxacaBeach():
    # Offer user right or down keys to continue game
    # Based on right, proceed to vultureLurk
    # Based on down, proceed to disoriented
    slowprint(
        "Wow mama! You have many eggs to lay, you've" +
        "ended up swimming"
        + emoji_choice.egg()
        + "to Oaxaca Beach! Lets see if you can protect"
        "them all!" + emoji_choice.mexico())
    userInput = input().lower()
    if userInput == key.LEFT:
        vultureLurk()
    elif userInput == key.DOWN:
        disoriented()
    else:
        print(KeyError + "Please enter a valid key option (LEFT or DOWN).")


def vultureLurk():
    # Offer user up or right keys to continue game
    # Based on up, proceed to fleeExit
    # Based on right, proceed to babiesSafe
    slowprint(
        "Watch out! Vultures are out to attack!" +
        emoji_choice.vulture()
        + name + ", select your next option: Up or Right!")
    userInput = input().lower()
    if userInput == key.UP:
        fleeExit()
    elif userInput == key.RIGHT:
        babiesSafe()
    else:
        print(KeyError + "Please enter a valid key option (UP or RIGHT).")
    vultureLurk()


def babiesSafe():
    # Exit game
    slowprint(
        "Phew! You dug a deep nest and all the babies are safe!" +
        emoji_choice.whiteheart()
        + "You tried so hard in the heat and wading through the thick sand."
        + emoji_choice.clapping()
        + "Amazing, you have 100 baby turtle eggs protected!" +
        emoji_choice.blowfish())
    exit()


def fleeExit():
    # Exit game
    slowprint(
        "Vultures viciously circled and you fled back to the ocean!"
        + emoji_choice.wave +
        "You're so lucky! You made it back to ride the tide!"
        + emoji_choice.lightblueheart
        + "You can try again tomorrow.")
    exit()


def disoriented():
    # Continue to beachPartExit
    slowprint(
        "You seem a bit disorientated! Humans like to surf here and"
        + emoji_choice.divingmask()
        + "this means the beach has changed so much since you were"
        + emoji_choice.compass()
        + "first here, 20 years ago. Will you find a quiet place"
        "to protect your eggs?")
    beachPartyExit()


def beachPartyExit():
    # Exit game
    slowprint(
        "Blast! The people are startling you."
        + "There is a beach party. There's nowhere to lay!")


def gillnetRescue():
    # Continue to rescueExit
    slowprint(
        "Oh! Unfortunately, you have been accidentally captured!"
        + emoji_choice.motorboat()
        + "You are stuck in gillnets and struggling to get out"
        + emoji_choice.buoy()
        + "means you have deep cuts on your flippers..."
        + "Fishermen are so sorry and have called ocean rescue!")
    rescueExit()


def rescueExit():
    # Exit game
    slowprint(
        "Yay! The rescue team are taking you to rehab, looks like your"
        + "injuries will be fixed and you are going back"
        + "to the open ocean!" + emoji_choice.squid())
    exit()


def tangledExit():
    # Exit game
    slowprint(
        "Bad storms mean that fishermen's nets are no longer drying"
        + "on the beach and made it into the water!"
        + emoji_choice.tropicalfish
        + "Oops, you got tangled. You are on your"
        "own in the deep ocean and nobody can help this time! :(")
    exit()


def swimWithFriends():
    # Offer user up or left keys to continue game
    # Based on up, proceed to greatWhite
    # Based on left, proceed to oilSpill
    slowprint(
        "Looks like you've found some friends! you are swimming around"
        + emoji_choice.jellyfish()
        + "kelp, little fishes and terrible claw lobsters."
        + emoji_choice.lobster()
        + "Woah!There is lots of food here!"
        + emoji_choice.crab()
        + "Which way will you go?"
        "Enter your option: Up or Left")
    userInput = input().lower()
    if userInput == key.UP:
        greatWhite()
    elif userInput == key.LEFT:
        oilSpill()
    else:
        print(KeyError + "Please enter a valid key option (UP or LEFT).")


def greatWhite():
    # Offer user up or left keys to continue game
    # Based on up, proceed to sharkBaitExit
    # Based on left, proceed to balloonExit
    slowprint(
        "Can you hide from the great white shark? He's spotted you!"
        + emoji_choice.shark()
        + name
        + ", select your next option: Up or Left!")
    userInput = input().lower()
    if userInput == key.UP:
        sharkBaitExit()
    elif userInput == key.LEFT:
        balloonExit()
    else:
        print(KeyError + "Please enter a valid key option (UP or LEFT).")


def sharkBaitExit():
    # Exit game
    slowprint(
        "He got you! You tried to get away but he's too fast."
        + "You're dead.")
    exit()


def balloonExit():
    # Exit game
    slowprint(
        "You swam up and out of sight!"
        + emoji_choice.shell()
        + "But oops! You accidentally swallowed a balloon"
        + "You thought it was a jellyfish! Unlucky..."
        + emoji_choice.jellyfish()
        + "Let's hope that get's recycled out of your body"
        + "or it will be fatal..")
    exit()


def oilSpill():
    # Continue to vesselStrikeExit
    slowprint(
        "There's been an oil spill affecting your favourite"
        + emoji_choice.biohazard()
        + "corals! You are going to have to rest by the"
        + emoji_choice.reef()
        + "mangroves instead. Take a five minute rest and get"
        + "back to swimming.")
    vesselStrikeExit()


def vesselStrikeExit():
    # Exit game
    slowprint(
        "Poor you! A boat came to watch sealions near by your"
        + "new favourite spot! the boat It's colided with a pod"
        + "of seals. You haven't been able to reach the surface this time!"
        + emoji_choice.seal())
    exit()


def introScene():
    # Make name recognised as global
    global name
    name = input("Please enter your name: ")
    slowprint(
        name + ", great. Now you have 4 directions to choose from."
        + "Which way will you go next?")
    userInput = input().lower()

    # Based on option user selects, proceed to correct destination function
    slowprint(
        name + ", your options are on your keyboard."
        + "Throughout this adventure, all you need to tap is:"
        + "Up, Down, Left or Right"
        + "And if you would like to escape anytime - hit escape!")
    userInput = input().lower()
    if userInput == key.UP:
        gillnetRescue()
    elif userInput == key.DOWN:
        tangledExit()
    elif userInput == key.LEFT:
        oaxacaBeach()
    elif userInput == key.RIGHT:
        swimWithFriends()
    else:
        print(
            KeyError + "Please enter a valid key option"
            + "(UP/DOWN/LEFT/RIGHT)")


if __name__ == "__main__":
    slowprint(
        "Welcome to the Save the Sea Turtle Game!"
        # ... [introductory text]
        + "Ahoy! As an endangered sea turtle, you are peacefully riding"
        + emoji_choice.whale()
        + "the Pacific Ocean. We are going to take you on an adventure!"
        + emoji_choice.dolphin()
        + "Watch out for the Great White Shark and other great terrors."
        + emoji_choice.okay())
    main()
