# -*- coding: utf-8 -*-

from math import *
from model.FireType import FireType
from model.TankType import TankType
from model.BonusType import BonusType
import random


class MyStrategy:

    def __init__(self):
        self.left_track_power = 0
        self.right_track_power = 0

    def go_to_nearest_bonus(self, me, world):
        nearest_bonus = None
        nearest_bonus_distance = 10000

        for bonus in world.bonuses:
            distance = me.get_distance_to_unit(bonus)
            if distance < nearest_bonus_distance:
                nearest_bonus = bonus
                nearest_bonus_distance = distance

        if nearest_bonus:
            if abs(me.get_angle_to_unit(nearest_bonus)) < 0.2:
                self.left_track_power = 1
                self.right_track_power = 1
                print "forward!"
            # бонус сбоку, разворачиваемся в эту сторону
            elif me.get_angle_to_unit(nearest_bonus) < -0.5:
                self.left_track_power = -1
                self.right_track_power = 1
                print "left!"
            elif me.get_angle_to_unit(nearest_bonus) < 0:
                self.left_track_power = -0.5
                self.right_track_power = 0.5
                print "small left!"
            # бонус с другого боку, разворачиваемся в другую сторону
            elif me.get_angle_to_unit(nearest_bonus) > 0.5:
                self.left_track_power = 1
                self.right_track_power = -1
                print "right!"
            elif me.get_angle_to_unit(nearest_bonus) > 0:
                self.left_track_power = 0.5
                self.right_track_power = -0.5
                print "small right!"
            return True
        else:
            return False

    def move(self, me, world, move):

        if self.go_to_nearest_bonus(me, world) is True:
            pass
        else:
            if (world.tick % 50) == 0:
                self.left_track_power = random.randint(-1, 1)
                self.right_track_power = random.randint(-1, 1)

        for tank in world.tanks:
            if tank.teammate is False:
                if abs(me.get_angle_to_unit(tank)) < 0.05:
                    move.fire_type = FireType.PREMIUM_PREFERRED

        move.left_track_power = self.left_track_power
        move.right_track_power = self.right_track_power

    def select_tank(self, tank_index, team_size):
        return TankType.MEDIUM
