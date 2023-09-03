# import random
# # import pygame, sys
# from pygame.locals import *
# from const import *
# from block import *
# from utils import *

# class BlockGroup(object):
#     # def __init__(self, width, height, blockConfigList, relPos):
#     #     super().__init__()
#     #     self.blocks = []
#     #     for config in blockConfigList:
#     #         blk = Block(config['blockType'], config['rowIdx'], config['colIdx'], width, height, relPos)
#     #         self.blocks.append(blk)

#     def __init__(self, blockGroupType, width, height, blockConfigList, relPos):
#         super().__init__()
#         self.blocks = []
#         self.blockGroupType = blockGroupType
#         self.time = 0
#         self.eliminateTime = 0
#         self.dropInterval = 0 # time interval for dropping operation
#         for config in blockConfigList:
#             blk = Block(config['blockType'], config['rowIdx'], config['colIdx'], config['blockShape'], config['blockRot'], config['blockGroupIdx'], width, height, relPos)
#             self.blocks.append(blk)

#     def setBaseIndexes(self, baseRow, baseCol):
#         for blk in self.blocks:
#             blk.setBaseIndex(baseRow, baseCol)

#     # def GenerateBlockGroupConfig(rowIdx, colIdx): # generate random block group
#     #     idx = random.randint(0, len(BLOCK_SHAPE) - 1)
#     #     bType = random.randint(0, BlockType.BLOCKMAX - 1)
#     #     configList = []
#     #     for x in range(len(BLOCK_SHAPE[idx])):
#     #         config = {
#     #             'blockType' : bType,
#     #             'rowIdx' : rowIdx + BLOCK_SHAPE[idx][x][0],
#     #             'colIdx' : colIdx + BLOCK_SHAPE[idx][x][1]
#     #         }
#     #         configList.append(config)
#     #     return configList
    
#     def GenerateBlockGroupConfig(rowIdx, colIdx): # generate block group configuration
#         shapeIdx = random.randint(0, len(BLOCK_SHAPE) - 1)
#         bType = random.randint(0, BlockType.BLOCKMAX - 1)
#         configList = []
#         rotIdx = 0
#         for i in range(len(BLOCK_SHAPE[shapeIdx][rotIdx])):
#             config = {
#                 'blockType' : bType,
#                 'blockShape' : shapeIdx,
#                 'blockRot' : rotIdx,
#                 'blockGroupIdx' : i,
#                 'rowIdx' : rowIdx,
#                 'colIdx' : colIdx
#             }
#             configList.append(config)
#         return configList
    
#     def draw(self, surface):
#         for b in self.blocks:
#             b.draw(surface) # rendering

#     # def update(self):
#     #     self.time += 1
#     #     if self.time >= 1000:
#     #         self.time = 0
#     #         for b in self.blocks:
#     #             b.drop()

#     def update(self):
#         # self.time += 1
#         oldTime = self.time
#         curTime = getCurrentTime()
#         diffTime = curTime - oldTime
#         if self.blockGroupType == BlockGroupType.DROP: # dropping blocks will start timing operation
#             # if self.time >= 1000:
#             #     self.time = 0 # reset timer
#             #     for b in self.blocks:
#             #         b.drop() # drop operation
#             if diffTime >= 300: # time interval judges dropping operation
#                 self.time = curTime
#                 for b in self.blocks:
#                     b.drop() # drop operation
#             self.keyDownHandler()

#             for blk in self.blocks:
#                 blk.update()
        
#         if self.isEliminating(): # eliminating status
#             if getCurrentTime() - self.eliminateTime > 500: # time interval judges
#                 tmpBlocks = []
#                 for blk in self.blocks:
#                     if blk.getIndex()[0] != self.eliminateRow: # not in eliminate row
#                         if blk.getIndex()[0] < self.eliminateRow:
#                             blk.drop() # drop after the row has been eliminated
#                         tmpBlocks.append(blk)
#                 self.blocks = tmpBlocks
#                 self.setEliminate(False)

#     def getBlockIndexes(self):
#         return [block.getIndex() for block in self.blocks]
    
#     def getNextBlockIndexes(self):
#         return [block.getNextIndex() for block in self.blocks]
    
#     def getBlocks(self):
#         return self.blocks
    
#     def clearBlocks(self):
#         self.blocks = []

#     def addBlocks(self, blk):
#         self.blocks.append(blk)

#     def keyDownHandler(self): # key presses' control 
#         pressed = pygame.key.get_pressed()
#         if pressed[K_LEFT] and self.checkAndSetPressTime(K_LEFT):
#             b = True
#             for blk in self.blocks:
#                 if blk.isLeftBound():
#                     b = False
#                     break
#             if b:
#                 for blk in self.blocks:
#                     blk.doLeft()
#         elif pressed[K_RIGHT] and self.checkAndSetPressTime(K_RIGHT):
#             b = True
#             for blk in self.blocks:
#                 if blk.isRightBound():
#                     b = False
#                     break
#             if b:
#                 for blk in self.blocks:
#                     blk.doRight()

#         if pressed[K_DOWN]: # increase dropping speed by reducing time interval
#             self.dropInterval = 30
#         else:
#             self.dropInterval = 800

#         if pressed[K_UP] and self.checkAndSetPressTime(K_UP): # rotate blocks
#             for blk in self.blocks:
#                 blk.doRotate()

#     def doEliminate(self, row):
#         eliminateRow = {}

#         for col in range(0, GAME_COL):
#             idx = (row, col)
#             eliminateRow[idx] = 1
#         self.setEliminate(True)
#         self.eliminateRow = row

#         for blk in self.blocks:
#             if eliminateRow.get(blk.getIndex()): # eliminateRow get blocks' indexes
#                 blk.startBlink()

