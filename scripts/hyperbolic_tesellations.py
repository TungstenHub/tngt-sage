cython('''
from math import pi, sin
from mpmath import sec
from libc.math cimport sqrt
import numpy as np
cimport numpy as np

cdef extern from "complex.h":
	double complex cexp(double complex)

def transf(double complex z, float d, int n):
	cdef double complex a, num, den, I
	I = complex(0,1)
	a = cexp(2*pi*I/n)
	num = (a-d**2)*z + d*(1-a)
	den = d*(a-1)*z + 1- d**2*a
	return num/den

def iter_transf(double complex z, float d, int n):
	cdef double complex w, I
	I = complex(0,1)
	if z.real < 0:
		return iter_transf(-z,d,n)
	elif z.imag < 0:
		return iter_transf(z.real-I*z.imag,d,n)
	else:
		w = transf(z,d,n)
		if abs(w) >= abs(z):
			return z
		else:
			return iter_transf(w,d,n)

def value(z,d,n):
	if abs(z) >= 0.99:
		return 0
	else:
		w = iter_transf((z-d)/(1-d*z),d,n)
		if abs(w.real) < 0.04:
			return 0
		else:
			return 1
			
def hyp_tes(int n, int c, int res):
	cdef double complex z
	cdef double d
	cdef int j, k
	cdef np.ndarray[np.uint16_t, ndim=2] m

	m = np.zeros((2*res+1,2*res+1), dtype=np.uint16)
	d = float(sqrt(-1+2/(1+sec(pi/c)*sin(pi/n))))
	for j in range(2*res+1):
		for k in range(2*res+1):
			z = complex((j/float(res)-1),(k/float(res)-1))
			m[j,k]=value(z,d,n)
	return m
''')

@interact
def _(n = slider(1, 20, 1, default=7, label="n"),
			c = slider(1, 20, 1, default=3, label="c"),
			res = slider(10, 500, 1, default=100, label="resolution")):
	if 1/n + 1/c < 1/2:
		show(matrix_plot(hyp_tes(n,c,res), cmap = [ '#FFFFFF', '#01579B' ], frame=False))
	else:
		show(LatexExpr(r'''\dfrac{1}{n}+\dfrac{1}{c}<\dfrac{1}{2}\text{ must hold}'''))