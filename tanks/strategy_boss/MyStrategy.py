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
        pass

    def move_to(self, unit):
        if self.me.get_angle_to_unit(unit) < 0.5 and self.me.get_angle_to_unit(unit) > -0.5:
            print("to forward")
            self.mv.left_track_power = 1
            self.mv.right_track_power = 1
        elif self.me.get_angle_to_unit(unit) > 0:
            print("to rotate left")
            self.mv.left_track_power = -1
            self.mv.right_track_power = 1
        else:
            print("to rotate right")
            self.mv.left_track_power = 1
            self.mv.right_track_power = -1

    def move_from(self, unit):
        print(self.me.get_angle_to_unit(unit))
        if self.me.get_angle_to_unit(unit) < -0.5 or self.me.get_angle_to_unit(unit) > 0.5:
            print("from back")
            self.mv.left_track_power = -1
            self.mv.right_track_power = -1
        elif self.me.get_angle_to_unit(unit) > 0:
            print("from rotate left")
            self.mv.left_track_power = -1
            self.mv.right_track_power = 1
        else:
            print("from rotate right")
            self.mv.left_track_power = 1
            self.mv.right_track_power = -1

    def get_enemy(self):
        for tank in self.world.tanks:
            if tank.teammate is False:
                return tank

    def move(self, me, world, move):
        self.me = me
        self.world = world
        if hasattr(self, 'mv'):
            self.prev_mv = self.mv
        self.mv = move
        self.enemy = None
        self.enemy_shell = None

        for tank in self.world.tanks:
            if tank.teammate is False:
                self.enemy = tank

        if len(world.shells) > 0:
            print("!!!Shells")
            for shell in world.shells:
                d1 = me.get_distance_to(shell.x, shell.y)
                d2 = me.get_distance_to(shell.x + shell.speedX, shell.y + shell.speedY)
                if (d2 < d1):  # пуля летит на нас
                    self.enemy_shell = shell

        a1 = abs(self.me.get_angle_to(0,0))
        a2 = abs(self.me.get_angle_to(self.world.width, 0))
        a3 = abs(self.me.get_angle_to(self.world.width, self.world.height))
        a4 = abs(self.me.get_angle_to(0,self.world.height))

        d1 = self.me.get_distance_to(0,0)
        d2 = self.me.get_distance_to(self.world.width, 0)
        d3 = self.me.get_distance_to(self.world.width, self.world.height)
        d4 = self.me.get_distance_to(0,self.world.height)

        l = [a1, a2, a3, a4]
        if min(l) == a1:
            d = d1
        if min(l) == a2:
            d = d2
        if min(l) == a3:
            d = d3
        if min(l) == a4:
            d = d4

        def f1():
            if not self.already_moving:
                print("new move")
                if d > 800:
                    self.mv.left_track_power = 1
                    self.mv.right_track_power = 1
                else:
                    self.mv.left_track_power = -1
                    self.mv.right_track_power = -1
                self.already_moving = True
            else:
                print("using prev move")
                self.mv.left_track_power = self.prev_mv.left_track_power
                self.mv.right_track_power = self.prev_mv.right_track_power


        if self.enemy_shell:
            f1()
        else:
            self.already_moving = False

            a1 = self.me.get_angle_to_unit(self.enemy)

            if a1 > (math.pi / 2 - 0.1) and a1 < (math.pi / 2 + 0.1):
                print("good")
                f1()
#                self.mv.left_track_power = 0
#                self.mv.right_track_power = 0
            else:
                if a1 < (math.pi / 2 - 0.1):
                    print("left")
                    self.mv.left_track_power = -1
                    self.mv.right_track_power = 1
                else:
                    print("right")
                    self.mv.left_track_power = 1
                    self.mv.right_track_power = -1

#        if self.enemy_shell:
#            self.move_from(self.enemy_shell)
#        else:
#            print("no shells")
#            enemy = self.get_enemy()
#            if me.get_distance_to_unit(enemy) > 700:
#                self.move_to(enemy)
#            else:
#                self.move_from(enemy)

#        move.fire_type = FireType.PREMIUM_PREFERRED

    def select_tank(self, tank_index, team_size):
        return TankType.MEDIUM
