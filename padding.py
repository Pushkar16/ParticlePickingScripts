from skimage import transform as tf
import matplotlib.pyplot as plt
import numpy 
import mrcfile
with mrcfile.open('op-01.mrc') as mrc:
  arr=mrc.data
a = numpy.asarray(arr)
b = numpy.zeros(shape=(4946,4946))
for i in range(0,arr.shape[0]):
	for j in range(0,arr.shape[1]):
		b[i+2413][j+2413]=a[i][j]
b = abs(numpy.fft.fftshift(numpy.fft.fft2(b)))
b = b.astype(numpy.float32, copy=False)
with mrcfile.new('output_op-01.mrc') as mrc1:
    mrc1.set_data(b)

