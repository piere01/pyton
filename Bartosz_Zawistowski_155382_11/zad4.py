import numpy
import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D

kolory=['green','red','cyan','black','blue','brown','purple','yellow']
kolory_4_x_5=[kolory[x] for y in range(4) for x in range(0+y,5+y,1)]

fig = pyplot.figure( figsize =( 15 , 7 ))
ax1 = fig.add_subplot( projection = '3d' )
_x = numpy.arange( 5 )
_y = numpy.arange( 4 )
_xx, _yy = numpy.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = (y+x)**(4/3)
bottom = numpy.zeros_like(top)
width = 0.9
depth = 0.95
ax1.bar3d(x, y, bottom, width, depth, top, color=kolory_4_x_5, shade = True, lightsource=None)
pyplot.show()