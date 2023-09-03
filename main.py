# from typing import Any
import pygame, sys, const
from pygame.locals import *
# from const import *
# from block import *
# from blockGroup import *
from game import *
# import random

# from pygame.sprite import _Group

pygame.init() # pygame library initialization
DISPLAYSURF = pygame.display.set_mode((800, 600)) # set 800 x 600 window

game = Game(DISPLAYSURF)
# Image = pygame.image.load("../pygame/pic/yellow.png")
# Rect = Image.get_rect()
# Rect.center = (400, 300)

# B = Block()
# P = Block(BlockType.PURPLE, (200, 300))
# C = Block(BlockType.CYAN, (600, 300))

# blocks = [] # 2-dimensional array

# for i in range(GAME_ROW):
#     b = []
#     for j in range(GAME_COL):
#         b.append(Block(random.randint(0, BlockType.BLOCKMAX - 1), i, j, 32, 32, (240, 50)))

# blocks.append(b)

# blockGroups = []

# for x in range(5):
#     conf = BlockGroup.GenerateBlockGroupConfig(x * 4, x)
#     blockGroups.append(BlockGroup(32, 32, conf, (240, 50)))

# main loop
while True:
    for event in pygame.event.get():
        # --------------------
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # --------------------
        # pressed = pygame.key.get_pressed()
        # if pressed[K_LEFT]:
        #     Rect.move_ip(-5, 0) # move in place
        # elif pressed[K_RIGHT]:
        #     Rect.move_ip(5, 0) # move in place
        # elif pressed[K_UP]:
        #     Rect.move_ip(0, -5) # move in place
        # elif pressed[K_DOWN]:
        #     Rect.move_ip(0, 5) # move in place
        # --------------------
        # B.update()
        # P.update()
        # C.update()
        # --------------------
        # for i in range(GAME_ROW):
        #     for j in range(GAME_COL):
        #         blocks[i][j].update() # blocks' keypresses update
        # --------------------
        # for i in range(GAME_ROW):
        #     for j in range(GAME_COL):
        #         blockGroups[i][j].update() # blockGroups' keypresses update
        # --------------------
        game.update() # logic operation
        # --------------------
        DISPLAYSURF.fill((0, 0, 0)) # wipe out rendering before each keypress update
        # DISPLAYSURF.blit(Image, Rect) # display image
        # Rect.centerx += random.randint(-5, 5) # Rect.centerx = Rect.centerx + random.randint(-1, 1)
        # --------------------
        # B.draw(DISPLAYSURF)
        # P.draw(DISPLAYSURF)
        # C.draw(DISPLAYSURF)
        # --------------------
        # for i in range(GAME_ROW):
        #     for j in range(GAME_COL):
        #         blocks[i][j].draw(DISPLAYSURF) # rendering window
        # --------------------
        # for bg in blockGroups:
        #     bg.draw(DISPLAYSURF) # rendering window
        # --------------------
        game.draw() # rendering operation
        # --------------------
        pygame.display.update() # final pygame display update
