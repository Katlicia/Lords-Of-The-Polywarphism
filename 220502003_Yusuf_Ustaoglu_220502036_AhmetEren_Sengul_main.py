import pygame
from player import Player
import random

pygame.init()

# Game Config
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
pygame.display.set_caption("Lords of the Polywarphism")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
FPS = 60


# Default Game Settings
NUM_SQUARES = 16
FONT_SIZE = 40
gameState = "menu"
numOfPlayer = 2
playerTurn = "p1"
gameMode = "ai"
choosen = False
warrior = ""
started = False
fontUI = pygame.font.Font(None, 40)


# Colors
RED = (234, 153, 153)
RED2 = (158, 9, 9) # Darker Red
BLUE = (164, 194, 244)
BLUE2 = (17, 85, 204) # Darker Blue
GREEN = (182, 215, 168)
GREEN2 = (109, 170, 83) # Darker Green
YELLOW = (255, 229, 153)
YELLOW2 = (241, 196, 56) # Darker Yellow
ORANGE = (255, 66, 0)


# List for Rectangle Objects
rectList = [0]
# List for Player Moves
moveList = []

# Menu Image
menuImage = pygame.image.load("assets/poly2.png").convert_alpha()
scaledMenuImage = pygame.transform.scale(menuImage, (SCREEN_WIDTH, 500))


# Draws Start Button
def drawStart():
    mouseX, mouseY = pygame.mouse.get_pos()
    if 664 <= mouseX <= 1294 and 726 <= mouseY <= 866:
        startImage = pygame.image.load("assets/start2.png").convert_alpha()
    else:
        startImage = pygame.image.load("assets/start.png").convert_alpha()
    scaledStartImage = pygame.transform.scale(startImage, (SCREEN_WIDTH / 3, 150))
    screen.blit(scaledStartImage, ((SCREEN_WIDTH / 2 - 300), SCREEN_HEIGHT / 1.5))


# Draws Resolution Buttons
def drawRes():
    mouseX, mouseY = pygame.mouse.get_pos()
    if 322 <= mouseX <= 512 and 341 <= mouseY <= 534:
        image8x8 = pygame.image.load("assets/eight2.png").convert_alpha()
    else:
        image8x8 = pygame.image.load("assets/eight1.png").convert_alpha()
    scaledImage8x8 = pygame.transform.scale(image8x8, (200, 200))
    screen.blit(scaledImage8x8, ((SCREEN_WIDTH / 6), SCREEN_HEIGHT / 2 - 200))
    if 822 <= mouseX <= 1015 and 341 <= mouseY <= 534:
        image16x16 = pygame.image.load("assets/sixteen2.png").convert_alpha()
    else:
        image16x16 = pygame.image.load("assets/sixteen1.png").convert_alpha()
    scaledImage16x16 = pygame.transform.scale(image16x16, (200, 200))
    screen.blit(scaledImage16x16, ((SCREEN_WIDTH / 6 + 500), SCREEN_HEIGHT / 2 - 200))
    if 1320 <= mouseX <= 1501 and 341 <= mouseY <= 534:
        image32x32 = pygame.image.load("assets/thirtytwo2.png").convert_alpha()
    else:
        image32x32 = pygame.image.load("assets/thirtytwo1.png").convert_alpha()
    scaledImage32x32 = pygame.transform.scale(image32x32, (200, 200))
    screen.blit(scaledImage32x32, ((SCREEN_WIDTH / 6 + 1000), SCREEN_HEIGHT / 2 - 200))


