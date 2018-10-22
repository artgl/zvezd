import sys
import time
import math
import random

import gym
from gym import wrappers, logger

class RandomAgent(object):
    """The world's simplest agent!"""
    def __init__(self, action_space):
        self.action_space = action_space
        self.old_dth = None
        self.old_th = None
        self.prev_res = 0
        self.max_abs = 0

    def act(self, observation, reward, done):
        
        res = None

        th = observation[2]
        dist = observation[0]

        if self.old_th:
            dth = th - self.old_th
        else:
            dth = 0

        if abs(th) > self.max_abs:
            self.max_abs = abs(th)

        print(th, dth, dist)
        print(self.max_abs)

        self.old_th = th 
        self.prev_res = res
        print (res)
        return res

if __name__ == '__main__':

    # You can set the level to logger.DEBUG or logger.WARN if you
    # want to change the amount of output.
    logger.set_level(logger.INFO)

    env = gym.make('CartPole-v0')

    # You provide the directory to write to (can be an existing
    # directory, including one with existing data -- all monitor files
    # will be namespaced). You can also dump to a tempdir if you'd
    # like: tempfile.mkdtemp().
    outdir = '.'
    env = wrappers.Monitor(env, directory=outdir, force=True)
#    env.seed(0)
    agent = RandomAgent(env.action_space)

    reward = 0
    done = False

    ob = env.reset()
#    import pdb; pdb.set_trace()
    env.env.env.theta_threshold_radians = 45 * 2 * math.pi / 360
    env.env._max_episode_steps = 1000
    i = 0
    while True:

        action = agent.act(ob, reward, done)
        ob, reward, done, _ = env.step(action)

#        print(ob[0], ob[1], ob[2], ob[3])

        if done:
            break
        # Note there's no env.render() here. But the environment still can open window and
        # render if asked by env.monitor: it calls env.render('rgb_array') to record video.
        # Video is not recorded every episode, see capped_cubic_video_schedule for details.
        time.sleep(0.2)
        i = i + 1

    print("i=", i)
    # Close the env and write monitor result info to disk
    env.close()
