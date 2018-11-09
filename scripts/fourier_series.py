@interact
def _(f = input_box(default=exp(x)), n = slider(1, 12, 1, default=5, label="n")):
    g = piecewise([((0,pi), f)])
    p = plot(g, (0,pi), thickness=3, rgbcolor=(0.1,0.4,0.9))
    ymin = p.get_axes_range()['ymin']
    ymax = p.get_axes_range()['ymax']
    sine_series = [p + plot(g.fourier_series_partial_sum(n), (x,0,pi), ymin=ymin, ymax=ymax, thickness=3, rgbcolor=(0.9,0,0.4)) for n in sxrange(0,n,1)]
    show(animate(sine_series))