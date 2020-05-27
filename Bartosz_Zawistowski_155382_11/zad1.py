from mpl_toolkits.mplot3d import Axes3D
import numpy 
import matplotlib.pyplot as pyplot


fig = pyplot.figure()
ax = fig.gca( projection = '3d' )
z = numpy.linspace( 0 , 2 * numpy.pi, 100 )
x = numpy.sin(z)
y = 2*numpy.cos(z)
ax.plot(x, y, z, label = 'zad1' )
ax.legend()
pyplot.show()