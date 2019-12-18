import pygame
import time
from network import Network

pygame.init()

width = 1000
height = 200

horseRun = [pygame.image.load('at1.png'), pygame.image.load('at2.png'), pygame.image.load('at3.png'), pygame.image.load('at4.png'), pygame.image.load('at5.png'), pygame.image.load('at6.png'), pygame.image.load('at7.png'), pygame.image.load('at8.png'), pygame.image.load('at9.png'), pygame.image.load('at10.png'), pygame.image.load('at11.png'), pygame.image.load('at12.png'), pygame.image.load('at13.png'), pygame.image.load('at14.png'), pygame.image.load('at15.png')]


win = pygame.display.set_mode((width,height))
pygame.display.set_caption("At Yarışı-1")
clientNumber = 0


class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.horse = (x, y, width, height)
        self.vel = 5
        self.walkCount = 0
        self.isJump = False
        self.jumpCount = 7

    def draw(self, win):

        if self.walkCount + 1 >= 150:
            self.walkCount = 0
        win.blit(horseRun[self.walkCount // 15], (self.x, self.y))

    def drawp2(self, win):

        if self.walkCount+1 >= 150:
            self.walkCount = 0
        win.blit(horseRun[self.walkCount // 15], (self.x, self.y))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]and self.x < width - 75:
            self.walkCount += 6
            self.x += self.vel


        if keys[pygame.K_SPACE] and self.isJump == False and self.x < width-75:
            self.walkCount += 2
            self.x += 5
            self.y -= self.vel + 5
            self.isJump = True


        elif self.isJump == True:
            time.sleep(0.075)
            self.walkCount += 2
            self.x += 5
            self.y += self.vel + 5
            self.isJump = False

        self.update()

    def update(self):
        self.horse = (self.x, self.y, self.width, self.height)


def read_pos(str):
    str = str.split(",")
    return (int(str[0]), int(str[1]))


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(win, player, player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.drawp2(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(startPos[0], startPos[1], 0, 100)
    p2 = Player(0, 0, 0, 100)
    clock = pygame.time.Clock()


    while run:

        clock.tick(60)
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win, p2, p)


main()