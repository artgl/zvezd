# -*- coding: utf-8 -*-

from math import *
from model.FireType import FireType
from model.TankType import TankType
from model.BonusType import BonusType
import random
from math import pi, sin, cos
import time
from shapely.geometry import LineString, Point


class MyStrategy:

    def __init__(self):
        pass

    def is_near_border(self, min_dist=200):
        w = self.world.width
        h = self.world.height
        lines = [
            LineString([(0, 0), (w, 0)]),
            LineString([(0, 0), (0, h)]),
            LineString([(w, 0), (w, h)]),
            LineString([(0, h), (w, h)])
        ]
        for line in lines:
            if Point(self.me.x, self.me.y).distance(line) < min_dist:
                return True
        return False

    def move_turret_to(self, unit, t):
        a = self.me.get_turret_angle_to(self.enemy.x + self.enemy.speedX * t, self.enemy.y + self.enemy.speedY * t)
        if a < 0:
            print("turret_ccw")
            self.mv.turret_turn = -1.0 * pi / 180.0
        else:
            print("turret_cw")
            self.mv.turret_turn =  1.0 * pi / 180.0

        if abs(a) < 0.3 and self.me.remaining_reloading_time < 30:
            print("wait turret")
            self.mv.left_track_power = 0
            self.mv.right_track_power = 0

    def move_to_unit(self, unit):
        self.move_to(unit.x, unit.y)

    def move_to(self, x, y):
        if self.me.get_angle_to(x, y) < 0.5 and self.me.get_angle_to(x, y) > -0.5:
            print("to forward")
            self.mv.left_track_power = 1
            self.mv.right_track_power = 1
        elif self.me.get_angle_to(x, y) > 0:
            print("to rotate left")
            self.mv.left_track_power = 1
            self.mv.right_track_power = -1
        else:
            print("to rotate right")
            self.mv.left_track_power = -1
            self.mv.right_track_power = 1

    def get_enemy(self):
        self.enemy = None
        for tank in self.world.tanks:
            if tank.teammate is False:
                self.enemy = tank

    def get_enemy_shell(self):
        self.enemy_shell = None
        for shell in self.world.shells:
            d1 = self.me.get_distance_to(shell.x, shell.y)
            d2 = self.me.get_distance_to(shell.x + shell.speedX, shell.y + shell.speedY)
            if (d2 < d1):  # пуля летит на нас
                self.enemy_shell = shell

    def move(self, me, world, move):
        self.me = me
        self.world = world
        if hasattr(self, 'mv'):
            self.prev_mv = self.mv
        self.mv = move

        self.get_enemy()
        self.get_enemy_shell()

        if self.is_near_border():
            print("near_border")
            self.move_to(self.world.width/2, self.world.height/2)
        else:
            print("no_border")
            if self.enemy_shell:
                a = self.me.get_angle_to_unit(self.enemy_shell)
            if self.enemy_shell and abs(abs(a) - pi / 2) < 0.4:
                print(a, pi / 2)
                print('evade')
                self.mv.left_track_power = 1
                self.mv.right_track_power = 1
            else:
                print('no_evade')

                if abs(abs(self.me.get_angle_to_unit(self.enemy)) - pi / 2) > 0.4:
                    a = self.me.get_angle_to_unit(self.enemy)
                    speed = 1
                    if a > -pi and a < -pi / 2:
                        print('rotate cw1')
                        self.mv.left_track_power  = - speed
                        self.mv.right_track_power =   speed
                    if a > -pi / 2 and a < 0:
                        print('rotate ccw2')
                        self.mv.left_track_power  =   speed
                        self.mv.right_track_power = - speed
                    if a > 0 and a < pi / 2:
                        print('rotate cw3')
                        self.mv.left_track_power  = - speed
                        self.mv.right_track_power =   speed
                    if a > pi / 2:
                        print('rotate ccw4')
                        self.mv.left_track_power  =   speed
                        self.mv.right_track_power = - speed
                else:
                    print('no_rotate')
                    self.mv.left_track_power = 1
                    self.mv.right_track_power = 1

                    for b in self.world.bonuses:
                        if self.me.get_distance_to_unit(b) < 150 and abs(self.me.get_angle_to_unit(b)) < 0.2:
                            print('move to bonus')
                            self.move_to_unit(b)

        bullet_speed = 13 # pixels per tick
        d = self.me.get_distance_to_unit(self.enemy)
        t = d / bullet_speed

        self.move_turret_to(self.enemy, t)

        do_fire = False
        if d < 200 and abs(self.me.get_turret_angle_to(self.enemy.x, self.enemy.y)) < 0.1:
            do_fire = True
        if d >= 200 and abs(self.me.get_turret_angle_to(self.enemy.x + self.enemy.speedX * t, self.enemy.y + self.enemy.speedY * t)) < 0.05:
            do_fire = True

        if do_fire:
            print('fire')
            self.mv.fire_type = FireType.PREMIUM_PREFERRED
            for b in self.world.bonuses:
                if self.me.get_distance_to_unit(b) < d:
                    if abs(self.me.get_turret_angle_to_unit(b)) < 0.05:
                        print('fire canceled')
                        self.mv.fire_type = FireType.NONE
        else:
            print('no_fire')
            self.mv.fire_type = FireType.NONE

    def select_tank(self, tank_index, team_size):
        return TankType.MEDIUM
