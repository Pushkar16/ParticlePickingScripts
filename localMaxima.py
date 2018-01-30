
	

import numpy as np
import mrcfile
import scipy
import scipy.ndimage as ndimage
import scipy.ndimage.filters as filters
import matplotlib.pyplot as plt
from skimage.feature import peak_local_max

def cutBoxes(x_coord,y_coord):
	with mrcfile.open('filter_resize__ctf.mrc') as mrc:
		arr=mrc.data
	a = np.zeros(shape=(80,80))
	for i in range(0,80):
		for j in range(0,80):
			a[i][j]=arr[x_coord+i-40][y_coord+j-40];
	a = np.asarray(a)
	a = a.astype(np.float32, copy=False)
	with mrcfile.new('cutBoxes/'+str(x_coord)+'_'+str(y_coord)+'.mrc') as mrc1:
		mrc1.set_data(a)      
    	 
def main():
	fname = 'demo.png'
	neighborhood_size = 4
	threshold = 17
#data = scipy.misc.imread(fname)
#print type(data)
	with mrcfile.open('final.mrc') as mrc:
  		arr=mrc.data
	data=np.asarray(arr)
	picture_len=int(data.shape[0])
	data_max = filters.maximum_filter(data, neighborhood_size)
	maxima = (data == data_max)
	data_min = filters.minimum_filter(data, neighborhood_size)
	diff = ((data_max - data_min) > threshold)
	maxima[diff == 0] = 0

	labeled, num_objects = ndimage.label(maxima)
	slices = ndimage.find_objects(labeled)
	x, y = [], []
	for dy,dx in slices:
         x_center = (dx.start + dx.stop - 1)/2
         y_center = (dy.start + dy.stop - 1)/2  
    	 if x_center<picture_len-200 and y_center<picture_len-200 and x_center>200 and y_center>200:
    		 x.append(x_center)  
    		 y.append(y_center)
	arr_len=len(x)
	for i in range(0,arr_len):
		cutBoxes(x[i],y[i])


if __name__ == "__main__":
    main()