# Draws Setting Buttons
def drawSettings():
    mouseX, mouseY = pygame.mouse.get_pos()

    if 322 <= mouseX <= 512 and 341 <= mouseY <= 534:
        image2Player = pygame.image.load("assets/player2a.png").convert_alpha()
    else:
        image2Player = pygame.image.load("assets/player2.png").convert_alpha()

    scaledImage2Player = pygame.transform.scale(image2Player, (200, 200))
    screen.blit(scaledImage2Player, ((SCREEN_WIDTH / 6), SCREEN_HEIGHT / 2 - 200))

    if 822 <= mouseX <= 1015 and 341 <= mouseY <= 534:
        image3Player = pygame.image.load("assets/player3a.png").convert_alpha()
    else:
        image3Player = pygame.image.load("assets/player3.png").convert_alpha()

    scaledImage3Player = pygame.transform.scale(image3Player, (200, 200))
    screen.blit(scaledImage3Player, ((SCREEN_WIDTH / 6 + 500), SCREEN_HEIGHT / 2 - 200))

    if 1320 <= mouseX <= 1501 and 341 <= mouseY <= 534:
        image4Player = pygame.image.load("assets/player4a.png").convert_alpha()
    else:
        image4Player = pygame.image.load("assets/player4.png").convert_alpha()
    scaledImage4Player = pygame.transform.scale(image4Player, (200, 200))
    screen.blit(scaledImage4Player, ((SCREEN_WIDTH / 6 + 1000), SCREEN_HEIGHT / 2 - 200))

    if 700 <= mouseX <= 897 and 810 <= mouseY <= 1008:
        aiImage = pygame.image.load("assets/aia.png").convert_alpha()
    else:   
        aiImage = pygame.image.load("assets/ai.png").convert_alpha()
    scaledAiImage = pygame.transform.scale(aiImage, (200, 200))
    screen.blit(scaledAiImage, (700, 810))

    if 1100 <= mouseX <= 1296 and 810 <= mouseY <= 1008:
        vsImage = pygame.image.load("assets/vsa.png").convert_alpha()
    else:
        vsImage = pygame.image.load("assets/vs.png").convert_alpha()
    scaledVsImage = pygame.transform.scale(vsImage, (200, 200))
    screen.blit(scaledVsImage, (1100, 810))


# Changes Games State According to Inputs
def gameStateChanger(): 
    global gameState
    global NUM_SQUARES
    global FONT_SIZE
    global numOfPlayer
    global gameMode
    global started
    if gameState == "menu":
        if pygame.mouse.get_pressed()[0]:
            mouseX, mouseY = pygame.mouse.get_pos()
            # Check if mouse is on button.
            if 664 <= mouseX <= 1294 and 726 <= mouseY <= 866:
                gameState = "menu2"
    
    elif gameState == "menu2":
        key = pygame.key.get_pressed()
        if key [pygame.K_ESCAPE]:
            gameState = "menu"
        if pygame.mouse.get_pressed()[0]:
            mouseX, mouseY = pygame.mouse.get_pos()
            if 322 <= mouseX <= 512 and 341 <= mouseY <= 534:
                NUM_SQUARES = 8
                gameState = "menu3"
            elif 822 <= mouseX <= 1015 and 341 <= mouseY <= 534:
                NUM_SQUARES = 16
                gameState = "menu3"
            elif 1320 <= mouseX <= 1501 and 341 <= mouseY <= 534:
                NUM_SQUARES = 32
                FONT_SIZE = 20
                gameState = "menu3"
    
    elif gameState == "menu3":
        key = pygame.key.get_pressed()
        if pygame.mouse.get_pressed()[0]:
            mouseX, mouseY = pygame.mouse.get_pos()
            if 322 <= mouseX <= 512 and 341 <= mouseY <= 534:
                numOfPlayer = 2
            elif 822 <= mouseX <= 1015 and 341 <= mouseY <= 534:
                numOfPlayer = 3
            elif 1320 <= mouseX <= 1501 and 341 <= mouseY <= 534:
                numOfPlayer = 4
            if 700 <= mouseX <= 897 and 810 <= mouseY <= 1008:
                gameMode = "ai"
                gameState = "playing"
                started = True
            elif 1100 <= mouseX <= 1296 and 810 <= mouseY <= 1008:
                gameMode = "vs"
                gameState = "playing"
                started = True
                

# Handles Dynamic Square Resolution
def calculateSquareSize(NUM_SQUARES):
    maxSize = (950 - (NUM_SQUARES + 1)) // NUM_SQUARES
    return maxSize


# Draws Squares and Saves Attributes to rectList.
def drawSquares(NUM_SQUARES):
    for i in range(NUM_SQUARES):
        for j in range(NUM_SQUARES):
            x = (i * (calculateSquareSize(NUM_SQUARES) + 1)) + 1
            y = (j * (calculateSquareSize(NUM_SQUARES) + 1)) + 1
            rect = pygame.Rect(x, y, calculateSquareSize(NUM_SQUARES), calculateSquareSize(NUM_SQUARES))
            if len(rectList) <= pow(NUM_SQUARES, 2):
                rectList.append(rect)
            pygame.draw.rect(screen, "white", rect, 1)


