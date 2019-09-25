# -*- coding: utf-8 -*-

from math import *
from model.FireType import FireType
from model.TankType import TankType
from model.BonusType import BonusType
import random
import math
import time

class MyStrategy:

    def __init__(self):
        self.p = None

    def get_nearest_bonus(self, me, world, move, bonus_type, enemy):
        nearest_bonus = None
        nearest_bonus_time_to_take = 10000

        a_to_enemy = me.get_angle_to_unit(enemy)

        for bonus in world.bonuses:
            if bonus.type == bonus_type:

                d = me.get_distance_to_unit(bonus)
                a = me.get_angle_to_unit(bonus)

                d_to_enemy = enemy.get_distance_to_unit(bonus)

                # не берем бонус если бонус слишком близко в врагу
                if d_to_enemy < 350:
                    print "has bad bonus"
                    continue

                # считаем что все поле по горизонтали танк проезжает за 6 секунд
                # считаем что танк разворачивается на 180 градусов за 6 секунд
                time_to_take1 = float(d) / (float(world.width) / 6.0)
                time_to_take2 = abs(a) / (math.pi / 6.0)
                time_to_take = time_to_take1 + time_to_take2

                if time_to_take < nearest_bonus_time_to_take:
                    nearest_bonus = bonus
                    nearest_bonus_time_to_take = time_to_take
                    t1 = time_to_take1
                    t2 = time_to_take2

        if nearest_bonus:
            print "Nearest bonus %s: %s + %s" % (bonus_type, t1, t2)

        return nearest_bonus

    def go_to(self, me, world, move, x, y, enemy):

        a = me.get_angle_to(x, y)
        d = me.get_distance_to(x, y)

        near_border = False
        if me.x < 55 or me.x > (world.width - 55) or me.y < 55 or me.y > (world.height - 55):
            print "me.x: %s, me.y: %s" % (me.x, me.y)
            print "-- near border"
            near_border = True

        if abs(a) < 0.5:
            move.left_track_power = 1
            move.right_track_power = 1
            print "forward!"
        else:
            if d > 250 and not near_border and enemy:
                if a <= -0.5:
                    move.left_track_power = 0
                    move.right_track_power = 1
                    print "small left!"
                elif a >= 0.5:
                    move.left_track_power = 1
                    move.right_track_power = 0
                    print "small right!"
            else:  # d <=300
                if a <= -0.5:
                    move.left_track_power = -1
                    move.right_track_power = 1
                    print "max left!"
                elif a >= 0.5:
                    move.left_track_power = 1
                    move.right_track_power = -1
                    print "max right!"

    def aim(self, enemy):
        



    def move(self, me, world, move):

        bonus = None
        enemy = None

        for tank in world.tanks:
            if tank.teammate is False:
                enemy = tank

        ch = float(me.crew_health) / 100
        hd = float(me.hull_durability) / me.hull_max_durability

        print "ch: %s, hd: %s" % (ch, hd)

        if ch <= 0.5 or hd <= 0.5:
            if ch < hd:
                bonus = self.get_nearest_bonus(me, world, move, BonusType.MEDIKIT, enemy)
                if not bonus:
                    bonus = self.get_nearest_bonus(me, world, move, BonusType.REPAIR_KIT, enemy)
            else:
                bonus = self.get_nearest_bonus(me, world, move, BonusType.REPAIR_KIT, enemy)
                if not bonus:
                    bonus = self.get_nearest_bonus(me, world, move, BonusType.MEDIKIT, enemy)

#        time.sleep(0.1)

        if bonus and False:
            self.go_to(me, world, move, bonus.x, bonus.y, enemy)
        else:
            print "remaining_reloading_time %s" % (me.remaining_reloading_time)

            if enemy.x < world.width / 2:
                p1 = (world.width - 140, 140)
                p2 = (world.width - 140, world.height - 140)
            else:
                p1 = (140, 140)
                p2 = (140, world.height - 140)

            if not self.p:
                self.p = p1
            if me.get_distance_to(p1[0], p1[1]) < 30:
                self.p = p2
            if me.get_distance_to(p2[0], p2[1]) < 30:
                self.p = p1

            if me.remaining_reloading_time < 75 and me.get_distance_to_unit(enemy) > 550:
                self.go_to(me, world, move, enemy.x, enemy.y, enemy)
            else:
                self.go_to(me, world, move, self.p[0], self.p[1], enemy)

            a = me.get_angle_to_unit(enemy)
            if abs(a) < 0.03:
                move.fire_type = FireType.PREMIUM_PREFERRED
            else:
                move.fire_type = FireType.NONE

    def select_tank(self, tank_index, team_size):
        return TankType.MEDIUM
