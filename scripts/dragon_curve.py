def transf1(p):
    x = p[0]
    y = p[1]
    return [(x-y)/2,(x+y)/2]
    
def transf2(p):
    x = p[0]
    y = p[1]
    return [1-(x+y)/2,(x-y)/2]

def duplicate(l):
    l1 = [transf1(p) for p in l]
    l2 = [transf2(p) for p in l]
    return l1[:-1] + l2[::-1] 

def dragonCurve(iterations):
    points = [[0,0],[1,0]]
    for _ in range(iterations):
        points = duplicate(points) 
    return points

@interact
def _(iter=slider(0, 18, 1, default=16)):
    show(line(dragonCurve(iter), color='steelblue'), axes=False, aspect_ratio=1)