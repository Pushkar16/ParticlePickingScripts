from skimage import transform as tf
import matplotlib.pyplot as plt
import numpy 
import mrcfile
with mrcfile.open('filter_resize__ctf.mrc') as mrc:
  arr=mrc.data
a = numpy.asarray(arr)
b = abs(numpy.fft.fftshift(numpy.fft.fft2(a)))
b = b.astype(numpy.float32, copy=False)
with mrcfile.new('outputref.mrc') as mrc1:
    mrc1.set_data(b)

