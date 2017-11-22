import vrep
import time
import math


def to_rad(grad):
    if grad > 0:
        return 2 * math.pi / 360 * grad
    return 0

def forward():

    str = "a030c140b150d030a140c030b030d150"

    opMode = vrep.simx_opmode_blocking

    i = 0

    while True:

        b1 = str[i + 0]
        b2 = str[i + 1]
        b3 = str[i + 2]
        b4 = str[i + 3]

        grad = int(b2) * 100 + int(b3) * 10 + int(b4)

        if (b1 == 'a'):
            object_name = "arm1_1"
            rad = - to_rad(120) + to_rad(grad)
        if (b1 == 'b'):
            object_name = "arm1_2"
            rad = - to_rad(30) + to_rad(grad)
        if (b1 == 'c'):
            object_name = "arm2_1"
            rad = - to_rad(50) + to_rad(grad)
        if (b1 == 'd'):
            object_name = "arm2_2"
            rad = - to_rad(180) + to_rad(30) + to_rad(grad)

        print object_name, grad

        res, handle = vrep.simxGetObjectHandle(clientID, object_name, opMode)
        res = vrep.simxSetJointTargetPosition(clientID, handle, rad, opMode)

        time.sleep(1)

#        res, handle = vrep.simxGetObjectHandle(clientID, object_name, opMode)
#        res = vrep.simxSetJointTargetPosition(clientID, handle, -math.pi / 2.2, opMode)
#        res, handle = vrep.simxGetObjectHandle(clientID, "arm2_1", opMode)
#        res = vrep.simxSetJointTargetPosition(clientID, handle, math.pi / 2.2, opMode)
#
#        time.sleep(1)
#
#        res, handle = vrep.simxGetObjectHandle(clientID, "arm1_2", opMode)
#        res = vrep.simxSetJointTargetPosition(clientID, handle, math.pi / 4, opMode)
#        res, handle = vrep.simxGetObjectHandle(clientID, "arm2_2", opMode)
#        res = vrep.simxSetJointTargetPosition(clientID, handle, -math.pi / 4, opMode)
#
#        time.sleep(1)
#
#        res, handle = vrep.simxGetObjectHandle(clientID, "arm1_1", opMode)
#        res = vrep.simxSetJointTargetPosition(clientID, handle, math.pi / 3, opMode)
#        res, handle = vrep.simxGetObjectHandle(clientID, "arm2_1", opMode)
#        res = vrep.simxSetJointTargetPosition(clientID, handle, -math.pi / 3, opMode)
#
#        time.sleep(1)
#
#        res, handle = vrep.simxGetObjectHandle(clientID, "arm1_2", opMode)
#        res = vrep.simxSetJointTargetPosition(clientID, handle, 0, opMode)
#        res, handle = vrep.simxGetObjectHandle(clientID, "arm2_2", opMode)
#        res = vrep.simxSetJointTargetPosition(clientID, handle, 0, opMode)
#
        i = i + 4
        if (i >= len(str)):
            i = 0

    time.sleep(10)


print ('Program started')

vrep.simxFinish(-1)  # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)  # Connect to V-REP
if clientID != -1:
    print ('Connected to remote API server')

    # Now try to retrieve data in a blocking fashion (i.e. a service call):
    res, objs = vrep.simxGetObjects(clientID, vrep.sim_handle_all, vrep.simx_opmode_blocking)
    if res == vrep.simx_return_ok:
        print ('Number of objects in the scene: ', len(objs))
    else:
        print ('Remote API function call returned with error code: ', res)

    time.sleep(2)

    forward()

    # Now close the connection to V-REP:
    vrep.simxFinish(clientID)
else:
    print ('Failed connecting to remote API server')

print ('Program ended')
