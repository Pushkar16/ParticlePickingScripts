import numpy as np
import matplotlib.pyplot as plt
import mrcfile
import sys

class Formatter(object):
    def __init__(self, im):
        self.im = im
    def __call__(self, x, y):
        z = self.im.get_array()[int(y), int(x)]
        return 'x={:.01f}, y={:.01f},z={:.01f}'.format(x, y, z)
filename=sys.argv[1]
with mrcfile.open(filename, mode='r+', permissive=True) as mrc:
    arr=mrc.data

fig, ax = plt.subplots()
im = ax.imshow(arr,cmap='Greys',origin='lower', interpolation='none')
ax.xaxis.label.set_color('red')
ax.spines['bottom'].set_color('red')
ax.format_coord = Formatter(im)
plt.rc('axes',edgecolor='r')
mng = plt.get_current_fig_manager()
plt.show()