#     def processEliminate(self):
#         hash = {}

#         allIndexes = self.getBlockIndexes()
#         for idx in allIndexes:
#             hash[idx] = 1 # mapping all indexes into hash table

#         for row in range(GAME_ROW-1, -1, -1): # from top to bottom
#             full = True
#             for col in range(0, GAME_COL): # from bottom to top
#                 idx = (row, col)
#                 if not hash.get(idx): # there is no index in hash table
#                     full = False
#                     break
#             if full:
#                 self.doEliminate(row)
#                 return
            
#     def setEliminate(self, bEl):
#         self.isEliminating = bEl
#         self.eliminateTime = getCurrentTime()

#     def isEliminating(self):
#         return self.isEliminating

import random
import pygame, sys
from pygame.locals import *
from block import *
from utils import *

import const

class BlockGroup(object):
    def GenerateBlockGroupConfig(rowIdx, colIdx, shapeIdx = -1):
        if shapeIdx == -1:
            shapeIdx = random.randint(0, len(const.BLOCK_SHAPE)-1 )
        bType = random.randint(0, const.BlockType.BLOCKMAX-1 )
        configList = []
        rotIdx = 0
        for i in range( len( const.BLOCK_SHAPE[shapeIdx][rotIdx] ) ):
            config = {
                'blockType' : bType,
                'blockShape' : shapeIdx,
                'blockRot' : rotIdx,
                'blockGroupIdx' : i, 
                'rowIdx' : rowIdx,
                'colIdx' : colIdx
            }
            configList.append(config)
        return configList

    def __init__(self, blockGroupType, width, height, blockConfigList, relPos):
        super().__init__() 
        self.blocks = []
        self.blockGroupType = blockGroupType
        self.dropTime = getCurrentTime()
        self.dropInterval = 0
        self.pressTime = {}
        self.isEliminating = False
        self.eliminateRow = 0
        self.eliminateTime = 0
        for config in blockConfigList:
            blk = Block(config['blockType'], config['rowIdx'], config['colIdx'], config['blockShape'], config['blockRot'], config['blockGroupIdx'], width, height, relPos)
            self.blocks.append(blk)
        
    def setBaseIndexes(self, baseRow, baseCol):
        for blk in self.blocks:
            blk.setBaseIndex(baseRow, baseCol)
    
    def getBlockIndexes(self):
        return [block.getIndex()  for block in self.blocks]
    
    def getNextBlockIndexes(self):
        return [block.getNextIndex()  for block in self.blocks]
    
    def draw(self, surface):
        for b in self.blocks:
            b.draw(surface)
    
    def getBlocks(self):
        return self.blocks

    def clearBlocks(self):
        self.blocks = []
    
    def addBlocks(self, blk ):
        self.blocks.append( blk )
    
    def checkAndSetPressTime(self, key):
        ret = False
        if getCurrentTime() - self.pressTime.get(key, 0) > 150:
            ret = True
            self.pressTime[key] = getCurrentTime()
        return ret
    
    def keyDownHandler(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT] and self.checkAndSetPressTime(K_LEFT):
            b = True
            for blk in self.blocks:
                if blk.isLeftBound():
                    b = False
                    break
            if b:
                for blk in self.blocks:
                    blk.doLeft()
        
        if pressed[K_RIGHT] and self.checkAndSetPressTime(K_RIGHT):
            b = True
            for blk in self.blocks:
                if blk.isRightBound():
                    b = False
                    break
            if b:
                for blk in self.blocks:
                    blk.doRight()   
        
        if pressed[K_UP] and self.checkAndSetPressTime(K_UP):
            for blk in self.blocks:
                blk.doRotate()  
        
        if pressed[K_DOWN]:
            self.dropInterval = 30
        else:
            self.dropInterval = 1000
        
        if self.blockGroupType == const.BlockGroupType.DROP:
            for blk in self.blocks:
                blk.setShadow( pressed[K_DOWN] )  
    
    def update(self):
        oldTime = self.dropTime
        curTime = getCurrentTime()
        diffTime = curTime - oldTime
        if self.blockGroupType == const.BlockGroupType.DROP:
            if diffTime >= self.dropInterval:
                self.dropTime = curTime
                for b in self.blocks:
                    b.drop()
            self.keyDownHandler()
        
        for blk in self.blocks:
            blk.update()

        if self.IsEliminating():
            if getCurrentTime() - self.eliminateTime > 500:
                tmpBlocks = []
                for blk in self.blocks:
                    if blk.getIndex()[0] != self.eliminateRow:
                        if blk.getIndex()[0] < self.eliminateRow:
                            blk.drop()
                        tmpBlocks.append( blk )
                self.blocks = tmpBlocks
                self.setEliminate(False)


    def doEliminate(self, row):
        eliminateRow = {}
        for col in range(0, GAME_COL):
            idx = (row, col)
            eliminateRow[idx] = 1
        self.setEliminate(True)
        self.eliminateRow = row        
        
        for blk in self.blocks:
            if eliminateRow.get( blk.getIndex() ):
                blk.startBlink()

    def processEliminate(self):
        hash = {}
        
        allIndexes = self.getBlockIndexes()
        for idx in allIndexes:
            hash[idx] = 1
        
        for row in range(const.GAME_ROW-1, -1, -1):
            full = True
            for col in range(0, const.GAME_COL):
                idx = (row, col)
                if not hash.get(idx):
                    full = False
                    break
            if full:
                self.doEliminate(row)
                return True
    
    def setEliminate(self, bEl):
        self.isEliminating = bEl
        self.eliminateTime = getCurrentTime()
    
    def IsEliminating(self):
        return self.isEliminating
    