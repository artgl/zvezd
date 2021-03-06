# Copyright 2006-2017 Coppelia Robotics GmbH. All rights reserved. 
# marc@coppeliarobotics.com
# www.coppeliarobotics.com
# 
# -------------------------------------------------------------------
# THIS FILE IS DISTRIBUTED "AS IS", WITHOUT ANY EXPRESS OR IMPLIED
# WARRANTY. THE USER WILL USE IT AT HIS/HER OWN RISK. THE ORIGINAL
# AUTHORS AND COPPELIA ROBOTICS GMBH WILL NOT BE LIABLE FOR DATA LOSS,
# DAMAGES, LOSS OF PROFITS OR ANY OTHER KIND OF LOSS WHILE USING OR
# MISUSING THIS SOFTWARE.
# 
# You are free to use/modify/distribute this file for whatever purpose!
# -------------------------------------------------------------------
#
# This file was automatically created for V-REP release V3.4.0 rev. 1 on April 5th 2017

# Make sure to have the server side running in V-REP: 
# in a child script of a V-REP scene, add following command
# to be executed just once, at simulation start:
#
# simExtRemoteApiStart(19999)
#
# then start simulation, and run this program.
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!

import vrep
import time

def arm():
    joints = ["Revolute_joint", "Revolute_joint0", "Revolute_joint1"]
    opMode = vrep.simx_opmode_blocking

    while True:
      for name in joints:
          res, handle = vrep.simxGetObjectHandle(clientID, name, opMode)
          res, pos = vrep.simxGetJointPosition(clientID, handle, opMode)

          res = vrep.simxSetJointTargetPosition(clientID, handle, pos + 0.1, opMode);

          print name, pos, res
      time.sleep(2)

def wave():
    opMode = vrep.simx_opmode_blocking
    res, handle = vrep.simxGetObjectHandle(clientID, "Revolute_joint0", opMode)
    res = vrep.simxSetJointTargetVelocity(clientID, handle, 0.6, opMode)
    print res
    time.sleep(6)
    res = vrep.simxSetJointTargetVelocity(clientID, handle, -1.2, opMode)
    time.sleep(1.5)

#    time.sleep(2)
#    res = vrep.simxSetJointTargetPosition(clientID, handle, 1.5, opMode);
#    time.sleep(2)
#    res = vrep.simxSetJointTargetPosition(clientID, handle, 0, opMode);
#    time.sleep(2)
#    res = vrep.simxSetJointTargetPosition(clientID, handle, 1.5, opMode);
#    time.sleep(2)




print ('Program started')

vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP
if clientID != -1:
    print ('Connected to remote API server')

    # Now try to retrieve data in a blocking fashion (i.e. a service call):
    res,objs=vrep.simxGetObjects(clientID,vrep.sim_handle_all,vrep.simx_opmode_blocking)
    if res==vrep.simx_return_ok:
        print ('Number of objects in the scene: ',len(objs))
    else:
        print ('Remote API function call returned with error code: ',res)

    time.sleep(2)

#    arm()

    wave()

    # Now close the connection to V-REP:
    vrep.simxFinish(clientID)
else:
    print ('Failed connecting to remote API server')

print ('Program ended')
