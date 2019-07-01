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
    scene room with blinds
    n "Where am I?"
    u "Oh, you've woken up. Drink some water."
    show maki_05_01 at left
    p "Thanks."
    show makismom1 at right
    u "How are you feeling?"
    p "I'm feeling fine now, thank you."
    u "I'm sorry for that map, that was a mistake of us."
    p "Huh?"
    u "We were the ones who talked to your dad to invite you here."
    u "This is my daughter, Maki Nishikino. I'm her mother."
    MakiMom "But do you want to sleep again?"
    p "Yes, I want to have some more sleep."
    MakiMom "Ok. Maki, you can stay there if you want. Sleeping with him is also fine."
    hide maki_05_01
    show maki_05_06 at left
    Maki "MOM!"
    with hpunch
    n "She threw a pillow at me. Why on me?"
    hide maki_05_06
    with dissolve
    MakiMom "Oh, she ran away."
    n "And who's fault is that?"
    MakiMom "But good night."
    #scene black
    hide makismom1
    define c_fade_01 = Fade(1.0, 2.0, 1.0) # c = custom, this is how I'll define custom transistions
    scene room with c_fade_01
    n "Where am I?"
    n "Oh, that's right. I was at Nishikino's house."
    n "I'm hungry, I should look where the Nishikino-san's mother is."
    scene music-room with fade
    show maki_05_01 at left
    p "Nishikino-san?"
    hide maki_05_01
    show maki_05_03 at left
    Maki "?!"
    hide maki_05_03
    show maki_05_01 at left
    Maki "Oh, it's you. What is it?"
    p "Where is your mother?"
    Maki "She's in the kitchen."
    p "Could you take me there, I don't know where it is."
    Maki "Fine, follow me."
    scene home with dissolve
    show maki_05_01 at left
    show makismom1
    p "Thanks Nishikino-san."
    MakiMom "Oh, you're awake. Are you hungry? Also, you can just call her Maki."
    p "Is that fine with you?"
    Maki "It doesn't really matter for me."
    p "And yes, I'm hungry."
    MakiMom "That's good, I just made breakfast for you."
    p "Thanks!"
    MakiMom "Why don't you two go on a date today?"
    hide maki_05_01 at left
    show maki_05_03 at left
    "Both" "DATE?!"
    MakiMom "I mean, [firstname]-kun doesn't know the city yet so maybe you can show him around."
    Maki "Oh… So that was what you meant… Don’t scare me like that, Mom."
    hide maki_05_03
    show maki_05_01 at left
    MakiMom "Teehee"
    n "Don't just 'Teehee', you gave me nearly a heart attack. But I wouldn't mind a citytour."
    Maki "If it's fine with you, then I don't mind."
    p "It's fine with me, shall we go this afternoon?"
    Maki "Ok."
    scene shopping-street with blinds
    show maki_05_01 at left
    n "Maki showed me around Akihabara since I was wondering where it was. We were currently doing some shopping, she looked like she was having fun."
    n "Oh, I'm hungry. My stomache is rumbling."
    Maki "What's wrong?"
    p "I'm getting kind of hungry."
    Maki "You could have told me earlier."
    p "But you looked like you were having fun."
    hide maki_05_01
    show maki_05_03 at left
    Maki "B-but let's go, I'm also getting hungry."
    scene restaurant-2 with dissolve
    show maki_05_01 at left
    n "When I walked into a restaurant with Maki I saw a blonde girl at a table in the corner with a purple haired girl. I have a feeling I knew her."
    Maki "[lastname]-kun, what do you want?"
    p "Huh? Oh, a sandwich and orange juice will be fine."
    Maki "I'll order then, can you get a table for us?"
    p "Fine."
    hide maki_05_01
    n "There were two seats to the two girls, so I sat there. I was looking at the blonde girl, thinking where I know here from."
    u "I'm going to the toilet, ok?"
    n "Oh, I remember! She looks like my childhood friend back in Russia."
    n "I looked again at her. Oh, crap. She noticed I was looking at her."
    show maki_05_01 at left
    Maki "Here's what you asked for."
    p "Thanks, Maki."
    n "As Maki sits down, I look again at that girl. She looked back at me with an angry face."
    n "She stood up and walked to us."
    show eli_05_05 at right
    u "Why were you looking at me?"
    Maki "Huh?"
    p "I'm sorry, you looked like my childhood friend."
    n "I stood up and bowed to her."
    show nozomi_05_01 at center
    u "Eli-chi, what's wrong?"
    n "Eli-chi, Elichi, Elichika… It can't be, is she really Elichika?"
    p "You… Are you…"
    Maki "Do you know her?"
    p "Are you Elichika?"
    n "“Elichika” was the nickname that I gave my childhood friend when we were kids. I remember that we always played together, we were really close back then."
    hide eli_05_05
    show eli_05_03 at right
    Eli "H-how do you know my old nickname? Are you…"
    u "Huh?"
    Eli "[firstname]-kun?"
    p "Yes… Long time no see, Elichika."
    hide eli_05_03
    show eli_05_02 at right
    n "She jumped into my arms and hugged me tight."
    p "Huh?"
    n "When I looked at her I saw she was crying."
    Eli "I really, really missed you so much…"
    Maki "What's going on?"
    u "I don't understand. Can you explain?"
    p "Haha… Elichika, can you let off of me?"
    Eli "I'm sorry."
    Eli "Nozomi, this is [playername]. [firstname]-kun, this is Nozomi Tojo."
    Nozomi "You can just call me Nozomi."
    p "But…"
    Nozomi "It's fine, a friend of Eli-chi is also a friend of mine."
    p "Maki, this is Eli Ayase, my childhood friend from Russia. Elichika, this is Nishikino Maki. I'm living at her house because of my father."
    Maki "Pleased to meet you."
    Eli "Pleased to meet you too. So you're living at her house right now [firstname]-kun?"
    p "Yes, I am."
    scene stairs-street with dissolve
    show maki_05_01 at left
    show eli_05_01 at right
    show nozomi_05_01 at center
    n "After we were finished eating we walked around the city talking with each other."
    Maki "[lastname]-kun, I'm going. I need to do some stuff."
    Eli "Leaving so soon?"
    Nozomi "We are just getting to know each other."
    Maki "Really? [lastname]-kun, if you want you can stay with them. Call me if you can't find your way home."
    p "Are you really sure?"
    Maki "Yes, nice meeting you too, Ayase-san, Tojo-san. Goodbye."
    Eli "Goodbye."
    Nozomi "Bye."
    p "W-wait!"
    Maki "What?"
    p "Thanks for everything."
    hide maki_05_01
    show maki_05_05 at left
    Maki "I-it's not like I’m being nice to you or anything! I’m just being considerate!"
    p "Ok, ok. Bye."
    hide maki_05_05 with dissolve
    scene street-2 with blinds
    show eli_05_01 at right
    show nozomi_05_01 at center
    n "After Maki left we were talking about everything that happened when we were kids and things that happened in our lives. It was already evening before we noticed."
    Nozomi "I need to go, are you coming with me Eli-chi?"
    Eli "W-wait. [firstname]-kun, do you have a moment?"
    p "Yes, why?"
    Nozomi "You're leaving me alone now?"
    Eli "I'm sorry, I'll make it up to you tomorrow."
    Nozomi "Nah, just kidding. See you tomorrow Eli-chi."
    Eli "Bye."
    p "Goodbye."
    hide nozomi_05_01 with dissolve
    scene park-3
    show eli_05_01
    Eli "Shall we take a walk?"
    p "That's fine."
    n "We were walking around but when Eli saw a bench she sat on it. I sat next to her."
    Eli "A-are you still mad at me about what happened years ago?"
    n "She asked me with a worried face."
    p "You mean that accident?"
    n "I got into accident when I was young. It is the one who break my legs and also my dreams."
    n "Because that accident I lost my friends and all important things in my life."
    n "It doesn't matter anymore. I don't have any interest on the people around me. And I don't have any dreams now."
    p "I've forgiven you along time ago, I knew you didn't meant to do that."
    Eli "Why are you here in Japan then?"
    p "I'm here because I needed a medical rehabilitation for my legs. I could never be angry at you for a long time."
    Eli "I thought all this time you would be really angry at me. I mean, you nearly died because of me."
    p "No worries, it’s all good."
    Eli "Ok, if you say so. Again, I'm really sorry about what happened."
    p "I need to go now, ok? It's pretty late now."
    Eli "This is then where we will split our ways."
    p "Ok, goodnight."
    Eli "W-wait, can I get your phone number?"
    p "Sure, let's exchange our phone numbers."
    n "We exchanged numbers and try it out by sending a simple “Hi”, testing if we got it correctly."
    Eli "Uhm… Let's keep in touch, ok?"
    p "Sure."
    Eli "Can I call you later on?"
    p "Of course. I need to go now, goodbye Elichika."
    Eli "Goodbye."
    jump nishikino_closure
