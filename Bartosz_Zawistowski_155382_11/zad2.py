import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D
import numpy


numpy.random.seed( 19680822 )
def randrange(n, vmin, vmax):
    return (vmax - vmin)*numpy.random.rand(n) + vmin
kolory=['blue','black','red','pink','violet','brown','cyan','orange']
markers=['.','o','v','+','D','P','X','<','d','*','8','p']
fig = pyplot.figure()
ax = fig.add_subplot( 111 , projection = '3d' )
n = 100
xs = randrange(n, 0 , 100 )
ys = randrange(n, 0 , 100 )
for x in range(1,6,1):
    zs = randrange(n, 0+20*(x-1), 20*x+1)
    ax.scatter(xs, ys, zs, c =kolory[int(numpy.random.randint(0,len(kolory)))], marker =markers[int(numpy.random.randint(0,len(markers)))])
ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
pyplot.show()