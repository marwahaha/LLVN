label select_home:
    n "I'm currently at my grandparents house, I was staying here for this weekend because I wanted to visit them again."
    p "I'm bored. What can I do?"
    menu selhome:
        "What should I do?"
        
        "Call my dad":
            jump nishikino_residence
        
        "Call my mom":
            "Choice not available yet."
            return #End game.
            #jump selhome_callmom
        
        "Do nothing":
            "Choice not available yet."
            return #End game.
            #jump selhome_none

label nishikino_residence:
    n "Let's call dad, I haven't spoken with him for the last couple days."
    n "Tring, tring..."
    n "Huh, oh it's dad."
    p "Hi dad, I just wanted to call you too."
    Dad "We think alot alike, don't we? But I wanted to ask you something."
    p "What do you want to ask?"
    Dad "Why don't move to Akihabara?"
    p "WHAT?! Why? I quite like it here."
    Dad "You wanted to attend Otonokizaka High and visit Akihabara, didn't you?"
    p "You got me there..."
    scene street
    n "That's how I came here. I got a map, but it doesn't look quite right."
    p "Hello, can I ask you something?"
    Passerby "What is it?"
    p "Where can I find this?"
    n "I pointed at the location on the map."
    Passerby "That map doesn't look right, since that's an empty plot of land. But if you go that way you should come there."
    n "One hour later..."
    p "Where am I supposed to go? I'm at the same place as first."
    n "I was feeling a bit dizzy."
    show maki_05_05 at right
    u "Are you feeling well?"
    n "That was the last thing I heard before I lost my consciousness."
    scene black with pixellate
    hide maki_05_05
    scene room
    n "Where am I?"
    u "Oh, you've woken up. Drink some water."
    show maki_05_01 at left
    p "Thanks."
    show makismom1 at right
    u "How are you feeling?"
    return
