# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("[playername]")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene house

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show arisa_01_04
    
    # Ask protagonist name.
    python:
        playername = renpy.input("What is your name?")
        playername = playername.strip()
    
        if not playername:
             playername = "Yuukou Mika"

    # These display lines of dialogue.

    p "You've created a new Ren'Py game."

    p "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
