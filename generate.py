import pyrosim.pyrosim as pyrosim


#pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length,width,height])
def Create_World():
    length, width, height = 1, 1, 1
    x, y, z = 0, 0, 0.5 
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length,width,height])
    pyrosim.End()

def Create_Robot():
    length, width, height = 1, 1, 1
    x, y, z = 0, 0, 0.5 
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x, y, z] , size=[length,width,height])
    pyrosim.End()

Create_World()
Create_Robot()