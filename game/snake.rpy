init python:

    def spriteEvent(ev, x, y, st):
        renpy.log("event: " + str(type(ev)))

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
    MyCurriedFunction = renpy.curry(MyFunction)


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
    "snek"
    show wormsprite at left
    "snuk"
    show screen grid
    "grid"
    #python:
    #    
    #    

   # show expression spritemanager as spritemanager
    "sprite"
    #hide spritemanager
    jump enterpronouns