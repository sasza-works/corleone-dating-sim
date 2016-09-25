init python:
## holy shit. events!
    import pygame

    score = 0
    direction = { "up" : -1, "down" : 1, "left": -10, "right": 10 }
    scale = 50;
    snakeRange = [ (0,0), (13,0), (13,11), (0,11) ] 
    wormsprite = list()

    def defaultSnekCallback(score):
        renpy.log("default snake callback. score: " + str(score))
        return

    snekCallback = defaultSnekCallback

    def spriteEvent(ev, x, y, st):
        ## it is receiving ALL the events. christ.
        return
        #keyup = str(pygame.constants.KEYUP)

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
        for index in range(len(wormsprite)):
            if (index == 0): 
                continue
            equalx = wormsprite[index].x == coords[0]
            equaly = wormsprite[index].y == coords[1]
            if (equalx and equaly):
                collision()
                return False
        return True

    def collisionCheck(coord):
        if isInRange(coord):
            return True 
        else:
            collision()
            return False


    def collision():
        renpy.sound.play(audio.snekmiss)
        renpy.log("collision")
        showScoreBoard(score, nextScene)

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
        speed = 0.2
        coord = getFuturePosition()
        if (collisionCheck(coord) and checkAgainstSelf(coord)):
            eatCheck()
            lastcoords = updatePositions(coord)
            if score >= len(wormsprite):
                addToTail(lastcoords)
                if score > 0:
                    speed =- 100/score 
        return speed


    def initSnek(pNextScene, pCallback=defaultSnekCallback):
        renpy.log("INIT SNEEEEK")
        global spritemanager
        global itemsprite 
        global wormsprite 
        global playerdirection 
        global items 
        global itemsprite
        global score
        global nextScene
        global callback
        snekCallback = pCallback
        nextScene = pNextScene
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
        renpy.call_screen("snek", pNextScene)


    def cleanSnek():
        global wormsprite 
        global items 
        global spritemanager
        del spritemanager
        del wormsprite 
        del items 

    def exitSnek(label):
        renpy.log("exit snek. jumping to... " + str(label))
        renpy.hide_screen("snake")
        renpy.jump(label)

    ExitAndJumpTo = renpy.curry(exitSnek)

    def showScoreBoard(score, label):
        pscore = score
        renpy.call("snekMenu", score, label)

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

screen snek(nextScene):
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
            key "m" action ExitAndJumpTo(nextScene)
    
label snek: 
    $ initSnek("first") # parametrise method wiRth label we're jumping to after
    # give this method a callback which will be processed when user is done playing as a 2nd parameter

#TODO the control flow isn't quite right. errors happening at the end of the game.
label snekMenu(score, nextScene):
    show text "Score: [score]"
    menu:
        "try again":
            call snek(nextScene)
        "no thanks i'm good":
            if snekCallback == None:
                jump expression nextScene
            else:
                $ snekCallback(score)
                jump expression nextScene