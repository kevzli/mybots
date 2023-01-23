import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName

        self.values = numpy.zeros(100)
        #print(self.values)
    
    def Get_Value(self):
        self.values = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        print(self.values)