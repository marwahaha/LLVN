# Prologue

# Introduction
label start:

    # Start in the house of your grandparents.

    scene house

    # This sprite is for testing.

    show arisa1
    
    # Ask protagonist name.
    "Welcome, please give your character a name. If you don't it will use 'Yuukou Mika'."
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
