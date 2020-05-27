import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy 

colormaps=['spring','summer', 'autumn', 'winter', 'copper']

fig = pyplot.figure()
for x in range(321,326,1):
    t=colormaps[int(numpy.random.randint(0,len(colormaps)))]
    colormaps.remove(t)
    ax = fig.add_subplot( x , projection = '3d' )
    X = numpy.arange(- 5 , 5 , 0.25 )
    Y = numpy.arange(- 5 , 5 , 0.25 )
    X, Y = numpy.meshgrid(X, Y)
    R = numpy.sqrt(X** 2 + Y** 2 )
    Z = numpy.sin(R)
    surf = ax.plot_surface(X, Y, Z, cmap =pyplot.get_cmap(t),
    linewidth = 0 , antialiased = False )
    ax.set_zlim(- 1.01 , 1.01 )
    ax.zaxis.set_major_locator(LinearLocator( 10 ))
    ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))

    fig.colorbar(surf, shrink = 0.5 , aspect = 5 )
pyplot.show()