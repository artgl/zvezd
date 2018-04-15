# -*- coding: utf-8 -*-

from math import *
from model.FireType import FireType
from model.TankType import TankType
import random



class MyStrategy:

    def __init__(self):
        self.left_track_power = 0
        self.right_track_power = 0

    def move(self, me, world, move):

        if (world.tick % 50) == 0:
            self.left_track_power = random.randint(-1, 1)
            self.right_track_power = random.randint(-1, 1)

        move.left_track_power = self.left_track_power
        move.right_track_power = self.right_track_power

        move.fire_type = FireType.PREMIUM_PREFERRED

    def select_tank(self, tank_index, team_size):
        return TankType.MEDIUM
