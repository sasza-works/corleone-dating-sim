init python:
## holy shit. events!
    import pygame

    score = 0

    def spriteEvent(ev, x, y, st):
        ## it is receiving ALL the events. christ.
        keyup = str(pygame.constants.KEYUP)
        event = str(ev.type)
        if (event == keyup):
            renpy.log("wormsprite position:")
            renpy.log(str(wormsprite.x) + " // " + str(wormsprite.y))
            for item in items:
                if (wormsprite.x == item.x and wormsprite.y == item.y):
                    renpy.log("worm ate the item")
                    item.x = renpy.random.randint(1, 15) * 50
                    item.y = renpy.random.randint(1, 14) * 50
                    renpy.log("gonna show next item at " + str(item.x) + " " + str(item.y))
                    renpy.sound.play(snekeatersounds())
                    global score
                    score = score + 1
                    renpy.notify("score: " + str(score))

    def spriteUpdate(st):
        return 0.1

    spritemanager = SpriteManager(update=spriteUpdate, event=spriteEvent)
    itemsprite = spritemanager.create("snow.png")
    wormsprite = spritemanager.create("ball.png")

    items = [ itemsprite ]

    itemsprite.x = 250
    itemsprite.y = 200

    def MyFunction(key):
        if (key == "m"):
            renpy.hide_screen("grid")
            renpy.jump("first")
        if (key == "w"):
            wormsprite.y -= 50
        if (key == "a"):
            wormsprite.x -= 50
        if (key == "s"):
            wormsprite.y += 50
        if (key == "d"):
            wormsprite.x += 50
        return

    MyCurriedFunction = renpy.curry(MyFunction) ## == closure


    def goUp():
        wormsprite.y -= 50
        return

    def goDown():
        wormsprite.y += 50
        return

    def goLeft():
        wormsprite.x -= 50
        return

    def goRight():
        wormsprite.x += 50
        return

screen grid():
    modal True
    tag snake
    add LiveTile("tile.png")
    add spritemanager

    key "w" action goUp
    key "a" action goLeft
    key "s" action goDown
    key "d" action goRight
    key "m" action MyCurriedFunction("m")
    
label snek: 
    show wormsprite at left
    show screen grid
    #python:
    #    
    #    
    "booty"
   # show expression spritemanager as spritemanager
    #hide spritemanager
    jump enterpronouns