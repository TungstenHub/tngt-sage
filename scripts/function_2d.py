var('x y')
@interact
def _(f = input_box(default=(x**4+y**4)/(x**2+y**2)), xrange = slider(1, 10, 1, 2), yrange = slider(1, 10, 1, 2)):
    show(plot3d(f, (x,-xrange,xrange), (y,-yrange,yrange), rgbcolor='cadetblue', opacity=0.9), viewer='threejs')