def matrix_perm_step(m,A,idx):
    
    pad = 0.1
    minus_color='salmon'
    plus_color='mediumseagreen'
    piv_color='steelblue'
    
    perm = Permutations(m)[idx]
    x1=0
    y1=-m/2
    
    g = Graphics()
    
    for k in range(m):
        g += polygon([(x1+perm[k]-1+pad,y1+m-k-1+pad), (x1+perm[k]-pad,y1+m-k-1+pad), (x1+perm[k]-pad,y1+m-k-pad), (x1+perm[k]-1+pad,y1+m-k-pad)], color=piv_color)
    
    
    for i in range(m):
        for j in range(m):
            g += text(A[i,j],(x1+j+0.5,y1+m-i-0.5),rgbcolor=(0, 0, 0),fontsize=25)
    
    g += polygon([(x1+0,y1+0), (x1+m,y1+0), (x1+m,y1+m), (x1+0,y1+m)], fill=False, thickness=4, color='black')
    
    for i in range(m):
        g += text(i+1,(m+1+i/2,1.5),rgbcolor=(0,0,0),fontsize=15)
        g += point((m+1+i/2,1.3),rgbcolor=(0,0,0))
        g += point((m+1+i/2,0.6),rgbcolor=(0,0,0))
        g += arrow((m+1+i/2,1.2),(m+0.5+perm[i]/2,0.7),rgbcolor=(0,0,0))
    
    s=perm.sign()
    g += text(r"$\times$".join([str(A[k,perm[k]-1]) for k in range(m)]),(m+0.75+m/4,-0.9),color=(plus_color if s==1 else minus_color),fontsize=25) 
       
    g += polygon([(m+0.75,0.4), (m+0.75+m*(idx+1)/(2*factorial(m)),0.4), (m+0.75+m*(idx+1)/(2*factorial(m)),0.25), (m+0.75,0.25)], color=piv_color)
    g += polygon([(m+0.75,0.4), (m+0.75+m/2,0.4), (m+0.75+m/2,0.25), (m+0.75,0.25)], fill=False, thickness=1, color='black')
    
    return g

@interact
def _(m = input_box(default = 4, label = 'dim = ')):
    @interact
    def _(Ain = input_grid(m,m, default = [[(k+1)^j for k in range(m)] for j in range(m)], label = 'A = ', to_value=matrix),\
          delay = slider([10..300], default=50, step_size=5, label="Delay: ", display_value=True)):
        
        A = matrix(QQ,Ain)
        steps = []

        for k in range(factorial(m)):
            steps.append(matrix_perm_step(m,A,k))

        a = animate(steps,axes=False)
        a.show(delay=delay)