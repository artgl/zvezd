# -*- coding: utf-8 -*-

from math import *
from model.FireType import FireType
from model.TankType import TankType

class MyStrategy:
    def move(self, me, world, move):

        for tank in world.tanks:
            # стреляем в первый найденный танк который не в нашей команде
            if tank.teammate == False:
                # если наш танк смотрит на противника, то выключаем гусеницы и стреляем
                if abs(me.get_angle_to_unit(tank)) < 0.1:
                    move.left_track_power = 0
                    move.right_track_power = 0
                    move.fire_type = FireType.PREMIUM_PREFERRED
                # вражеский танк сбоку, разворачиваемся в эту сторону, не стреляем
                elif me.get_angle_to_unit(tank) < 0:
                    move.left_track_power = -1
                    move.right_track_power = 1
                    move.fire_type = FireType.NONE
                # вражеский танк с другого боку, разворачиваемся в другую сторону, не стреляем
                elif me.get_angle_to_unit(tank) > 0:
                    move.left_track_power = 1
                    move.right_track_power = -1
                    move.fire_type = FireType.NONE

    def select_tank(self, tank_index, team_size):
        return TankType.MEDIUM
