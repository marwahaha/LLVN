image ea = "gui/early_access.png"
default menuset = set()
# Prologue

# Introduction
label start:
    # show ea
    # if persistent.analytics is None:
# 
        # menu:
            # "Welcome! This game supports analytics. Enabling it will help us make better games, and will send data to Google Analytics and the developers. Do you want to enable analytics?"
# 
            # "Yes.":
                # $ persistent.analytics = True
                # "Thank you."
# 
            # "No.":
                # $ persistent.analytics = False
                # "No problem!"
    # Start in the house of your grandparents.
    stop music fadeout 1.0
    scene house with Dissolve(0.5)
    show ea

    # Ask protagonist name.
    n "Welcome, please give your character a name. If you don't it will use 'Yuukou Mika'."
    python:
        playername = renpy.input("What is your name?")
        playername = playername.strip()
    
        if not playername:
             playername = "Yuukou Mika"

    jump select_home
