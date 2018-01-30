from skimage import transform as tf
import matplotlib.pyplot as plt
import numpy 
import mrcfile
with mrcfile.open('outputref.mrc') as mrc:
  arr=mrc.data
a = numpy.asarray(arr)
a = a.astype(numpy.float32, copy=False)
with mrcfile.open('output_op-01.mrc') as mrc:
  arr1=mrc.data
b= numpy.asarray(arr1)
b = b.astype(numpy.float32, copy=False)
c= numpy.zeros(shape=(5116,5116))
for i in range(0,arr.shape[0]):
	for j in range(0,arr.shape[1]):
		c[i][j]=a[i][j]*b[i][j]
c = abs(numpy.fft.ifft2(numpy.fft.ifftshift(c)))
c= c.astype(numpy.float32, copy=False)

with mrcfile.new('final.mrc') as mrc1:
    mrc1.set_data(c)