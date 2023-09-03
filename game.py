# # from typing import Any
# import pygame
# # import sys

# # from pygame.sprite import _Group
# from blockGroup import *
# from const import *

# class Game(pygame.sprite.Sprite):
#     def getRelPos(self):
#         return (240, 50)
    
#     def __init__(self, surface):
#         self.surface = surface
#         self.fixedBlockGroup = BlockGroup(BlockGroupType.FIXED, BLOCK_SIZE_W, BLOCK_SIZE_H, [], self.getRelPos())
#         self.dropBlockGroup = None
#         self.gameOverImage = pygame.image.load("../pygame/pic/lose.png")
#         self.isGameOver = False
#         self.font = pygame.font.Font(None, 60)
#         self.score = 0
#         self.nextBlockGroup = None
#         self.generateNextBlockGroup()

#     def setBaseIndexes(self, baseRow, baseCol):
#         for blk in self.blocks:
#             blk.setBaseIndex(baseRow, baseCol)

#     def generateNextBlockGroup(self):
#         conf = BlockGroup.GenerateBlockGroupConfig(0, GAME_COL + 3)
#         self.nextBlockGroup = BlockGroup(BlockGroupType.DROP, BLOCK_SIZE_W, BLOCK_SIZE_H, conf, self.getRelPos())
    
#     def generateDropBlockGroup(self):
#         # conf = BlockGroup.GenerateBlockGroupConfig(0, GAME_COL/2 - 1)
#         # self.dropBlockGroup = BlockGroup(BlockGroupType.DROP, BLOCK_SIZE_W, BLOCK_SIZE_H, conf, self.getRelPos())
#         self.dropBlockGroup = self.nextBlockGroup
#         self.dropBlockGroup.setBaseIndexes(0, GAME_COL/2 - 1)
#         self.generateNextBlockGroup()

#     # def update(self):
#     #     pass

#     # def draw(self):
#     #     pass

#     # def update(self): # keypress ,timing and collision operation
#     #     self.fixedBlockGroup.update()
#     #     if self.dropBlockGroup:
#     #         self.dropBlockGroup.update()
#     #     else:
#     #         self.generateDropBlockGroup()
#     #     if self.willCollide():
#     #         blocks = self.dropBlockGroup.getBlocks()
#     #         for blk in blocks:
#     #             self.fixedBlockGroup.addBlocks(blk) # dropping blocks will be combined with fixed blocks
#     #         self.dropBlockGroup.clearBlocks() # reset dropping blocks
#     #         self.dropBlockGroup = None # reset dropping blocks
#     #     if self.fixedBlockGroup.processEliminate():
#     #         self.score += 1

#     #     if self.fixedBlockGroup.isEliminating(): # blink: fixed block group is eliminating
#     #         return
#     #     if self.isGameOver:
#     #         return
#     #     self.checkGameOver()
#     def update(self):
#         if self.isGameOver:
#             return 
        
#         self.fixedBlockGroup.update()

#         if self.fixedBlockGroup.isEliminating():
#             return

#         if self.dropBlockGroup:
#             self.dropBlockGroup.update()
#         else:
#             self.generateDropBlockGroup()
        
#         if self.willCollide():
#             blocks = self.dropBlockGroup.getBlocks()
#             for blk in blocks:
#                 self.fixedBlockGroup.addBlocks(blk)
#             self.dropBlockGroup.clearBlocks()
#             self.dropBlockGroup = None
#             if self.fixedBlockGroup.processEliminate():
#                 self.score += 1
        
#         self.checkGameOver()

#     def checkGameOver(self):
#         allIndexes = self.fixedBlockGroup.getBlockIndexes()
#         for idx in allIndexes:
#             if idx[0] < 2:
#                 self.isGameOver = True

#     def draw(self): # rendering operation
#         self.fixedBlockGroup.draw(self.surface)
#         if self.dropBlockGroup:
#             self.dropBlockGroup.draw(self.surface)
#         self.nextBlockGroup.draw(self.surface)
#         if self.isGameOver(): # checking game is over or not
#             rect = self.gameOverImage.get_rect()
#             rect.centerx = GAME_WIDTH_SIZE / 2
#             rect.centery = GAME_HEIGHT_SIZE / 2
#             self.surface.blit(self.gameOverImage, rect) # show game over image
#         textImage = self.font.render('Score: ' + str(self.score), True, (255, 255, 255))
#         self.surface.blit(textImage, (10, 20))

