from tiles import *
from spritesheet import Spritesheet
import pygame
import pkg_resources


#must include ^^^ in any pygame python file
#allows acces to files withing project folder omg this was too hard to find
pygame.init()
pygame.display.init()
FramePerSec = pygame.time.Clock()
win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("PinkBunny")

#Pre game related^^^^^
##############################################################################
walkRight = [pygame.image.load('RunningR1.png'), pygame.image.load('RunningR2.png'), pygame.image.load('RunningR3.png'), pygame.image.load('RunningL5.png')]
walkLeft = [pygame.image.load('RunningL1.png'), pygame.image.load('RunningL2.png'), pygame.image.load('RunningL3.png'), pygame.image.load('RunningL4.png'), pygame.image.load('RunningL5.png')]
#bg = pygame.image.load('PrpleBlok.png')
char = pygame.image.load('Idle1.png')
############################Chanracter animation^#############################
clock = pygame.time.Clock()
DISPLAY_W, DISPLAY_H = 480, 270
canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))

spritesheet = Spritesheet('Floor.png')
map = TileMap('level1.csv', spritesheet)


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self, win):
        if self.walkCount + 1 >= 13:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))


def redrawGameWindow():
    man.draw(win)
    pygame.display.update()
# mainloop
man = player(map.start_x, map.start_y, 32, 32)


run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_d] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0

    if not (man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10


    map.draw_map(win)
    redrawGameWindow()
    pygame.display.update()
pygame.quit()