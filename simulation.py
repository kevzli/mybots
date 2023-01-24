from world import WORLD
from robot import ROBOT

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import os
import random
import matplotlib.pyplot
import constants as c


#amplitudeFront, frequencyFront, phaseOffsetFront = numpy.pi/4.0, 5, 0
#amplitudeBack, frequencyBack, phaseOffsetBack = numpy.pi/4.0, 5, numpy.pi/4.0


class SIMULATION:

    def __init__(self):

        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
    #planeId = p.loadURDF("plane.urdf")
    #robotId = p.loadURDF("body.urdf")
    #p.loadSDF("world.sdf")
        

        self.world = WORLD()
        self.robot = ROBOT()  

        pyrosim.Prepare_To_Simulate(self.robot.robotId)  

        self.robot.Prepare_To_Sense()
        
        

    def Run(self):
        
        for t in range(1001):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Act()
            time.sleep(1/60)
            print(t)

        #p.disconnect()
    
    def __del__(self):

        p.disconnect()


# frontLegSensorValues = numpy.zeros(100)


# #targetAngles = (numpy.pi/4.0) * numpy.sin(x)
# targetAnglesFront = c.amplitudeFront * numpy.sin(c.frequencyFront * c.x + c.phaseOffsetFront)
# targetAnglesBack = c.amplitudeBack * numpy.sin(c.frequencyBack * c.x + c.phaseOffsetBack)
# numpy.save(os.path.join('data', 'targetAnglesFront'), targetAnglesFront, allow_pickle=True, fix_imports=True)
# numpy.save(os.path.join('data', 'targetAnglesBack'), targetAnglesBack, allow_pickle=True, fix_imports=True)
# #exit()


# print(backLegSensorValues)
# numpy.save(os.path.join('data', 'backLegSensorValues'), backLegSensorValues, allow_pickle=True, fix_imports=True)
# print(frontLegSensorValues)
# numpy.save(os.path.join('data', 'frontLegSensorValues'), frontLegSensorValues, allow_pickle=True, fix_imports=True)
