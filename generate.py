import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
length, width, height = 1, 1, 1
x, y, z = 0, 0, 0.5
#pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length,width,height])
#x2, y2, z2 = 1, 0, 1.5
#pyrosim.Send_Cube(name="Box2", pos=[x2, y2, z2] , size=[length,width,height])

for i in range(5):
    x += 1
    y = 0
    for j in range(5):
        y += 1
        length, width, height = 1, 1, 1
        for k in range(5):
            pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length,width,height])
            z += 1
            length, width, height = 0.9 * length, 0.9 * width, 0.9 * height
    
pyrosim.End()