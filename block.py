# import pygame
# # import sys
# from pygame.locals import *
# # from pygame.sprite import _Group
# from const import *
# from utils import *

# # class Block(pygame.sprite.Sprite):
# #     def __init__(self, blockType, pos): # Block() class itself initialization
# #         super().__init__()
# #         # self.image = pygame.image.load("../pygame/pic/yellow.png")
# #         self.image = pygame.image.load(BLOCK_RES[blockType])
# #         self.rect = self.image.get_rect() # image can be considered as object
# #         self.rect.center = pos # object's position

# #     def update(self):
# #         pressed = pygame.key.get_pressed()
# #         if pressed[K_LEFT]:
# #             self.rect.move_ip(-5, 0)
# #         elif pressed[K_RIGHT]:
# #             self.rect.move_ip(5, 0)
# #         elif pressed[K_UP]:
# #             self.rect.move_ip(0, -5)
# #         elif pressed[K_DOWN]:
# #             self.rect.move_ip(0, 5)

# #     def draw(self, surface):
# #         surface.blit(self.image, self.rect)

# class Block(pygame.sprite.Sprite):
#     # def __init__(self, blockType, rowIdx, colIdx, width, height, relPos):
#     #     super().__init__()
#     #     self.blockType = blockType
#     #     self.rowIdx = rowIdx
#     #     self.colIdx = colIdx
#     #     self.width = width
#     #     self.height = height
#     #     self.relPos = relPos
#     #     self.loadImage()
#     #     self.updateImagePos()

#     def __init__(self, blockType, baseRowIdx, baseColIdx, blockShape, blockRot, blockGroupIdx, width, height, relPos):
#         super().__init__()
#         self.blockType = blockType
#         self.blockShape = blockShape
#         self.blockRot = blockRot
#         self.blockGroupIdx = blockGroupIdx
#         self.baseRowIdx = baseRowIdx
#         self.baseColIdx = baseColIdx
#         self.width = width
#         self.height = height
#         self.relPos = relPos
#         self.blink = False
#         self.blinkCount = 0
#         self.loadImage()
#         self.updateImagePos()

#     def setBaseIndex(self, baseRow, baseCol):
#         self.baseRowIdx = baseRow
#         self.baseColIdx = baseCol

#     def getBlockConfigIndex(self):
#         return BLOCK_SHAPE[self.blockShape][self.blockRot][self.blockGroupIdx]
    
#     @property
#     def rowIdx(self):
#         return self.baseRowIdx + self.getBlockConfigIndex()[0]
    
#     @property
#     def colIdx(self):
#         return self.baseColIdx + self.getBlockConfigIndex()[1]

#     def loadImage(self):
#         self.image = pygame.image.load(BLOCK_RES[self.blockType]) # load image
#         self.image = pygame.transform.scale(self.image, (self.width, self.height)) # calibrate image

#     def updateImagePos(self):
#         self.rect = self.image.get_rect() # image can be considered as object
#         self.rect.left = self.relPos[0] + self.width * self.colIdx
#         self.rect.top = self.relPos[1] + self.height * self.rowIdx

#     # def update(self): 
#     #     pressed = pygame.key.get_pressed() # keypresses' logic operation
#     #     if pressed[K_LEFT]:
#     #         self.rect.move_ip(-1, 0)
#     #     elif pressed[K_RIGHT]:
#     #         self.rect.move_ip(1, 0)
#     #     elif pressed[K_UP]:
#     #         self.rect.move_ip(0, -1)
#     #     elif pressed[K_DOWN]:
#     #         self.rect.move_ip(0, 1)

#     def isLeftBound(self):
#         return self.colIdx == 0
    
#     def isRightBound(self):
#         return self.colIdx == GAME_COL - 1
    
#     def doLeft(self):
#         self.colIdx -= 1
    
#     def doRight(self):
#         self.colIdx += 1

#     def draw(self, surface):
#         self.updateImagePos()
#         if self.blink and self.blinkCount % 2 == 0:
#             return
#         surface.blit(self.image, self.rect) # rendering image and object

#     def drop(self):
#         self.rowIdx += 1 # drop operation self.rowIdx = self.rowIdx + 1
#         # self.updateImagePos()

#     def getIndex(self):
#         return (int(self.rowIdx), int(self.colIdx))
    
#     def getNextIndex(self):
#         return (int(self.rowIdx + 1), int(self.colIdx))
    
#     def doRotate(self):
#         self.blockRot += 1
#         if self.blockRot >= len(BLOCK_SHAPE[self.blockShape]):
#             self.blockRot = 0

#     def startBlink(self):
#         self.blink = True
#         self.blinkTime = getCurrentTime()

#     def update(self):
#         if self.blink:
#             diffTime = getCurrentTime() - self.blinkTime
#             self.blinkCount = int(diffTime / 30)

import pygame, sys
from pygame.locals import *
from utils import *

import const

class Block(pygame.sprite.Sprite):
    def __init__(self, blockType, baseRowIdx, baseColIdx, blockShape, blockRot, blockGroupIdx, width, height, relPos):
        super().__init__() 
        self.blockType = blockType
        self.blockShape = blockShape
        self.blockRot = blockRot
        self.blockGroupIdx = blockGroupIdx
        self.baseRowIdx = baseRowIdx
        self.baseColIdx = baseColIdx
        self.width = width
        self.height = height
        self.relPos = relPos
        self.blink = False
        self.blinkCount = 0
        self.hasShadow = False
        self.loadImage()
        self.updateImagePos()
    
    def loadImage(self):
        self.image = pygame.image.load( const.BLOCK_RES[self.blockType] )
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
    
    def updateImagePos(self):
        self.rect = self.image.get_rect()
        self.rect.left = self.relPos[0] + self.width * self.colIdx
        self.rect.top = self.relPos[1] + self.height * self.rowIdx
    
    def setBaseIndex(self, baseRow, baseCol):
        self.baseRowIdx = baseRow
        self.baseColIdx = baseCol
    
    def getBlockConfigIndex(self):
        return const.BLOCK_SHAPE[self.blockShape][self.blockRot][self.blockGroupIdx]
    
    def doRotate(self):
        self.blockRot += 1
        if self.blockRot >= len(const.BLOCK_SHAPE[self.blockShape]):
            self.blockRot = 0
    
    @property
    def rowIdx(self):
        return self.baseRowIdx + self.getBlockConfigIndex()[0]
    
    @property
    def colIdx(self):
        return self.baseColIdx + self.getBlockConfigIndex()[1]
    
    def getIndex(self):
        return (int(self.rowIdx), int(self.colIdx))

    def getNextIndex(self):
        return (int(self.rowIdx + 1), int(self.colIdx))

    def drop(self):
        self.baseRowIdx += 1
    
    def isLeftBound(self):
        return self.colIdx == 0

    def isRightBound(self):
        return self.colIdx == const.GAME_COL - 1

    def doLeft(self):
        self.baseColIdx -= 1

    def doRight(self):
        self.baseColIdx += 1
    
    def setShadow(self, b):
        self.hasShadow = b

    def startBlink(self):
        self.blink = True
        self.blinkTime = getCurrentTime()

    
    def update(self):
        if self.blink:
            diffTime = getCurrentTime() - self.blinkTime
            self.blinkCount = int(diffTime / 30)

    def drawSelf(self, surface):
        surface.blit(self.image, self.rect)

    def draw(self, surface):
        self.updateImagePos()
        if self.blink and self.blinkCount % 2 == 0:
            return
        self.drawSelf(surface)