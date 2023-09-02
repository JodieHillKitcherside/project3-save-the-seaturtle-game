from statements import (
    beachPartyExitPrint,
    fleeExitPrint,
    rescueExitPrint,
    tangledExitPrint,
    sharkBaitExitPrint,
    balloonExitPrint,
    vesselStrikeExitPrint,
    babiesSafePrint
)
import sys
import time
import keyboard
import pyfiglet
from emojis import Emoji


def slowprint(all_strings):
    # Styling all strings with a delayed type time
    for each_character in all_strings:
        sys.stdout.write(each_character)
        sys.stdout.flush()
        time.sleep(1/17)


def check_user_input(input_str):
    # Validates all user input
    # Prints prompt if blank
    if user_input == "":
        print("Please enter your input")
    else:
        None


# Use pyfiglet module
result = pyfiglet.figlet_format("Save the Sea Turtle", font="digital")
print(result)


# Rename Emoji class
emoji_choice = Emoji()


def main():
    # Introduce main start screen
    introScene()


def exit():
    # Exit function exits the game
    slowprint(
        " GAME OVER " + name + emoji_choice.skull +
        "Well done on getting that far. I'm sure you've worked out by now" +
        " that unfortunately sea turtles face many threats to their survival" +
        " and although some are natural - most are human threats." +
        " If you survived, you're made of strong stuff. It's estimated that" +
        " only 1 in 1000 sea turtles make it to adult turtle."
        + emoji_choice.pirateflag + emoji_choice.seaturtle)
    sys.exit()


def slowPrintExit(all_strings):
    # Reusable function to exit game
    # Links to print_statements
    slowprint(all_strings)
    exit()


def oaxacaBeach():
    # Offer user right or down keys to continue game
    # Based on right, proceed to vultureLurk
    # Based on down, proceed to disoriented
    slowprint(
        "Wow mama! You have many eggs to lay, you've" +
        "ended up swimming to Oaxaca Beach!" 
        " Lets see if you can protect them all!" 
        + emoji_choice.mexico + emoji_choice.egg
        + " Select your next option:"
        + " Choose either 'l'" + emoji_choice.e_left
        + " or choose 'd'" + emoji_choice.e_down)
    while True:
        oaxaca_input = input("Please choose your option:\n")
        oaxaca_answer = oaxaca_input.strip().lower()
        if oaxaca_input == "l":
            vultureLurk()
        elif oaxaca_input == "d":
            disoriented()
        else:
            print(KeyError + "Please enter a valid key option.")
    return oaxaca_answer


def vultureLurk():
    # Offer user up or right keys to continue game
    # Based on up, proceed to fleeExit
    # Based on right, proceed to babiesSafe
    slowprint(
        "Watch out! Vultures are out to attack!" 
        + emoji_choice.vulture
        + name + ", select your next option:"
        + " Choose either 'u'" + emoji_choice.e_up
        + " or choose 'r'" + emoji_choice.e_right)
    while True:
        vulture_input = input("Please choose your option:\n")
        vulture_answer = vulture_input.strip().lower()
        if value_input == "u":
            fleeExit()
        elif value_input == "r":
            babiesSafe()
        else:
            print(KeyError + "Please enter a valid key option.")
        vultureLurk()
    return vulture_answer


def babiesSafe():
    # Exit game
    slowPrintExit(babiesSafePrint)


def fleeExit():
    # Exit game
    slowPrintExit(fleeExitPrint)


def disoriented():
    # Continue to beachPartExit
    slowprint(
        "You seem a bit disorientated! Humans like to surf here and"
        + " this means the beach has changed so much since you were"
        + " first here, 20 years ago. Will you find a quiet place"
        + " to protect your eggs?")
        + emoji_choice.divingmask + emoji_choice.compass
    beachPartyExit()


def beachPartyExit():
    # Exit game
    slowPrintExit(beachPartyExit)


