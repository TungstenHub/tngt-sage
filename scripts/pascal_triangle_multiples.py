@interact
def _(p=2, n=64):

    g = Graphics()
    
    for i in range(n):
        for j in range(i+1):
            g += circle((j-i/2,-sqrt(3)*i/2), 0.4, fill=True, rgbcolor='steelblue' if binomial(i,j)%p==0 else 'whitesmoke')
            
    show(g, axes=False)