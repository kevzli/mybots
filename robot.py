from sensor import SENSOR
from motor import MOTOR

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import os
import random
import matplotlib.pyplot
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:

    def __init__(self):

        self.robotId = p.loadURDF("body.urdf")
        
        self.motors = {}

        self.sensors = {}

        self.nn = NEURAL_NETWORK("brain.nndf")

    def Prepare_To_Sense(self):
        
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)
    
    def Prepare_To_Act(self):
        #self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            print(neuronName)
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(desiredAngle, self.robotID)
                print()

        # for i in self.motors:
        #     self.motors[i].Set_Value(t, self.robotID)
    
    def Think(self):
        self.nn.Update()
        self.nn.Print()