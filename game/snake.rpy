init python:
## holy shit. events!
    import pygame

    class SnakeRound:
        def __init__(self):
            self.score = 0

        def nom(self):
            renpy.sound.play(snekeatersounds())
            self.score += 1
            renpy.notify("score: " + str(self.score))


    class SnakeField:
        direction = { "up" : -1, "down" : 1, "left": -10, "right": 10 }

        def defaultIsInRange(self, coord):
            x = coord[0]
            y = coord[1]
            xmin = self.snakeRange[0][0] * self.scale
            xmax = self.snakeRange[1][0] * self.scale

            ymin = self.snakeRange[0][1] * self.scale
            ymax = self.snakeRange[1][1] * self.scale

            return (x >= xmin and x <= xmax) and (y >= ymin and y <= ymax)

        def spriteUpdate(self, st):
            speed = self.speed
            coord = self.getFuturePosition()
            if (self.checkAgainstWalls(coord) and self.checkAgainstSelf(coord)):
                self.eatCheck()
                lastcoords = self.updatePositions(coord)
                if self.snakeRound.score >= len(self.wormsprite):
                    self.addToTail(lastcoords)
                    if self.snakeRound.score > 0:
                        speed = speed - (self.snakeRound.score*0.01)
                        self.speed = speed
                return speed
            return 0


        def __init__(self, speed=None, snakeRange=None, isInRange=None, wormsprite=None, scale=None, snakeRound=None, playerDirection=None):
            #spriteUpdate = renpy.curry(self.spriteUpdateSelf)
            self.spritemanager = SpriteManager(update=self.spriteUpdate)

            itemsprite = self.spritemanager.create("snow.png")
            itemsprite.x = 250
            itemsprite.y = 200
            self.items = [ itemsprite ]
            
            if speed is None:
                self.speed = 0.2
            else:
                self.speed = speed
            if snakeRange is None:
                self.snakeRange = [ (0,0), (13,11) ]
            else:
                self.snakeRange = snakeRange

            if isInRange is None:
                self.isInRange = self.defaultIsInRange

            if wormsprite is None:
                head = self.spritemanager.create("ball.png")
                head.x = 150
                head.y = 100 
                self.wormsprite = list()
                self.wormsprite.append(head)
            else:
                self.wormsprite = wormsprite
            if scale is None:
                self.scale = 50
            else:
                self.scale = scale
            if snakeRound is None:
                self.snakeRound = SnakeRound()
            else:
                self.snakeRound = snakeRound
            if playerDirection is None:
                self.playerDirection = self.direction["down"]
            else:
                self.playerDirection = playerDirection

        def isInRange(self, coord):
            return self.isInRange(coord)

        def changeDirection(self, direction):
            self.playerDirection = direction

        def getFuturePosition(self): 
            futurex = self.wormsprite[0].x
            futurey = self.wormsprite[0].y
            if (self.playerDirection == self.direction["up"]):
                futurey -= self.scale
            if (self.playerDirection == self.direction["down"]):
                futurey += self.scale
            if (self.playerDirection == self.direction["left"]):
                futurex -= self.scale
            if (self.playerDirection == self.direction["right"]):
                futurex += self.scale
            return (futurex, futurey)

        def updatePositions(self, coords):
            x = coords[0]
            y = coords[1]
            for member in self.wormsprite:    
                x1 = member.x
                y1 = member.y
                member.x = x
                member.y = y
                x = x1 
                y = y1
            return (x,y)

        def addToTail(self, coords):
            tail = self.spritemanager.create("ball.png")
            tail.x = coords[0]
            tail.y = coords[1]
            self.wormsprite.append(tail)

        def checkAgainstSelf(self, coords):
            for index in range(len(self.wormsprite)):
                if (index == 0): 
                    continue
                equalx = self.wormsprite[index].x == coords[0]
                equaly = self.wormsprite[index].y == coords[1]
                if (equalx and equaly):
                    self.collision()
                    return False
            return True

        def checkAgainstWalls(self, coord):
            if self.isInRange(coord):
                return True 
            else:
                self.collision()
                return False

        def collision(self):
            renpy.sound.play(audio.snekmiss)
            self.endRound()

        def endRound(self):
            renpy.end_interaction(self.snakeRound.score)

        def eatCheck(self):
            for item in self.items:
                if (self.wormsprite[0].x == item.x and self.wormsprite[0].y == item.y):
                    self.snakeRound.nom()
                    item.x = renpy.random.randint(self.snakeRange[0][0], self.snakeRange[1][0]) * self.scale
                    item.y = renpy.random.randint(self.snakeRange[0][1], self.snakeRange[1][1]) * self.scale

        def startSnek(self):
            renpy.log("-- start snek --")
            spritemgr = self.spritemanager
            renpy.call_screen("snekscreen", spritemgr)
            score = self.snakeRound.score
            return score 

    def cleanSnek():
        global snakeField
        del snakeField

    def goUp():
        snakeField.changeDirection(snakeField.direction["up"])
        return

    def goDown():
        snakeField.changeDirection(snakeField.direction["down"])
        return

    def goLeft():
        snakeField.changeDirection(snakeField.direction["left"])
        return

    def goRight():
        snakeField.changeDirection(snakeField.direction["right"])
        return

    def quit():
        snakeField.endRound()

screen snekscreen(spritemanager):
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
            key "m" action quit

# control flow still not completely proper
label snekMenu(score):
    show text "Score: [score]"
    menu:
        "try again":
            jump snek
        "no thanks i'm good":
            return 

# here is a demonstration.
label snek: 
    $ global snakeField
    $ snakeField = SnakeField()
    $ score = snakeField.startSnek()
    $ cleanSnek()
    call snekMenu(score)
    return score
