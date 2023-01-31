import constants as c
import pyrosim.pyrosim as pyrosim
import numpy
import pybullet as p
import os

class MOTOR:

    def __init__(self, jointName):

        self.jointName = jointName
        # self.motorValues
        # self.Prepare_To_Act()


    # def Prepare_To_Act(self):
    #     self.amplitude = c.amplitude_Back
    #     self.frequency = c.frequency_Back
    #     self.offset = c.phaseOffset_Back
        
    #     self.motorValues = self.amplitude * numpy.sin(self.frequency * numpy.linspace(0, 2 * numpy.pi, 1000) + self.offset)
    #     #self.values = numpy.zeros(1000)
    #     if self.jointName == 'Torso_BackLeg':
    #         self.frequency = self.frequency / 2

    def Set_Value(self, robotID, desiredAngle):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotID, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = desiredAngle, maxForce = 20)

    def Save_Values(self):
        numpy.save(os.path.join('data', 'motorValues'), self.motorValues, allow_pickle=True, fix_imports=True)