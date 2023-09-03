GAME_WIDTH_SIZE = 800
GAME_HEIGHT_SIZE = 600

class BlockType:
    RED = 0
    ORANGE = 1
    YELLOW = 2
    GREEN = 3
    CYAN = 4
    BLUE = 5
    PURPLE = 6
    BLOCKMAX = 7

BLOCK_RES = {
    BlockType.RED : "../pygame/pic/red.png",
    BlockType.ORANGE: "../pygame/pic/orange.png",
    BlockType.YELLOW: "../pygame/pic/yellow.png",
    BlockType.GREEN: "../pygame/pic/green.png",
    BlockType.CYAN: "../pygame/pic/cyan.png",
    BlockType.BLUE: "../pygame/pic/blue.png",
    BlockType.PURPLE: "../pygame/pic/purple.png",
}

GAME_ROW = 17 # y-axis / vertical
GAME_COL = 10 # x-axis / horizontal

# BLOCK_SHAPE = [
#     [(0, 0), (0, 1), (1, 0), (1, 1)], # square shape
#     [(0, 0), (0, 1), (0, 2), (0, 3)], # rectangle shape
#     [(0, 0), (0, 1), (1, 1), (1, 2)], # z shape
#     [(0, 1), (1, 0), (1, 1), (1, 2)], # airplane shape
# ]

BLOCK_SHAPE = [
    [((0, 0), (0, 1), (1, 0), (1, 1)), ], # square
    [((0, 0), (0, 1), (0, 2), (0, 3)), ((0, 0), (1, 0), (2, 0), (3, 0))], # rectangle
    [((0, 0), (0, 1), (1, 1), (1, 2)), ((0, 1), (1, 0), (1, 1), (2, 0))], # z
    [((0, 1), (1, 0), (1, 1), (1, 2)),((0, 1), (1, 1), (1, 2), (2, 1)),
    ((1, 0), (1, 1), (1, 2), (2, 1)),((0, 1), (1, 0), (1, 1), (2, 1))], # airplane
]

class BlockGroupType:
    FIXED = 0
    DROP = 1

BLOCK_SIZE_W = 32 # width
BLOCK_SIZE_H = 32 # height
