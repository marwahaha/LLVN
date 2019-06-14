# Sprites
image arisa1 = im.Scale("images/sprites/arisa_01_01.png", 720, 720)
image arisa2 = im.Scale("images/sprites/arisa_01_02.png", 720, 720)

# Characters
# Main
define p = Character("[playername]")
define Honoka = Character("Honoka Kosaka")
define Eli = Character("Eli Ayase")
define Kotori = Character("Kotori Minami")
define Umi = Character("Umi Sonoda")
define Maki = Character("Maki Nishikino")
define Nozomi = Character("Nozomi Tojo")
define Nico = Character("Nico Yazawa")
define Hanayo = Character("Hanayo Koizumi")
define Rin = Character("Rin Hoshizora")

# Secondary
define Arisa = Character("Arisa Ayase")

# Prologue

# Introduction
label start:

    # Start in the house of your grandparents.

    scene house

    # This sprite is for testing.

    show arisa1
    
    # Ask protagonist name.
    python:
        playername = renpy.input("What is your name?")
        playername = playername.strip()
    
        if not playername:
             playername = "Yuukou Mika"

    # More testing
    hide arisa1
    show arisa2
    Arisa "Hi [playername]"

    Arisa "Welcome to this visual novel, this is an in development game."
    Arisa "As you can see, there isn't anything here yet."

    # Because it's still in development this is the end.

    return
