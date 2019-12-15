import model
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import copy
import pprint
import random
import pathfinding


def distance_sqr(a, b):
     return (a.x - b.x) ** 2 + (a.y - b.y) ** 2

def one_step_to(game, unit, target_position):

    tiles = game.level.tiles

    len_x = len(game.level.tiles)
    len_y = len(game.level.tiles[0])

    my_map = copy.deepcopy(tiles)

    for x in range(len_x):
        for y in reversed(range(len_y)):
            my_map[x][y] = 0
            if tiles[x][y] == model.Tile.LADDER or tiles[x][y] == model.Tile.PLATFORM:
                my_map[x][y] = 3
                if tiles[x][y+1] == model.Tile.EMPTY:
                    my_map[x][y+1] = 3
            if tiles[x][y] == model.Tile.EMPTY and tiles[x][y - 1] == model.Tile.WALL:
                my_map[x][y] = 3
            if tiles[x][y] == model.Tile.EMPTY and tiles[x][y - 2] == model.Tile.WALL:
                my_map[x][y] = 9
            if tiles[x][y] == model.Tile.EMPTY and tiles[x][y - 3] == model.Tile.WALL:
                my_map[x][y] = 9

    for x in range(len_x):
        for y in range(len_y):
            if tiles[x][y] == model.Tile.JUMP_PAD:
                for i in range(10):
                    if (y+i) < len_y and my_map[x][y+i] == 0:
                        my_map[x][y+i] = 1
 
    for x in range(len_x):
        for y in reversed(range(len_y)):
            if my_map[x][y] == 3:
                if tiles[x-1][y] == model.Tile.EMPTY:
                    my_map[x-1][y] = 9
#                if x > 1 and tiles[x-2][y] == model.Tile.EMPTY:
#                    my_map[x-2][y] = 3


    for x in reversed(range(len_x)):
        for y in reversed(range(len_y)):
            if my_map[x][y] == 3:
                if tiles[x+1][y] == model.Tile.EMPTY:
                    my_map[x+1][y] = 9
#                if x < (len_x - 2) and tiles[x+2][y] == model.Tile.EMPTY:
#                    my_map[x+2][y] = 3

    # fall down
    for y in reversed(range(len_y)):
        for x in range(len_x):
            if my_map[x][y] > 0:
                y1 = y - 1
                while y1 >= 0 and tiles[x][y1] == model.Tile.EMPTY:
                    if my_map[x][y1] == 0:
                        my_map[x][y1] = 9
                    y1 = y1 - 1
                if my_map[x-1][y-1] == 0 and tiles[x-1][y-1] == model.Tile.EMPTY:
                    my_map[x-1][y-1] = 9
                if my_map[x+1][y-1] == 0 and tiles[x+1][y-1] == model.Tile.EMPTY:
                    my_map[x+1][y-1] = 9

    print(unit.position.x, unit.position.y)

    # print my_map
    for y in reversed(list(range(len_y))):
        line = []
        for x in range(len_x):
            line.append(my_map[x][y])
        print(line)

    # preparing matrix - we should invert y axis    
    matrix = []
    for y in range(len_y):
        line = []
        for x in range(len_x):
            line.append(my_map[x][y])
        matrix.insert(0, line)

    grid = Grid(matrix=matrix)
    start = grid.node(int(unit.position.x), len_y - 1 - int(unit.position.y))
#    end = grid.node(3, len_y - 1 - 15)
    end = grid.node(int(target_position.x), len_y - 1 - int(target_position.y))
    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    path, runs = finder.find_path(start, end, grid)
    if len(path) > 1:
        print(grid.grid_str(path=path, start=start, end=end))
        return model.Vec2Float(path[1][0], len_y - 1 - path[1][1])
    else:
        print(grid.grid_str(start=start, end=end))
        return None

