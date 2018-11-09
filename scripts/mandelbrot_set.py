cython('''
import numpy as np
cimport numpy as np
def mandelbrot_cython(float x0,float  x1,float  y0,float  y1, int N=200, int L=50):
	cdef double complex c, z, I
	cdef float deltax, deltay, R2 = 4
	cdef int h, j, k
	cdef np.ndarray[np.uint16_t, ndim=2] m
	m = np.zeros((int((y1-y0)*N),int((x1-x0)*N)), dtype=np.uint16)
	I = complex(0,1)
	delta = 1.0/N
	for j in range(int((y1-y0)*N)):
		for k in range(int((x1-x0)*N)):
			c = (x0+k*delta)+I*(y1-j*delta)
			z=0
			h=0
			while (h < L and z.real**2 + z.imag**2 < R2):
				z=z*z+c
				h+=1
			m[j,k]=h
	min = np.amin(m)
	m[m == L] = min
	return m
''')

import matplotlib.cm
x_range = [a.n(digits = 1) for a in [-2.5,-2.45,..,1]]
x_range[50] = 0
y_range = [a.n(digits = 1) for a in [-1.5,-1.45,..,1.5]]
y_range[30] = 0

@interact
def _(x_interval=range_slider(x_range, default=(-2.5, 1)),y_interval=range_slider(y_range, default=(-1.5, 1.5)),N=slider(10, 5000, 1, default=200),L=slider(1, 1000, 1, default=50),cmap = selector([key.encode("ascii") for key in matplotlib.cm.datad.keys()],default='bone')):
	m=mandelbrot_cython(x_interval[0] ,x_interval[1] ,y_interval[0] ,y_interval[1] , N, L)
	show(matrix_plot(m, cmap = cmap, frame=False))