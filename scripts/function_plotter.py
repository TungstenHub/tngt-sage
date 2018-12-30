@interact 
def _(f = input_box(default=sin(x**2)), xrange = slider(1, 10, 1, 3)):
    show(plot(f,(x,-xrange,xrange), thickness=3, rgbcolor=(0.1,0.4,0.9)))