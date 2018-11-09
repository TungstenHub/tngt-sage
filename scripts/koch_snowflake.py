def subdivideLine(a, b):
    x1 = a[0] ; x2 = b[0]
    y1 = a[1] ; y2 = b[1]
    p1 = ( (2*x1 + x2)/3, (2*y1 + y2)/3 )  
    p2 = ( (1/6)*(3*x1 + sqrt(3)*y1 + 3*x2 -sqrt(3)*y2), (1/6)*(-sqrt(3)*x1 + 3*y1 + sqrt(3)*x2 + 3*y2) ) 
    p3 = ( (x1 + 2*x2)/3, (y1 + 2*y2)/3 ) 
    return [a, p1, p2, p3]

def kochFractal(base_points, iterations):
    points = base_points
    for _ in range(iterations):
        new_points = [] 
        for k in range(len(points)-1): 
            new_points += subdivideLine( points[k], points[k+1] )
        new_points += subdivideLine( points[-1], points[0] )
        points = new_points
    return points

@interact
def _(iter=slider(0, 7, 1, default=4)):
    show(polygon(kochFractal([(0,0),(1/2,sqrt(3/4)),(1,0)], iter), color='whitesmoke', edgecolor='steelblue'), axes=False, aspect_ratio=1)