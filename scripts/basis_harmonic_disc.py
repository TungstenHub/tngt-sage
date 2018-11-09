r, t = var('r, t')
@interact
def _(n = slider(0, 8, 1, default=3, label="n")):
    show(parametric_plot3d((r*cos(t), r*sin(t), r**n*cos(n*t)), (r,0,1), (t,0,2*pi), plot_points=[10,100], rgbcolor=(0,0.5,1), opacity=0.7, viewer='threejs'))