# Draws "." to Empty Squares
def drawEmptySquare():
    for i in rectList:
        if rectList.index(i) > 0 and rectList.index(i) not in moveList:
            text = FONT.render(".", True, "white")
            text_rect = text.get_rect(center = i.center)
            screen.blit(text, text_rect)


# Draws GUI Element "Move Box"
def drawMoveBox(num):
    rect = pygame.Rect(1000, 50, 220, 30)
    pygame.draw.rect(screen, "white", rect, 1)
    text = font2.render(f"Square Number:", True, "white")
    screen.blit(text, (1003, 53))
    text = font2.render(f"Square Number: {num}", True, "white")
    screen.blit(text, (1003, 53))

# Draws GUI Element "Warrior Box"
def drawWarriorBox():
    rect = pygame.Rect(1000, 200, 700, 400)
    pygame.draw.rect(screen, ORANGE, rect, 1)
    rect2 = pygame.Rect(1233, 200, 1, 400)
    pygame.draw.rect(screen, ORANGE, rect2, 1)
    rect3 = pygame.Rect(1466, 200, 1, 400)
    pygame.draw.rect(screen, ORANGE, rect3, 1)
    rect4 = pygame.Rect(1000, 400, 700, 1)
    pygame.draw.rect(screen, ORANGE, rect4, 1)
    font = pygame.font.Font(None, 40)
    text = font.render("GUARDIAN", True, ORANGE)
    screen.blit(text, (1040, 290))
    text2 = font.render("ARCHER", True, ORANGE)
    screen.blit(text2, (1293, 290))
    text3 = font.render("ARTILLERYMAN", True, ORANGE)
    screen.blit(text3, (1470, 290))
    text4 = font.render("HORSEMAN", True, ORANGE)
    screen.blit(text4, (1040, 490))
    text5 = font.render("HEALER", True, ORANGE)
    screen.blit(text5, (1293, 490))
    text6 = font.render("PASS", True, ORANGE)
    screen.blit(text6, (1550, 490))

# Chooses Warrior
def chooseWarrior():
    global choosen
    global warrior
    if gameState == "playing":
            if pygame.mouse.get_pressed()[0]:
                mouseX, mouseY = pygame.mouse.get_pos()
                if 1000 <= mouseX <= 1240 and 200 <= mouseY <= 400:
                    #text = font.render("Selected Warrior: Guardian", True, ORANGE)
                    warrior = "Guardian"
                    choosen = True
                elif 1240 <= mouseX <= 1470 and 200 <= mouseY <= 400:
                    #text = font.render("Selected Warrior: Archer", True, ORANGE)
                    warrior = "Archer"
                    choosen = True
                elif 1470 <= mouseX <= 1690 and 200 <= mouseY <= 400:
                    #text = font.render("Selected Warrior: Artilleryman", True, ORANGE)
                    warrior = "Artilleryman"
                    choosen = True
                elif 1000 <= mouseX <= 1240 and 400 <= mouseY <= 600:
                    #text = font.render("Selected Warrior: Horseman", True, ORANGE)
                    warrior = "Horseman"
                    choosen = True
                elif 1240 <= mouseX <= 1470 and 400 <= mouseY <= 600:
                    #text = font.render("Selected Warrior: Healer", True, ORANGE)
                    warrior = "Healer"
                    choosen = True
                elif 1470 <= mouseX <= 1690 and 400 <= mouseY <= 600:
                    #text = font.render("Pass", True, ORANGE)
                    warrior = "Pass"
                    choosen = True
    return warrior


# When Game Starts Draws 1 Guard for Each Player to Random Corner
def drawRandom(NUM_SQUARES):
    global started
    if started == True:
        randomList = [1, NUM_SQUARES, NUM_SQUARES * NUM_SQUARES, NUM_SQUARES * NUM_SQUARES - (NUM_SQUARES - 1)]
        corner1 = random.choice(randomList)
        p1.playerMoveList.append(corner1)
        moveList.append(corner1)
        randomList.remove(corner1)
        corner2 = random.choice(randomList)
        p2.playerMoveList.append(corner2)
        moveList.append(corner2)
        if numOfPlayer > 2:
            randomList.remove(corner2)
            corner3 = random.choice(randomList)
            p3.playerMoveList.append(corner3)
            moveList.append(corner3)
        if numOfPlayer > 3:
            randomList.remove(corner3)
            corner4 = randomList[0]
            p4.playerMoveList.append(corner4)
            moveList.append(corner4)



