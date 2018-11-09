w = 3

def concept_derivative(f,xx):
    df = diff(f)
    fval = f(x=xx)
    dfval = df(x=xx)
    
    graph = Graphics()

    t = var('t')
    fplot = plot(f(x=t+w+1) ,(t,-2*w-1,-1), color='steelblue', thickness=2)
    dfplot = plot(df(x=t-w-1) ,(t,1,2*w+1), color='steelblue', thickness=2)
    graph += fplot + dfplot

    graph += line( [[-2*w-1,0], [-1, 0]],rgbcolor='black')
    graph += line( [[1,0], [2*w+1, 0]],rgbcolor='black')
    graph += line( [[-w-1,-2], [-w-1, 2]],rgbcolor='black')
    graph += line( [[+w+1,-2], [+w+1, 2]],rgbcolor='black')
    
    graph += line( [[-w-1+xx,0], [-w-1+xx, fval]],rgbcolor='gray')
    graph += line( [[-w-1+xx, fval], [-w+xx, fval]],rgbcolor='gray')
    
    graph += line( [[-w-1+xx, fval], [-w+xx, fval+dfval]],rgbcolor='salmon', thickness=2)
    
    graph += line( [[-w+xx, fval+dfval], [w+1+xx, dfval]],rgbcolor='orange', linestyle = "--")
    graph += line( [[-w+xx, fval], [w+1+xx, 0]],rgbcolor='orange', linestyle = "--")
    
    graph += arrow( [-w+xx, fval], [-w+xx, fval+dfval],rgbcolor='orange', thickness=2)
    graph += arrow( [w+1+xx, 0], [w+1+xx, dfval],rgbcolor='orange', thickness=2)

    show (graph, xmin = -7, xmax = 7, ymin = -3, ymax = 3, aspect_ratio=1, axes = False, figsize=8)

@interact
def _( f = input_box(default=sin(x)), x = (0.5,(-w,w))):
    concept_derivative(f,x)