import model
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import copy
import pprint

def distance_sqr(a, b):
            return (a.x - b.x) ** 2 + (a.y - b.y) ** 2

class MyStrategy:
    def __init__(self):
        pass

    def goto(self, game, unit):


        len_x = len(game.level.tiles)
        len_y = len(game.level.tiles[0])

        my_map = copy.deepcopy(game.level.tiles)
        tiles = game.level.tiles
        for x in range(len_x):
            for y in range(len_y):
                my_map[x][y] = 0
                try:
                    if tiles[x][y] == model.Tile.EMPTY and tiles[x][y - 1] == model.Tile.WALL:
                        my_map[x][y] = 1
                        if tiles[x-1][y] == model.Tile.EMPTY:
                            my_map[x-1][y] = 1
                        if tiles[x+1][y] == model.Tile.EMPTY:
                            my_map[x+1][y] = 1
                        if tiles[x-1][y+1] == model.Tile.EMPTY:
                            my_map[x-1][y+1] = 1
                        if tiles[x+1][y+1] == model.Tile.EMPTY:
                            my_map[x+1][y+1] = 1
                except IndexError:
                    pass

        # тайлы в которых мы можем падать - они всегда ниже текущей позициии игрока
        for x in range(len_x):
            for y in range(int(unit.position.y)):
                try:
                    if tiles[x][y] == model.Tile.EMPTY and \
                            (tiles[x - 1][y] == model.Tile.WALL or tiles[x + 1][y] == model.Tile.WALL):
                        y1 = y
                        while tiles[x][y1] == model.Tile.EMPTY:
                            my_map[x][y1] = 1
                            y1 = y1 - 1
                except IndexError:
                    pass

        grid = Grid(matrix=my_map)

        new = []
        for y in reversed(list(range(len_y))):
            line = []
            for x in range(len_x):
                line.append(my_map[x][y])
            new.insert(0, line)
            
        for line in new:
            print(line)

        pistol = min(
            filter(lambda box: isinstance(
                box.item, model.Item.Weapon) and box.item.weapon_type == 0, game.loot_boxes),
            key=lambda box: distance_sqr(box.position, unit.position),
            default=None)

        if pistol:
#            start = grid.node(int(unit.position.x), int(unit.position.y))
#            end = grid.node(int(pistol.position.x), int(pistol.position.y))
            start = grid.node(34, 5)
            end = grid.node(30, 5)

            finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
            path, runs = finder.find_path(start, end, grid)

        print()

    def get_action(self, unit, game, debug):
        # Replace this code with your own
        


        self.goto(game, unit)

        nearest_enemy = min(
            filter(lambda u: u.player_id != unit.player_id, game.units),
            key=lambda u: distance_sqr(u.position, unit.position),
            default=None)
        nearest_weapon = min(
            filter(lambda box: isinstance(
                box.item, model.Item.Weapon), game.loot_boxes),
            key=lambda box: distance_sqr(box.position, unit.position),
            default=None)
        target_pos = unit.position
        if unit.weapon is None and nearest_weapon is not None:
            target_pos = nearest_weapon.position
        elif nearest_enemy is not None:
            target_pos = nearest_enemy.position
        debug.draw(model.CustomData.Log("Target pos: {}".format(target_pos)))
        aim = model.Vec2Double(0, 0)
        if nearest_enemy is not None:
            aim = model.Vec2Double(
                nearest_enemy.position.x - unit.position.x,
                nearest_enemy.position.y - unit.position.y)
        jump = target_pos.y > unit.position.y
        if target_pos.x > unit.position.x and game.level.tiles[int(unit.position.x + 1)][int(unit.position.y)] == model.Tile.WALL:
            jump = True
        if target_pos.x < unit.position.x and game.level.tiles[int(unit.position.x - 1)][int(unit.position.y)] == model.Tile.WALL:
            jump = True

           
        return model.UnitAction(
            velocity=target_pos.x - unit.position.x,
            jump=jump,
            jump_down=not jump,
            aim=aim,
            shoot=True,
            reload=False,
            swap_weapon=False,
            plant_mine=False)
