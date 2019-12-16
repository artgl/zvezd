import model
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import copy
import pprint
import random
import pathfinding
from one_step_to import one_step_to

pathfinding.finder.MAX_RUNS = 10

def distance_sqr(a, b):
            return (a.x - b.x) ** 2 + (a.y - b.y) ** 2

class MyStrategy:
    def __init__(self):
        pass

    def get_action(self, unit, game, debug):
        # Replace this code with your own

        nearest_enemy = min(
            filter(lambda u: u.player_id != unit.player_id, game.units),
            key=lambda u: distance_sqr(u.position, unit.position),
            default=None)
        nearest_pistol = min(
            filter(lambda box: isinstance(
                box.item, model.Item.Weapon) and box.item.weapon_type == 0, game.loot_boxes),
            key=lambda box: distance_sqr(box.position, unit.position),
            default=None)
        nearest_weapon = min(
            filter(lambda box: isinstance(
                box.item, model.Item.Weapon), game.loot_boxes),
            key=lambda box: distance_sqr(box.position, unit.position),
            default=None)
        
        target_pos = unit.position
        if unit.weapon is None:
            if nearest_pistol:
                 target_pos = nearest_pistol.position
            else:
                 target_pos = nearest_weapon.position
        elif (unit.weapon.typ != model.WeaponType.PISTOL) and nearest_pistol:
            target_pos = nearest_pistol.position
        elif nearest_enemy is not None:
            target_pos = nearest_enemy.position

        pos = one_step_to(game, unit, target_pos)
        if pos:
            target_pos = pos

        debug.draw(model.CustomData.Log("Target pos: {}".format(target_pos)))
        debug.draw(model.CustomData.Log("Unit pos: {}".format(unit.position)))
        aim = model.Vec2Double(0, 0)
        if nearest_enemy is not None:
            aim = model.Vec2Double(
                nearest_enemy.position.x - unit.position.x,
                nearest_enemy.position.y - unit.position.y)
        jump = target_pos.y > unit.position.y \
                or game.level.tiles[int(unit.position.x)][int(unit.position.y - 1)] == model.Tile.EMPTY
        if target_pos.x > unit.position.x and game.level.tiles[int(unit.position.x + 1)][int(unit.position.y)] == model.Tile.WALL:
            jump = True
        if target_pos.x < unit.position.x and game.level.tiles[int(unit.position.x - 1)][int(unit.position.y)] == model.Tile.WALL:
            jump = True

           
        return model.UnitAction(
            velocity=10 * (target_pos.x - unit.position.x),
#            velocity=100 if target_pos.x > unit.position.x else -100,
            jump=jump,
            jump_down=not jump,
            aim=aim,
            shoot=True,
            reload=False,
            swap_weapon=(unit.weapon and (unit.weapon.typ != model.WeaponType.PISTOL)),
            plant_mine=False)
