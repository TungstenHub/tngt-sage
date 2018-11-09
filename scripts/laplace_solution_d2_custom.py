r, th, z = var('r th z')
@interact
def _(f = input_box(default=sin(3*x))):
	s = plot3d(lambda r,th: numerical_integral((1-r**2)/(2*pi*(1+r**2-2*r*cos(th-x)))*f, -pi, pi)[0], (r,0,0.99), (th,0,2*pi), transformation=(r*cos(th),r*sin(th),z), rgbcolor=(1,1,0), opacity=0.7, plot_points=[10,200])
	b = parametric_plot3d((cos, sin, f), (-pi,pi), thickness=5, color='cadetblue')
	show(s+b, viewer='threejs', axes_labels=False)