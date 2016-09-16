## Declare characters used by this game. The color argument colorizes the name
## of the character.
define timo = Character('Timo', color="#00b6ef", image="timo")
define pronoun = ('they', 'them', 'their')

## The game starts here.

label start:
    ## jump to my snake playground
   # jump snek
   jump first

## here's some fun with vanilla ren'py
label first:
    #play music music.chillout 

    scene bg_gate with fade

    "So what're your pronouns?"

    menu:
        "They/Them/Their":
            jump welcometimo

        "He/Him/His":
            $ pronoun = ('he', 'him', 'his');
            jump welcometimo

        "She/Her":
            $ pronoun = ('she', 'her', 'her');
            jump welcometimo

        "Um, actually...":
            jump enterpronouns


label enterpronouns:
    python:
        nom = renpy.input("Enter your preferred pronoun for this sentence:\nWe know that {b}(pronoun){/b} likes to blow things up")
        acc = renpy.input("Enter your preferred pronoun for this sentence:\nMeet {b}(pronoun){/b} in the courtyard.")
        gen = renpy.input("Enter your preferred pronoun for this sentence:\nThis is {b}(pronouns){/b} room.")
        pronoun = (nom, acc, gen);
    jump welcometimo

label welcometimo:
    show timo at right with moveinright

    timo "Welcome to crime school... "

    show timo laugh with Dissolve(0.1)

    extend "which is for crime!"

    show timo with Dissolve(0.1)
    timo "I've been wondering! {i}Where could [pronoun[0]] be?{/i}"

    timo "{i}Will I ever see [pronoun[1]]{/i}?"

    timo "{i}And most importantly, who inherits [pronoun[2]] luggage?!{/i}"

    menu:
        "Finally, I've found it!":
            jump welcomep

        "... It looks like a jail...":
            jump welcomen

label welcomep:
    timo "No hard feelings. This facility was built to be hard to find."
    jump welcome02


label welcomen:
    show timo 
    timo "Of course it does!"

    timo laugh "It's a grim reminder of your future."
    jump welcome02

label welcome02:
    timo "Come on inside now. Let me show you around!"
    "--- years later ---"
    hide timo
    jump ruben01

    ## This ends the game.

    return
