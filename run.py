import sys
import time
import keyboard


def main():
    introScene()


def exit():
    print("Well done on getting that far. I'm sure you've worked out by now")
    print("that unfortunately sea turtles face many threats to their survival")
    print("and although some are natural - most are human threats.")
    print("If you survived, you're made of strong stuff. It's estimated that")
    print("only 1 in 1000 sea turtles make it to adult turtle.")
    sys.exit()


def oaxacaBeach():
    print("Wow mama! You have many eggs to lay, you've ended up swimming")
    print("to Oaxaca Beach! Lets see if you can protect them all!")
    vultureLurk()


def vultureLurk():
    print("Watch out! Vultures are out to attack!")
    print(name + ", select your next option: Up or Right!")
    userInput = input().lower()
    if userInput == keyboard.KP_UP:
        fleeExit()
    elif userInput == keyboard.KP_RIGHT:
        babiesSafe()
    else:
        print("Please enter a valid option.")
        vultureLurk()


def babiesSafe():
    print("Phew! You dug a deep nest and all the babies are safe!")
    print("You tried so hard in the heat and wading through the thick sand.")
    print("Amazing, you have 100 baby turtle eggs protected!")
    exit()


def fleeExit():
    print("Vultures viciously circled and you fled back to the ocean!")
    print("You're so lucky! You made it back to ride the tide!")
    print("You can try again tomorrow.")
    exit()


def gillnetRescue():
    print("Oh! Unfortunately, you have been accidentally captured!")
    print("You are stuck in gillnets and struggling to get out")
    print("means you have deep cuts on your flippers...")
    print("Fishermen are so sorry and have called ocean rescue!")
    rescueExit()


def rescueExit():
    print("Yay! The rescue team are taking you to rehab, looks like your")
    print("injuries will be fixed and you are going back")
    print("to the open ocean!")
    exit()


def tangledExit():
    print("Bad storms mean that fishermen's nets are no longer drying")
    print("on the beach and made it into the water!")
    print("Oops, you got tangled. You are on your")
    print("own in the deep ocean and nobody can help this time! :(")
    exit()


def swimWithFriends():
    greatWhite()


def greatWhite():
    print("Can you hide from the great white shark? He's spotted you!")
    print(name + ", select your next option: Up or Left!")
    userInput = input().lower()
    if userInput == "KP_UP":
        sharkBaitExit()
    elif userInput == "KP_LEFT":
        freedomExit()
    else:
        print("Please enter a valid option.")
        greatWhite()


def sharkBaitExit():
    print("He got you! You tried to get away but he's too fast.")
    print("You're dead.")
    exit()


def freedomExit():
    print("You swam up and out of sight! You are free.")
    exit()


def introScene():
    global name
    name = input("Please enter your name: ")
    print(name + ", great. Now you have 4 directions to choose from.")
    print("Which way will you go next?")
    userInput = input().lower()
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
