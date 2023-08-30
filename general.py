import sys
import time
from pynput import keyboard


def slowprint(all_strings):
    # Styling all strings
    for each_character in all_strings + "\n":
        sys.stdout.write(each_character)
        sys.stdout.flush()
        time.sleep(1/17)


def escape():
    # Implementing a hotkey
    if input == keyboard.Key.escape:
        exit()


def check_user_input(input_str):
    # Validates all user input
    # Prints prompt if blank
    if input == "":
        print("Please enter your input")
    else:
        None
