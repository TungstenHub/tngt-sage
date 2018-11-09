var('x y')
@interact
def _(f = input_box(default=(-y,x)), xrange = range_slider([-20,-19,..,20], default=(-3, 3)), yrange = range_slider([-20,-19,..,20], default=(-3, 3))):
	v = plot_vector_field(f, (x,xrange[0],xrange[1]), (y,yrange[0],yrange[1]), aspect_ratio=1)
	s = streamline_plot(f, (x,xrange[0],xrange[1]), (y,yrange[0],yrange[1]), aspect_ratio=1)
	show(graphics_array([v,s]))