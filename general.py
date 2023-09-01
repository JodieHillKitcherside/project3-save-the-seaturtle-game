import sys
import time
import pygame
from pygame.locals import *
from run import main


pygame.init()


def slowprint(all_strings):
    # Styling all strings
    for each_character in all_strings + "\n":
        sys.stdout.write(each_character)
        sys.stdout.flush()
        time.sleep(1/17)


def escape():
    # Implementing a hotkey
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return main()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                main()


def check_user_input(input_str):
    # Validates all user input
    # Prints prompt if blank
    for event in pygame.event.get():
        if event.type == "":
            print("Please enter your input")
        else:
            None
