## Declare characters used by this game. The color argument colorizes the name
## of the character.

define timo = Character('Timo', color="#00b6ef", image="timo")
define trisha = Character('Trisha', color="#c1d26a", image="trisha")
define pronoun = ('they', 'them', 'their')

## The game starts here.

label start:
    ## jump to my snake playground
    call snek 
    # give this method a callback which will be processed when user is done playing as a 2nd parameter
    $ renpy.log("start: score of snek " + str(_return))
    scene bg_gate with fade
    show trisha at center
    show timo rage at right with moveinright
    trisha "..."
    jump first

## here's some fun with vanilla ren'py
label first:
    #play music chillout 

    scene bg_gate with fade

    "So what're your pronouns?"

    menu:
        "They/Them/Their":
            jump welcome

        "He/Him/His":
            $ pronoun = ('he', 'him', 'his');
            jump welcome

        "She/Her":
            $ pronoun = ('she', 'her', 'her');
            jump welcome

        "Um, actually...":
            jump enterpronouns


label enterpronouns:
    python:
        nom = renpy.input("Enter your preferred pronoun for this sentence:\nWe know that {b}(pronoun){/b} likes to blow things up")
        acc = renpy.input("Enter your preferred pronoun for this sentence:\nMeet {b}(pronoun){/b} in the courtyard.")
        gen = renpy.input("Enter your preferred pronoun for this sentence:\nThis is {b}(pronouns){/b} room.")
        pronoun = (nom, acc, gen);
    jump welcome

label welcome:
    show timo at right with moveinright

    timo "Welcome to crime school... "

    show timo laugh 

    extend "which is for crime!"

    show timo with Dissolve(0.1)
    timo "I've been wondering! {i}Where could [pronoun[0]] be?{/i}"

    timo "{i}Will I ever see [pronoun[1]]{/i}?"

    timo "{i}And most importantly, who inherits [pronoun[2]] luggage?!{/i}"

    menu:
        "Finally, I've found it!":
            timo "No hard feelings. This facility was built to be hard to find."

        "... It looks like a jail...":
            timo "Of course it does!"
            timo laugh "It's a grim reminder of your future."

    timo "Come on inside now. Let me show you around!"
    
    jump .atrium

label .atrium:
    
    scene bg_atrium with fade
    show timo at right
    timo "This is the atrium. It's the hub of activity, what with the stairwells and the cafeteria."
    timo "Speaking of which, I'm only just realising I've lived off two Snickers for the last 24 hours..."
    timo "I'm gonna pop into the cafeteria for a bit."

    menu:
        "I'll come with!":
            jump ruben01

        "I'd rather wait here":
            hide timo with moveoutright
            "You use this quiet moment to look around."
            jump trisha

label trisha:
    show trisha with moveinright
    "You see a heavily tattooed butch. She is kind of hard to miss, actually."
    call interactionmenu pass (approach="trisha.first", observe="trisha.observe", leave="ruben01")

label .intro:
    show trisha with moveinright

    "You see a heavily tattooed butch reading a book."
    menu:
        "Talk to her":
            jump .first

        "I'd rather not.":
            jump ruben01

label .observe:
    "She is reading a rather massive looking softcover. It takes a bit of effort to figure out the writing on the bent spine."
    "It turns out to be {i}Philosophy of Language{/i} by {i}William Lycan{/i}."

label .first:
    $ masculine = pronoun == ('he', 'him', 'his')
    if masculine:
        trisha "Sod off, I'm tryin tae read."
    else:
        trisha "You need something?"


    ## This ends the game.

    return