#     def willCollide(self): # checking block will collide or not (drop BlockGroup and fixed BlockGroup)
#         hash = {}
#         allIndexes = self.fixedBlockGroup.getBlockIndexes()
#         for idx in allIndexes:
#             hash[idx] = 1 # mapping fixed blocks' indexes to hash table
#         dropIndexes = self.dropBlockGroup.getNextBlockIndexes()
#         for dropIdx in dropIndexes:
#             if hash.get(dropIdx): # future index matches hash table
#                 return True
#             if dropIdx[0] >= GAME_ROW: # future index collides with GAME_ROW
#                 return True
#         return False

import pygame, sys
from pygame.locals import *
from blockGroup import *
import const

class Game(pygame.sprite.Sprite):
    def getRelPos(self):
        return (240, 50)

    def __init__(self, surface):
        self.font = pygame.font.Font(None, 60)
        self.score = 0
        self.surface = surface
        self.gameOverImage = pygame.image.load( "../pygame/pic/lose.png" )
        self.isGameOver = False
        self.fixedBlockGroup = BlockGroup(const.BlockGroupType.FIXED, const.BLOCK_SIZE_W, const.BLOCK_SIZE_H, [], self.getRelPos())
        self.dropBlockGroup = None
        self.nextBlockGroup = None
        self.generateNextBlockGroup()

    def generateDropBlockGroup(self):
        self.dropBlockGroup = self.nextBlockGroup
        self.dropBlockGroup.setBaseIndexes(0, const.GAME_COL/2-1)
        self.generateNextBlockGroup()
    
    def generateNextBlockGroup(self):
        conf = BlockGroup.GenerateBlockGroupConfig(0, const.GAME_COL + 3)
        self.nextBlockGroup = BlockGroup(const.BlockGroupType.DROP, const.BLOCK_SIZE_W, const.BLOCK_SIZE_H, conf, self.getRelPos())

    def willCollide(self):
        hash = {}
        allIndexes = self.fixedBlockGroup.getBlockIndexes()
        for idx in allIndexes:
            hash[idx] = 1
        dropIndexes = self.dropBlockGroup.getNextBlockIndexes()

        for dropIdex in dropIndexes:
            if hash.get(dropIdex):
                return True
            if dropIdex[0] >= const.GAME_ROW:
                return True
        return False


    def update(self):
        if self.isGameOver:
            return 
        
        self.fixedBlockGroup.update()

        if self.fixedBlockGroup.IsEliminating():
            return

        if self.dropBlockGroup:
            self.dropBlockGroup.update()
        else:
            self.generateDropBlockGroup()
        
        if self.willCollide():
            blocks = self.dropBlockGroup.getBlocks()
            for blk in blocks:
                self.fixedBlockGroup.addBlocks(blk)
            self.dropBlockGroup.clearBlocks()
            self.dropBlockGroup = None
            if self.fixedBlockGroup.processEliminate():
                self.score += 1
        
        self.checkGameOver()

    def checkGameOver(self):
        allIndexes = self.fixedBlockGroup.getBlockIndexes()
        for idx in allIndexes:
            if idx[0] < 2:
                self.isGameOver = True


    def draw(self):
        self.fixedBlockGroup.draw(self.surface)
        if self.dropBlockGroup:
            self.dropBlockGroup.draw(self.surface)
        self.nextBlockGroup.draw(self.surface)
        
        if self.isGameOver:
            rect = self.gameOverImage.get_rect()
            rect.centerx = const.GAME_WIDTH_SIZE/2
            rect.centery = const.GAME_HEIGHT_SIZE/2
            self.surface.blit(self.gameOverImage, rect)

        textImage = self.font.render('Score: ' + str(self.score), True, (255,255,255))
        self.surface.blit(textImage, (10, 20))