var('x')

def riemann_sum(f,interval,number_of_subdivisions,endpoint_rule):
    a, b = map(QQ, interval)
    t = sage.calculus.calculus.var('t')
    func = fast_callable(f(x=t), RDF, vars=[t])
    dx = ZZ(b-a)/ZZ(number_of_subdivisions)

    xs = []
    ys = []
    for q in range(number_of_subdivisions):
        if endpoint_rule == 'Left':
            xs.append(q*dx + a)
        elif endpoint_rule == 'Midpoint':
            xs.append(q*dx + a + dx/2)
        elif endpoint_rule == 'Right':
            xs.append(q*dx + a + dx)
        elif endpoint_rule == 'Upper':
            x = find_local_maximum(func, q*dx + a, q*dx + dx + a)[1]
            xs.append(x)
        elif endpoint_rule == 'Lower':
            x = find_local_minimum(func, q*dx + a, q*dx + dx + a)[1]
            xs.append(x)
    ys = [ func(x) for x in xs ]

    rects = Graphics()
    for q in range(number_of_subdivisions):
        xm = q*dx + dx/2 + a
        x = xs[q]
        y = ys[q]
        rects += polygon([(xm-dx/2,0), (xm-dx/2,y), (xm+dx/2,y), (xm+dx/2,0)], color="#90CAF9", edgecolor="#2196F3", thickness=2)
        rects += point((x, y), marker='o', rgbcolor='#FFE082', markeredgecolor='#FFC107', size=40, zorder=3)
    min_y = min(0, find_local_minimum(func,a,b)[0])
    max_y = max(0, find_local_maximum(func,a,b)[0])

    numerical_answer = integral_numerical(func,a,b,max_points = 200)[0]
    estimated_answer = dx * sum([ ys[q] for q in range(number_of_subdivisions)])

    show(LatexExpr(r'''
        \int_{a}^{b} f(x)\mathrm{d}x = %s\\\ \sum_{i=1}^{ %s} {f(x_i) \Delta x} = %s ''' % (numerical_answer, number_of_subdivisions, estimated_answer)))
    
    show(plot(func,(x,a,b), thickness=4, color='#1565C0') + rects, xmin = a, xmax = b, ymin = min_y, ymax = max_y)
        
@interact
def _(f = input_box(default = sin(x) + 2, type = SR),
    interval=range_slider(0, 10, 1, default=(0, 4), label="Interval"),
    number_of_subdivisions = slider(1, 20, 1, default=4, label="Number of boxes"),
    endpoint_rule = selector(['Midpoint', 'Left', 'Right', 'Upper', 'Lower'], nrows=1, label="Endpoint rule")):
    
    riemann_sum(f,interval,number_of_subdivisions,endpoint_rule)