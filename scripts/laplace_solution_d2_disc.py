r, th, z = var('r th z')
@interact
def _(a = (0,(-3,3))):
	s = plot3d(lambda r,th: numerical_integral((1-r**2)/(2*pi*(1+r**2-2*r*cos(th-x))), a, pi)[0], (r,0,0.99), (th,0,2*pi), transformation=(r*cos(th),r*sin(th),z), rgbcolor=(1,1,0), opacity=0.7, plot_points=[10,200])
	b0 = parametric_plot3d((cos, sin, 0), (-pi,a), thickness=5, color='darkred')
	b1 = parametric_plot3d((cos, sin, 1), (a,pi), thickness=5, color='cadetblue')
	show(s+b0+b1, viewer='threejs', axes_labels=False)