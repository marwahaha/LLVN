label select_home:
    set menuset
    n "I'm currently at my grandparents house, I was staying here for this weekend because I wanted to visit them again."
    p "I'm bored. What can I do?"
    menu selhome:
        "What should I do?"
        
        "Call my dad":
            "Choice not available yet."
            return #End game.
            #jump selhome_calldad
        
        "Call my mom":
            "Choice not available yet."
            return #End game.
            #jump selhome_callmom
        
        "Do nothing":
            "Choice not available yet."
            return #End game.
            #jump selhome_none

    menu afterselhome:
        # After selecting home
