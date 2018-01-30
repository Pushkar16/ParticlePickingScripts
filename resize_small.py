'''import mrcfile
import numpy as np
from array import array
from skimage import transform as tf
import matplotlib.pyplot as plt
with mrcfile.open('op-01.mrc') as mrc:
  arr=mrc.data
m = arr.shape[0]  #image row size
n = arr.shape[1]
print m,n
data = np.random.random((1, 15, 3))*255
data = data.astype(np.uint8)
#print data
new_data = tf.resize(data, (600, 300, 1), order=0)
#print new_data
f, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(10, 10))
ax1.imshow(data)
ax2.imshow(new_data)'''
from skimage import transform as tf
import scipy
import matplotlib.pyplot as plt
import numpy as np
import mrcfile
with mrcfile.open('cf1f0_sumavg_0021.mrc', permissive=True) as mrc:
  arr=mrc.data
new_data =scipy.misc.imresize(arr, (4946, 4946)) # order=0, Nearest-neighbor interpolation
new_data = new_data.astype(np.float32, copy=False)
with mrcfile.new('filter_resize.mrc') as mrc1:
    mrc1.set_data(new_data)
