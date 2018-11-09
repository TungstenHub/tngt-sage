var('x y')
@interact
def _(f = input_box(default=(-y,x)), xrange = slider(1, 10, 1, 3), yrange = slider(1, 10, 1, 3)):
    show(plot_vector_field(f, (x,-xrange,xrange), (y,-yrange,yrange), aspect_ratio=1, color='darkcyan'))