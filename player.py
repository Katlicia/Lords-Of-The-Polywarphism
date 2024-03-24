import pygame

class Player:
    def __init__(self, color, playerNum):
        self.resource = 200
        self.alive = True
        self.color = color
        self.playerNum = playerNum
        self.playerMoveList = []
        self.warrior = 1

    def fillSquares(self, screen, NUM_SQUARES, rectList, num):
        if num != 0:
            #pygame.draw.rect(screen, self.color, rectList[squareNum])
            if num % NUM_SQUARES != 1:
                pygame.draw.rect(screen, self.color, rectList[num - 1])
                if num > NUM_SQUARES:
                    pygame.draw.rect(screen, self.color, rectList[num - NUM_SQUARES])
                    pygame.draw.rect(screen, self.color, rectList[num - NUM_SQUARES - 1])
            
            if num > NUM_SQUARES:
                pygame.draw.rect(screen, self.color, rectList[num - NUM_SQUARES])

            if num % NUM_SQUARES != 0:
                if num > NUM_SQUARES:
                    pygame.draw.rect(screen, self.color, rectList[num - NUM_SQUARES + 1])
                    if num != NUM_SQUARES + 1 and num % NUM_SQUARES != 1:
                        pygame.draw.rect(screen, self.color, rectList[num - NUM_SQUARES - 1])
                pygame.draw.rect(screen, self.color, rectList[num + 1])
                if num <= NUM_SQUARES * (NUM_SQUARES - 1):
                    pygame.draw.rect(screen, self.color, rectList[num + NUM_SQUARES + 1])
            if num <= NUM_SQUARES * (NUM_SQUARES - 1):
                pygame.draw.rect(screen, self.color, rectList[num + NUM_SQUARES])
                if num % NUM_SQUARES != 1:
                    pygame.draw.rect(screen, self.color, rectList[num + NUM_SQUARES - 1])

    def drawText(self, screen, FONT, rectList,text, color, num):
        text = FONT.render(text, True, color)
        if num != 0:
            text_rect = text.get_rect(center = rectList[num].center)
            screen.blit(text, text_rect)
    
    def drawPlayerMove(self, screen, FONT, num):
        text = FONT.render(f"Player{self.playerNum} moved to {num}.", True, "white")
        if num != 0:
            screen.blit(text, (1000, 100))
            self.warrior += 1

    def drawPlayer(self, screen, FONT, x, y):
        rect = pygame.Rect(x, y, 200, 50)
        pygame.draw.circle(screen, self.color,(x - 30, y + 25), 25)
        pygame.draw.rect(screen, self.color, rect, 1)
        text = FONT.render(f"Player{self.playerNum}: {self.resource}", True, "white")
        text_rect = text.get_rect(center = rect.center)
        screen.blit(text, text_rect)    
