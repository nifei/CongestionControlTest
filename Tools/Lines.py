import matplotlib.pyplot as pyplot
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
from pylab import *
import numpy

def DrawLines(xlists, ylists, ylabels):
    line_count = len(ylists)
    ymin = min([min(ylist) for ylist in ylists])
    ymax = max([max(ylist) for ylist in ylists])
    diff = ymax-ymin
    ymin = ymin - 0.1*diff
    ymax = ymax + 0.1*diff
    clf()
    host = host_subplot(111, axes_class=AA.Axes)
    pyplot.subplots_adjust(right=(0.9-0.05*line_count))
    host.set_xlabel('time')
    host.set_ylabel(ylabels[0])
    host.set_ylim(ymin, ymax)
    p1, = host.plot(xlists[0], ylists[0], label=ylabels[0])
    host.axis['left'].label.set_color(p1.get_color())
    for i in range(1, line_count):
        offset = 60*i
        par = host.twinx()
        new_fixed_axis = par.get_grid_helper().new_fixed_axis
        par.axis["right"] = new_fixed_axis(loc="right", axes=par, offset=(offset, 0))
        par.axis['right'].toggle(all=True)
        par.set_ylabel(ylabels[i])
        p, = par.plot(xlists[i], ylists[i], label = ylabels[i])
        par.set_ylim(ymin, ymax)
        par.axis['right'].label.set_color(p.get_color())

    host.legend()
    pyplot.draw()
    pyplot.show()

#t = [1,2,3,4]
#y1=[1,2,3,4]
#y2=[5,6,7,8]
#y3=[9,10,1,2]
#DrawLines(t, [y1, y2, y3], ['y1', 'y2', 'y3'])
