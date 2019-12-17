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


def distance_sqr_u(a, b):
            return (a.position.x - b.position.x) ** 2 + (a.position.y - b.position.y) ** 2


def on_fire_line(u1, enemy, u2, game):

    print("on_fire_line")
    u1 = u1.position
    enemy = enemy.position
    u2 = u2.position

    d = math.sqrt(distance_sqr(u1, enemy))

    aim = model.Vec2Double(
        enemy.x - u1.x,
        enemy.y - u1.y)

    for i in range(int(d) - 1):
        pos1 = model.Vec2Double(
            u1.x + (i + 1) / d * aim.x,
            u1.y + (i + 1) / d * aim.y)
        print("Fireline ", i, int(pos1.x), int(pos1.y))
        if math.sqrt(distance_sqr(pos1, u2)) < 1:
            print("stop fire!!!")
            return True
        if i < 6 and game.level.tiles[int(pos1.x)][int(pos1.y + 0.5)] == model.Tile.WALL:
            print("stop fire wall !!!")
            return True
    return False


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

        nearest_enemy2 = max(
            filter(lambda u: u.player_id != unit.player_id, game.units),
            key=lambda u: distance_sqr(u.position, unit.position),
            default=None)

        nearest_weapon = None
        if nearest_friend:
            if nearest_friend.id > unit.id:
                nearest_weapon = min(
                    filter(lambda box: isinstance(box.item, model.Item.Weapon)
                           and box.item.weapon_type != model.WeaponType.ROCKET_LAUNCHER, game.loot_boxes),
                    key=lambda box: distance_sqr(box.position, unit.position),
                    default=None)
            else:
                nearest_weapon = min(
                    filter(lambda box: isinstance(box.item, model.Item.Weapon)
                           and box.item.weapon_type == model.WeaponType.ROCKET_LAUNCHER, game.loot_boxes),
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
        jump = target_pos.y > unit.position.y
        dx = target_pos.x - unit.position.x
        if dx > 0.5 and game.level.tiles[int(unit.position.x + 1)][int(unit.position.y)] == model.Tile.WALL:
            jump = True
        if dx < -0.5 and game.level.tiles[int(unit.position.x - 1)][int(unit.position.y)] == model.Tile.WALL:
            jump = True
        if nearest_enemy:
            dx = (nearest_enemy.position.x - unit.position.x - math.copysign(1, target_pos.x - unit.position.x))
            print(dx)
            if abs(dx) < 1:
                jump = True
                if nearest_friend and nearest_friend.id < unit.id:
                    jump = False
        if nearest_friend and nearest_friend.id > unit.id:
            dx = (nearest_friend.position.x - unit.position.x - math.copysign(1, target_pos.x - unit.position.x))
            if abs(dx) < 1.5:
                jump = True

        shoot = True
        if nearest_friend:
            if nearest_enemy and on_fire_line(unit, nearest_enemy, nearest_friend, game):
                nearest_enemy = nearest_enemy2
                if nearest_enemy and on_fire_line(unit, nearest_enemy, nearest_friend, game):
                    shoot = False
        else:
            if on_fire_line(unit, nearest_enemy, unit, game):
                nearest_enemy = nearest_enemy2
                if on_fire_line(unit, nearest_enemy, unit, game):
                    shoot = False

        aim = model.Vec2Double(0, 0)
        if nearest_enemy is not None:
            aim = model.Vec2Double(
                nearest_enemy.position.x - unit.position.x,
                nearest_enemy.position.y - unit.position.y)

        direction = 1
        for u in game.units:
            if u.player_id != unit.player_id:
                if u.weapon and u.weapon.typ == model.WeaponType.ROCKET_LAUNCHER:
                    if distance_sqr(u.position, unit.position) < 150:
                        direction = -1
                        break

        velocity = direction * 20 * (target_pos.x - unit.position.x)
        print('vel', velocity, random.randint(-10, 10) / 10)
        return model.UnitAction(
            velocity=direction * 20 * (target_pos.x - unit.position.x) + random.randint(-10, 10) / 10,
            jump=jump,
            jump_down=not jump,
            aim=aim,
            shoot=shoot,
            reload=False,
            swap_weapon=(unit.weapon and (unit.weapon.typ == model.WeaponType.ROCKET_LAUNCHER)),
            plant_mine=(nearest_friend and unit.health < 20))
