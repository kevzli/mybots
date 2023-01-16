import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('./data/backLegSensorValues.npy')
print(backLegSensorValues)
frontLegSensorValues = numpy.load('./data/frontLegSensorValues.npy')
print(frontLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues, label='back leg', linewidth = 5)
matplotlib.pyplot.plot(frontLegSensorValues, label='front leg')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()