def gillnetRescue():
    # Continue to rescueExit
    slowprint(
        "Oh! Unfortunately, you have been accidentally captured!"
        + "You are stuck in gillnets and struggling to get out"
        + "means you have deep cuts on your flippers..."
        + "Fishermen are so sorry and have called ocean rescue!")
        + emoji_choice.motorboat + emoji_choice.buoy
    rescueExit()


def rescueExit():
    # Exit game
    slowPrintExit(rescueExitPrint)


def tangledExit():
    # Exit game
    slowPrintExit(tangledExitPrint)


def swimWithFriends():
    # Offer user up or left keys to continue game
    # Based on up, proceed to greatWhite
    # Based on left, proceed to oilSpill
    slowprint(
        "Looks like you've found some friends! you are swimming around"
        + " kelp, little fishes and terrible claw lobsters."
        + " Woah!There is lots of food here!"
        + emoji_choice.crab + emoji_choice.jellyfish
        + emoji_choice.lobster
        + " Which way will you go?"
        + " Enter your option: 'u'" + emoji_choice.e_up
        + " or 'l'" + emoji_choice.e_left)
    while True:
        swim_input = input("Please choose your option:\n")
        swim_answer = swim_input.strip().lower()
        if value_input == "u":
            greatWhite()
        elif value_input == "l":
            oilSpill()
        else:
            print(KeyError + "Please enter a valid key option.")
    return swim_answer


def greatWhite():
    # Offer user up or left keys to continue game
    # Based on up, proceed to sharkBaitExit
    # Based on left, proceed to balloonExit
    slowprint(
        "Can you hide from the great white shark? He's spotted you!"
        + emoji_choice.shark
        + name
        + ", select your next option: 'u'" + emoji_choice.e_up
        + " or 'l'" + emoji_choice.e_left)
    Wwhile True:
        shark_input = input("Please choose your option:\n")
        shark_answer = shark_input.strip().lower()
        if value_input == "u":
            sharkBaitExit()
        elif value_input == "l":
            balloonExit()
        else:
            print(KeyError + "Please enter a valid key option.")
    return shark_answer


def sharkBaitExit():
    # Exit game
    slowPrintExit(sharkBaitExitPrint)


def balloonExit():
    # Exit game
    slowPrintExit(balloonExitPrint)


def oilSpill():
    # Continue to vesselStrikeExit
    slowprint(
        "There's been an oil spill affecting your favourite"
        + "corals! You are going to have to rest by the"
        + "mangroves instead. Take a five minute rest and get"
        + "back to swimming."
        + emoji_choice.biohazard)

    vesselStrikeExit()


def vesselStrikeExit():
    # Exit game
    slowPrintExit(vesselStrikeExitPrint)


def introScene():
    # Make name recognised as global
    global name
    name = input("Please enter your name: \n")
    slowprint(
        name + ", great. Now you have 4 directions to choose from."
        + " Your options are on your keyboard."
        + " Throughout this adventure, all you need to tap is:"
        + " 'u' button for Up, 'd' button for Down, 'l' button for Left"
        + " or 'r' button for Right - then hit Enter"
        + emoji_choice.e_up 
        + " Which way will you go next?")
    while True: 
        intro_input = input("Please choose your option:\n")
        intro_answer = intro_input.strip().lower()
        if value_input == "u":
            gillnetRescue()
        elif value_input == "d":
            tangledExit()
        elif value_input == "u":
            oaxacaBeach()
        elif value_input == "l":
            swimWithFriends()
        else:
            print(
                KeyError + "Please enter a valid key option"
                + "(lowercase only - u/d/l/r)")
    return intro_answer


if __name__ == "__main__":
    slowprint(
        "Welcome to the Save the Sea Turtle Game!"
        # ... [introductory text]
        + " Ahoy! As an endangered sea turtle, you are peacefully riding"
        + "the Pacific Ocean. We are going to take you on an adventure!"
        + "Watch out for the Great White Shark and other great terrors."
        + emoji_choice.whale + emoji_choice.dolphin + emoji_choice.okay) 
    main()
