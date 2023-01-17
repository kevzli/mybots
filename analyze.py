import numpy
import matplotlib.pyplot

targetAnglesFront = numpy.load('./data/targetAnglesFront.npy')
targetAnglesBack = numpy.load('./data/targetAnglesBack.npy')
matplotlib.pyplot.plot(range(0,1001), targetAnglesFront, label = 'front leg', linewidth = 5)
matplotlib.pyplot.plot(range(0,1001), targetAnglesBack, label = 'back leg')
matplotlib.pyplot.legend()
matplotlib.pyplot.xlabel('Steps')
matplotlib.pyplot.ylabel('Value in Radians')
matplotlib.pyplot.axis('tight')
matplotlib.pyplot.show()
exit()

backLegSensorValues = numpy.load('./data/backLegSensorValues.npy')
print(backLegSensorValues)
frontLegSensorValues = numpy.load('./data/frontLegSensorValues.npy')
print(frontLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues, label='back leg', linewidth = 5)
matplotlib.pyplot.plot(frontLegSensorValues, label='front leg')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()