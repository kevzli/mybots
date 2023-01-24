import constants as c
import pyrosim.pyrosim as pyrosim
import numpy
import pybullet as p

class MOTOR:

    def __init__(self, jointName):

        self.jointName = jointName
        self.motorValues
        self.Prepare_To_Act()


    def Prepare_To_Act(self):
        self.motorValues = {self.amplitude, self.frequency, self.offset}
        #self.values = numpy.zeros(1000)

    def Set_Value(self):
        pyrosim.Set_Motor_For_Joint(jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = self.amplitude * numpy.sin(self.frequency * c.x + self.offset) , maxForce = 20)
