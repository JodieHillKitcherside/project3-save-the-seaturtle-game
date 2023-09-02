# Save the Sea Turtle Game

The Save the Sea Turtle Game has been created as a mini adventure game, perfect to play as you would have on a gameboy in the 80s! This mini adventure game follows the real life challenges faced to Sea Turtles, of which all species are either vulnerable or critcially endagered, significantly due to human threats. 
As tragic and morbid as this sounds, the game aims to make a light-hearted fun, and to educate anyone who plays it in a mini adventure episode. 
The quiz' main target market group would be ideal for pre-teen or teenagers, who typically would play adventure games and perfect as it is educational. Of course, this is welcome to all adults to try too!

The game is story based, with four main options to choose the 'sea turtle's next move. This them passes on to various actions. 
This formatted in Python Script, styled as a text-based room exploration game. Each option offers the user to use several keys to change direction, giving contol to the user to explore different sequences of the sea turtle's life.

# User Feedback

- ""

# Features

### Storyboard:

This is a basic format used to structure the story for the game.  
![Storyboard Flowchart](assets/images/planning_storyboard.png)

### Flowchart planning 
This is a basic structure plan for the code, mapping out the necessary functions to work from.  
![Functions Flowchart](assets/images/planning_functions.png) 

## Existing Features

### Move through inputs 
Inputs have been created to include the user in the game, adding to the user experience within the terminal. First, the user is asked to type their name, then the user is asked to choose from a list of key options: Up, Down, Left and Right. 
The name input is used throughout to draw reference back to the user.

### Code errors 
Wrong or missing inputs will be identified and an error message and print statement will appear. 

### If else functions
Most next steps as you progress throughout the quiz provide a question with two directions to choose from in order to continue. If the user selects from either key, they will progress to the next step in the sea turtle's adventure. If there is another option selected, there will be an error message. 

## Features left to implement

- Key arrows (Up/Down/Right/Left).
- Key options 'backspace' 'esc' and 'quit', to alow the user to go back and try other options. 
- Deeper storyline, more options other than limited death, allowing th user to understand more about the life of that species. 
- Other endangered species games, allowing use to choose which animal to play. 
- Basis for a cool RPG for children and young adults to play for in years to come, when several species have become extinct. For example, we could already create learning around the lift of recently extinct animals: Northern White Rhinocerous, Baiji or Pyrenean Ibex. As many games today are action-adventures and story based, it would be cool for something like this to team up with WWF or the National Geographic for children's fun and learning. 

# Addtional files to support run.py
- Emojis.py hosts the Emoji() class with all emoji unicodes, this is then sourced in run.py and used as part of a string. 
- Statements.py hosts the statements for each function called in run.py that follows the reusable function 'slowPrintExit()'. This was created to simplify code and cut repetition. 

# Frameworks, libraries and modules used 
- Sys used for slowprint() 
- Time used for slowprint() 
- Pyfiglet for termainal header - ASCII art 
- Emojis import Emoji - for emojis.py, run.py and statements.py

## Design

Index.html displays a background image of a vivid colourful ocean bed. White headings and footer have been styled to stand out in the foreground. 

### Validator Testing

## Examples

### PEP8

### Solved Bugs

- Terminal identified a number of indentation errors - quickly resolved with human eye. 

- Exit function would not work as parentheses included each individual function to call, fixed by calling main function, with all other functions inside. Thus, avoided repetition in code. Added a reusable function.

- Emoji class use: All of attributes in the emojis.py file had the same names as methods, which conflicted and was 
repeated code. Emojis.py has 
1 class and calls the class in run.py and statements.py at the string ie. "+ emoji_choice.seaturtle".

- User input: User input was appearing before the main intro, being called as a global variable and therefore have locally stored the named variable in each story statement.

- Keyboard arrows:
1. Goal: Download a module to support the keyboard arrows Up, Down, Right, Left. Solely for user experience and ease throughout the game. 
2. Actions: Imported keyboard, pyglet, pygame, os from OSMOD, pynput and Tkinter *; all separately. None of these worked and displayed many errors. Time spent trying to correct these errros is largely time lost. As the site runs solely on a terminal, the graphical inputs weren't supported. 
3. Back to basics: Instead have reverted to alphanumeric input only and described keys 'u' as Up for example. 
4. Further issues: 
- Import error - script running as root; Backend error suggesting 'must use a root' whilst using the library on Linux. Based on answers from ChatGBT, installed a root with myenv in the backend files alongisde main files. 
- After looking closely to the traceback message, identifieid the source error: 'event = keyboard.read_event()  # Capture a keyboard event' (a line of code that hadn't been removed after several other testing tried in (2) above.)
- Result: Running 'if keyboard.is_pressed("u")' instead. 
- Still errors with keyboard: ImportError: You must be root to use this library on linux. Probably due to using Mac - https://stackabuse.com/guide-to-pythons-keyboard-module/. Then showed an't open file 'my_script.py': [Errno 2] No such file or directory. 
- Result: Completely uninstalled keyboard and reverted to basic user input. 

Keys now look like:
        "if intro_input == "u":
            gillnetRescue()"

### Unsolved Bugs

- Could not add an 'esc' or 'quit' function without installing, importing and using the keyboard module. 

## Deployment

The project was deployed using Code Institute's mock terminal for Heroku.

Please see the steps below exceuted:
1. Go to heroku.com, ensure sign up and logged in 
2. Click Create App
3. First check Settings: 
    - Config vars - if you have a creds.json, allow access (copy creds.json files)
    - Always add build packs - python, node.js (this order) save or click and drag to reorder
4. 	Deploy: 
	- Deployment method - click deploy to GitHub
	- Connect to GitHub and search repo name
	- Enable automatic deploy or manual deploy

If you choose manual:
- Review build master - check process and click link to view 
- Preview in new tab 

## Credits

### Inspired websites/ books
Python Tricks The Book - Dan Bader 
- 4:3 Defining your own Exception Classes
- 2:4 Underscores, dunders and more  

Invent Your Own Computer Games With Python - Al Sweigart 
- 5 : Dragon Realm 

https://www.geeksforgeeks.org/how-to-print-to-stderr-and-stdout-in-python/ - import sys 
https://www.geeksforgeeks.org/python-program-to-print-emojis/ - errors on unicode 

### Tutor/mentor suggestions
Oisin suggested the reduction of repeated code to resolve the Emoji() issue. 

### Inspiration and content 
https://www.iucnredlist.org/species/11534/3292503
https://oliveridleyproject.org/threats-to-sea-turtles

