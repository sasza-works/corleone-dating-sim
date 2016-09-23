init python:
## holy shit. events!
    import pygame

    score = 0
    direction = { "up" : -1, "down" : 1, "left": -10, "right": 10 }
    scale = 50;
    snakeRange = [ (0,0), (13,0), (13,11), (0,11) ] 
    wormsprite = list()

    def spriteEvent(ev, x, y, st):
        ## it is receiving ALL the events. christ.
        return
        #keyup = str(pygame.constants.KEYUP)
        #event = str(ev.type)

    def isInRange(coord):
        x = coord[0]
        y = coord[1]
        xmin = snakeRange[0][0] * scale
        xmax = snakeRange[1][0] * scale

        ymin = snakeRange[1][1] * scale
        ymax = snakeRange[2][1] * scale

        return (x >= xmin and x <= xmax) and (y >= ymin and y <= ymax)

    def getFuturePosition(): 
        futurex = wormsprite[0].x
        futurey = wormsprite[0].y
        if (playerdirection == direction["up"]):
            futurey -= scale
        if (playerdirection == direction["down"]):
            futurey += scale
        if (playerdirection == direction["left"]):
            futurex -= scale
        if (playerdirection == direction["right"]):
            futurex += scale
        return (futurex, futurey)

    def updatePositions(coords):
        x = coords[0]
        y = coords[1]
        for member in wormsprite:    
            x1 = member.x
            y1 = member.y
            member.x = x
            member.y = y
            x = x1 
            y = y1
        return (x,y)

    def addToTail(coords):
        tail = spritemanager.create("ball.png")
        tail.x = coords[0]
        tail.y = coords[1]
        wormsprite.append(tail)

    def checkAgainstSelf(coords):
        renpy.log("CHECK AGAINST SELF...")
        renpy.log("updated position: " + str(coords[0]) + ", " + str(coords[1]))
        for index in range(len(wormsprite)):
            renpy.log(str(index) + ": " + str(wormsprite[index].x) + ", " + str(wormsprite[index].y))
            if (index == 0): 
                continue
            equalx = wormsprite[index].x == coords[0]
            equaly = wormsprite[index].y == coords[1]
            if (equalx and equaly):
                renpy.log("!!!--END: COLLISION")
                collision()
                return False
        return True
        renpy.log("--END: NO COLLISION")

    def collisionCheck(coord):
        if isInRange(coord):
            return True 
        else:
            collision()
            return False


    def collision():
        renpy.sound.play(audio.snekmiss)
        renpy.jump("snekend")

    def eatCheck():
        for item in items:
            if (wormsprite[0].x == item.x and wormsprite[0].y == item.y):
                item.x = renpy.random.randint(snakeRange[0][0], snakeRange[1][0]) * scale
                item.y = renpy.random.randint(snakeRange[1][1], snakeRange[2][1]) * scale
                renpy.sound.play(snekeatersounds())
                global score
                score = score + 1
                renpy.notify("score: " + str(score))

    def spriteUpdate(st):
        coord = getFuturePosition()
        if (collisionCheck(coord) and checkAgainstSelf(coord)):
            eatCheck()
            lastcoords = updatePositions(coord)
            if score >= len(wormsprite):
                addToTail(lastcoords) 
        return 0.2


    def initSnek():
        renpy.log("INIT SNEEEEK")
        global spritemanager
        global itemsprite 
        global wormsprite 
        global playerdirection 
        global items 
        global itemsprite
        global score 
        score = 0
        spritemanager = SpriteManager(update=spriteUpdate, event=spriteEvent)
        itemsprite = spritemanager.create("snow.png")
        head = spritemanager.create("ball.png")
        head.x = 150
        head.y = 100 
        wormsprite = list()
        wormsprite.append(head)
        playerdirection = direction["down"]
        items = [ itemsprite ]
        itemsprite.x = 250
        itemsprite.y = 200  

    def cleanSnek():
        global wormsprite 
        global items 
        global spritemanager
        del spritemanager
        del wormsprite 
        del items 
        renpy.notify("CLEANIIIIING")

    def MyFunction(key):
        if (key == "m"):
            renpy.hide_screen("snek")
            renpy.jump("first")
        return

    MyCurriedFunction = renpy.curry(MyFunction) ## == closure


    def changeDirection(newdirection):
        global playerdirection
        if (playerdirection + newdirection == 0):
            return
        playerdirection = newdirection
        return

    def goUp():
        newdirection = direction["up"]
        changeDirection(newdirection)
        return

    def goDown():
        newdirection = direction["down"]
        changeDirection(newdirection)
        return

    def goLeft():
        newdirection = direction["left"]
        changeDirection(newdirection)
        return

    def goRight():
        newdirection = direction["right"]
        changeDirection(newdirection)
        return



screen snek():
    modal True  
    tag snake
    frame:
        xalign 0.5
        yalign 0.5

        fixed:
            xmaximum 700
            ymaximum 600
            add LiveTile("tile.png")
            add spritemanager
            key "w" action goUp
            key "a" action goLeft
            key "s" action goDown
            key "d" action goRight
            key "m" action MyCurriedFunction("m")

screen sneklose(score):
    modal True
    tag snake
    frame:
        xalign 0.5
        yalign 0.5

        text _("Score: " + str(score))
    
label snek: 
    $ initSnek()
    call screen snek

label snekend:
    hide screen snek
    $ cleanSnek()
    show screen sneklose(score)
    menu: 
        "try again":
            hide screen sneklose
            jump snek
        "no thanks I'm good":
            hide screen sneklose
            jump first