p1 = Player(RED, 1)
p2 = Player(BLUE, 2)
p3 = Player(GREEN, 3)
p4 = Player(YELLOW, 4)

num = ""
num2 = 0

error = False
error2 = False
error3 = False


# Gameloop
while running:
    gameTime = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if num == "":
                    error3 = True
                    error = False
                    error2 = False
                elif int(num) > pow(NUM_SQUARES, 2):
                    error2 = True
                    error = False
                    error3 = False
                elif int(num) not in moveList:
                    moveList.append(int(num))
                    if playerTurn == "p1":
                        p1.playerMoveList.append(int(num))
                        playerTurn = "p2"
                    if playerTurn == "p2":
                        p2.playerMoveList.append(int(num))
                        if numOfPlayer > 2:
                            playerTurn = "p3"
                        else:
                            playerTurn = "p1"
                    if playerTurn == "p3":
                        p3.playerMoveList.append(int(num))
                        if numOfPlayer > 3:
                            playerTurn = "p4"
                        else:
                            playerTurn = "p1"
                    if playerTurn == "p4":
                        p4.playerMoveList.append(int(num))
                        playerTurn = "p1"


                    error = False
                    error2 = False
                    error3 = False
                    num2 = int(num)
                    #self.playerTurn = False 
                elif int(num) in moveList:
                    error = True
                    error2 = False
                    error3 = False
                num = ""
            elif event.key == pygame.K_BACKSPACE:
                num = num[:-1]
            elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                num += event.unicode

    gameStateChanger()
    FONT = pygame.font.Font(None, FONT_SIZE)
    font2 = pygame.font.Font(None, 30)
    screen.fill("black")

    notEmptyErrorText = font2.render("Square is already filled.", True, "white")
    invalidErrorText = font2.render("Invalid square entered.", True, "white")
    noNumberErrorText = font2.render("No number entered.", True, "white")

    if gameState == "menu":
        screen.blit(scaledMenuImage, (0, 0))
        drawStart()
    
    elif gameState == "menu2":
        drawRes()
        
    elif gameState == "menu3":
        drawSettings() 

    elif gameState == "playing":
        drawSquares(NUM_SQUARES)
        drawEmptySquare()
        drawMoveBox(num)
        drawRandom(NUM_SQUARES)
        started = False
        drawWarriorBox()
        chooseWarrior()

        if error == True:
            screen.blit(notEmptyErrorText, (1000, 143))
        elif error2 == True:
            screen.blit(invalidErrorText, (1000, 143))
        elif error3 == True:
            screen.blit(noNumberErrorText, (1000, 143))

        if choosen == True:
            text = fontUI.render(f"You choose {chooseWarrior()}", True, ORANGE)
            screen.blit(text, (1000, 700))

        p1.drawPlayer(screen, font2, 70, 1000)

        for i in p1.playerMoveList:
            p1.fillSquares(screen, NUM_SQUARES, rectList, i)
            p1.drawText(screen, FONT, rectList, "M1", RED2, i)
        
        if playerTurn == "p1":
            p1.drawPlayerMove(screen, font2, num2)

        if playerTurn == "p2":
            p2.drawPlayerMove(screen, font2, num2)

        for i in p2.playerMoveList:
            p2.fillSquares(screen, NUM_SQUARES, rectList, i)
            p2.drawText(screen, FONT, rectList, "M1", BLUE2, i)

        if numOfPlayer == 2:
            p2.drawPlayer(screen, font2, 1645, 1000)
        elif numOfPlayer == 3:
            p2.drawPlayer(screen, font2, SCREEN_WIDTH / 2 - 100, 1000)
            p3.drawPlayer(screen, font2, 1645, 1000)
            for i in p3.playerMoveList:
                p3.fillSquares(screen, NUM_SQUARES, rectList, i)
                p3.drawText(screen, FONT, rectList, "M1", GREEN2, i)
        elif numOfPlayer == 4:
            p2.drawPlayer(screen, font2, 443, 1000)
            p3.drawPlayer(screen, font2, 816, 1000)
            p4.drawPlayer(screen, font2, 1189, 1000)
            for i in p3.playerMoveList:
                p3.fillSquares(screen, NUM_SQUARES, rectList, i)
                p3.drawText(screen, FONT, rectList, "M1", GREEN2, i)
            for i in p4.playerMoveList:
                p4.fillSquares(screen, NUM_SQUARES, rectList, i)
                p4.drawText(screen, FONT, rectList, "M1", YELLOW2, i)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
