import numpy
import matplotlib.pyplot


backLegSensorValues = numpy.load("./data/backLegSensorValues.npy", mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII', *, max_header_size=10000)
print(backLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues)