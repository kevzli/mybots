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

class ROBOT:

    def __init__(self):

        self.robotId = p.loadURDF("body.urdf")
    
        