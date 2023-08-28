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
![Storyboard Flowchart](documents/save_the_seaturtle_game_storyboard.jpg)

### Flowchart planning 
This is a basic structure plan for the code, mapping out the necessary functions to work from.  
![Functions Flowchart](documents/save_the_seaturtle_game%20_functions.jpg) 

## Existing Features

## Code errors 
## Code decorators?
## If else functions

## Features left to implement

- Key option 'back', to alow the user to go back and try other options. 

The text-based game could be further developed with images and a more detailed storyline, as with an RPG, like many other nintendo games (Super Mario, Animal Crossing, Legend of Zelda) ideal for the nintendo switch. 
In order to enable this, the storyline would need to be simplified, add mutliple characters and update the functionality. Main character would be identified rather than asking a user to assign a name, and the story would start by introducing this character.

For example : 
"Ahoy Crush! I like the way you're riding the waves! Dude, it's time for an adventure! Your aim is to keep safe and avoid being eaten by the Great White Shark and any other hidden terrors - so watch out.
Which way would you like to go next?" 
Allowing the game to become a RPG would simplify the storyline and make this more unniversal for younger children. 

## Design

### Validator Testing

## Examples:

### PEP8

### Solved Bugs

- Terminal identified a number of indentation errors - quickly resolved with human eye. 
- Exit function would not work as parentheses included each individual function to call, fixed by calling main function, with all other functions inside. Thus, avoided repetition in code. 
- Import pygame and import os from OSMOD would not provide the correct import of the keyborad needed to link user pressed keys and user input to the game. Instead, keyboard has been imported. 

### Unsolved Bugs

## Deployment

## Credits

### Inspired websites/ books
Python Tricks The Book - Dan Bader 
- 4:3 Defining your own Exception Classes
- 2:4 Underscores, dunders and more  

Invent Your Own Computer Games With Python - Al Sweigart 
- 5 : Dragon Realm 

https://www.geeksforgeeks.org/how-to-print-to-stderr-and-stdout-in-python/ - import sys 

### Tutor/mentor suggestions

### Inspiration and content 
https://www.iucnredlist.org/species/11534/3292503
https://oliveridleyproject.org/threats-to-sea-turtles

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
