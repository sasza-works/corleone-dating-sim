
define ruben = Character('Ruben', color="#aa2020", image="ruben")
define louise = Character('Louise', color="#20aaa0")

label ruben01:

    show ruben at right
    ruben "so a train is going to run down these five people tied to the railway, except if you pull a lever, which will redirect the train onto a railway where a single person is tied up."
    ruben "what are you going to do?"

    $ lever = "person"

    menu: 
        "pull the lever": 
            $ lever = "girl"

        "don't pull the lever":
            $ lever = "guy"

    ruben "i see." 
    ruben "now imagine the same thing... "
    extend "except there is no lever."
    ruben "you can only stop the train by pushing something heavy in front of it."
    ruben "chance has it that you see a really fat [lever] right next to you. what do you..."
    show louise at left
    louise "what was that about fat people??"
    show ruben blush
    ruben "um. it's just a thought experiment..."