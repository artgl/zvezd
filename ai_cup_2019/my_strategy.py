import model
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import copy
import pprint
import random
import pathfinding
from one_step_to import one_step_to
import math

def distance_sqr(a, b):
            return (a.x - b.x) ** 2 + (a.y - b.y) ** 2

class MyStrategy:
    def __init__(self):
        pass

    def get_action(self, unit, game, debug):
        # Replace this code with your own

        if len(game.units) > 2:
            nearest_friend = max(
                    filter(lambda u: u.player_id == unit.player_id, game.units),
                    key=lambda u: distance_sqr(u.position, unit.position),
                    default=None)
        else:
            nearest_friend = None

        nearest_enemy = min(
            filter(lambda u: u.player_id != unit.player_id, game.units),
            key=lambda u: distance_sqr(u.position, unit.position),
            default=None)

        nearest_weapon = None
        if nearest_friend:
            if nearest_friend.id > unit.id:
                nearest_weapon = min(
                    filter(lambda box: isinstance(
                        box.item, model.Item.Weapon) and box.item.weapon_type == model.WeaponType.ASSAULT_RIFLE, game.loot_boxes),
                    key=lambda box: distance_sqr(box.position, unit.position),
                    default=None)
            else:
                nearest_weapon = min(
                    filter(lambda box: isinstance(
                        box.item, model.Item.Weapon) and box.item.weapon_type == model.WeaponType.PISTOL, game.loot_boxes),
                    key=lambda box: distance_sqr(box.position, unit.position),
                    default=None)
        if not nearest_weapon:
            nearest_weapon = min(
                filter(lambda box: isinstance(
                    box.item, model.Item.Weapon), game.loot_boxes),
                key=lambda box: distance_sqr(box.position, unit.position),
                default=None)
        nearest_hp = min(
            filter(lambda box: isinstance(
                box.item, model.Item.HealthPack), game.loot_boxes),
            key=lambda box: distance_sqr(box.position, unit.position),
            default=None)
         
        target_pos = unit.position
        if unit.health < 80 and nearest_hp:
            debug.draw(model.CustomData.Log("target: xp"))
            target_pos = nearest_hp.position
        elif unit.weapon is None:
            debug.draw(model.CustomData.Log("target: initial weapon"))
            target_pos = nearest_weapon.position
        elif nearest_weapon and unit.weapon and unit.weapon.typ == model.WeaponType.ROCKET_LAUNCHER:
            debug.draw(model.CustomData.Log("target: weapon"))
            target_pos = nearest_weapon.position
        elif nearest_enemy:
            debug.draw(model.CustomData.Log("target: enemy"))
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
        jump = target_pos.y > unit.position.y
        if target_pos.x > unit.position.x and game.level.tiles[int(unit.position.x + 1)][int(unit.position.y)] == model.Tile.WALL:
            jump = True
        if target_pos.x < unit.position.x and game.level.tiles[int(unit.position.x - 1)][int(unit.position.y)] == model.Tile.WALL:
            jump = True
        if nearest_enemy:
            dx = (nearest_enemy.position.x - unit.position.x - math.copysign(1, target_pos.x - unit.position.x))
            print(dx)
            if abs(dx) < 1:
                jump = True
        if nearest_friend and nearest_friend.id > unit.id:
            dx = (nearest_friend.position.x - unit.position.x - math.copysign(1, target_pos.x - unit.position.x))
            print(dx)
            if abs(dx) < 2 and target_pos.y > (unit.position.y + 2):
                jump = True

        shoot = True
        if unit.weapon and unit.weapon.typ == model.WeaponType.ROCKET_LAUNCHER:
            shoot = False
            if nearest_enemy and abs(nearest_enemy.position.x - unit.position.x) < 50:
                if nearest_friend and distance_sqr(unit.position, nearest_friend.position) > 20:
                    shoot = True

        direction = 1
        for u in game.units:
            if u.player_id != unit.player_id:
                if u.weapon and u.weapon.typ == model.WeaponType.ROCKET_LAUNCHER:
                    if distance_sqr(u.position, unit.position) < 150:
                        direction = -1
                        break
 
        return model.UnitAction(
            velocity=direction * 20 * (target_pos.x - unit.position.x),
#            velocity=100 if target_pos.x > unit.position.x else -100,
            jump=jump,
            jump_down=not jump,
            aim=aim,
            shoot=shoot,
#            shoot=False,
            reload=False,
            swap_weapon=(unit.weapon and (unit.weapon.typ == model.WeaponType.ROCKET_LAUNCHER)),
            plant_mine=(nearest_friend and unit.health < 20))
