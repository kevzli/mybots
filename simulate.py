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

        simulation = SIMULATION()
        self.world = WORLD()
        self.robot = ROBOT()

    physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0,0,-9.8)
    #planeId = p.loadURDF("plane.urdf")
    #robotId = p.loadURDF("body.urdf")
    #p.loadSDF("world.sdf")
    pyrosim.Prepare_To_Simulate(self.robotId)    

exit()

backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)


#targetAngles = (numpy.pi/4.0) * numpy.sin(x)
targetAnglesFront = c.amplitudeFront * numpy.sin(c.frequencyFront * c.x + c.phaseOffsetFront)
targetAnglesBack = c.amplitudeBack * numpy.sin(c.frequencyBack * c.x + c.phaseOffsetBack)
numpy.save(os.path.join('data', 'targetAnglesFront'), targetAnglesFront, allow_pickle=True, fix_imports=True)
numpy.save(os.path.join('data', 'targetAnglesBack'), targetAnglesBack, allow_pickle=True, fix_imports=True)
#exit()

for i in range(1001):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesBack[i] , maxForce = 20)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_FrontLeg", controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesFront[i], maxForce = 20)

    time.sleep(1/10)
    #print(i)

p.disconnect()

print(backLegSensorValues)
numpy.save(os.path.join('data', 'backLegSensorValues'), backLegSensorValues, allow_pickle=True, fix_imports=True)
print(frontLegSensorValues)
numpy.save(os.path.join('data', 'frontLegSensorValues'), frontLegSensorValues, allow_pickle=True, fix_imports=True)
