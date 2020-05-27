import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D
import numpy 

numpy.random.seed( 25461874 )
def randrange(n, vmin, vmax):
    return (vmax - vmin)*numpy.random.rand(n) + vmin
kolory=['violet','brown','cyan','orange','red','blue']
markery=['X','$...$','d','*','8','p']
fig = pyplot.figure()
ax = fig.add_subplot( 121 , projection = '3d' )
n=20
xs = randrange(n, 0 , 100 )
ys = randrange(n, 0 , 100 )
zs = randrange(n, 0 , 100 )
ax.scatter(xs, ys, zs, c =kolory[int(numpy.random.randint(0,len(kolory)))], marker =markery[int(numpy.random.randint(0,len(markery)))])
ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
ax = fig.add_subplot( 122 , projection = '3d' )
n=5
xs = randrange(n, 0 , 100 )
ys = randrange(n, 0 , 100 )
zs = randrange(n, 0 , 100 )
ax.plot(xs, ys, zs, c =kolory[int(numpy.random.randint(0,len(kolory)))], marker =markery[int(numpy.random.randint(0,len(markery)))])
ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
pyplot.show()