def matrix_step(m,p,n,A,B,piv_i,piv_k,piv_j):
    
    pad = 0.1
    line_color='steelblue'
    piv_color='mediumseagreen'
    
    C=A*B
    
    x1=0
    y1=-m/2
    x2=p+1
    y2=-p/2
    x3=p+1+n+1
    y3=-m/2
    
    g1 = Graphics()
    g2 = Graphics()
    g3 = Graphics()
    
    g1 += polygon([(x1+0,y1+m-piv_i-1), (x1+p,y1+m-piv_i-1), (x1+p,y1+m-piv_i), (x1+0,y1+m-piv_i)], color=line_color)
    g1 += polygon([(x1+piv_k+pad,y1+m-piv_i-1+pad), (x1+piv_k+1-pad,y1+m-piv_i-1+pad), (x1+piv_k+1-pad,y1+m-piv_i-pad), (x1+piv_k+pad,y1+m-piv_i-pad)], color=piv_color)
    
    g2 += polygon([(x2+piv_j,y2+0), (x2+piv_j+1,y2+0), (x2+piv_j+1,y2+p), (x2+piv_j,y2+p)], color=line_color)
    g2 += polygon([(x2+piv_j+pad,y2+p-piv_k-1+pad), (x2+piv_j+1-pad,y2+p-piv_k-1+pad), (x2+piv_j+1-pad,y2+p-piv_k-pad), (x2+piv_j+pad,y2+p-piv_k-pad)], color=piv_color)
    
    g3 += polygon([(x3+0,y3+m-piv_i-1), (x3+n,y3+m-piv_i-1), (x3+n,y3+m-piv_i), (x3+0,y3+m-piv_i)], color=line_color)
    g3 += polygon([(x3+piv_j,y3+0), (x3+piv_j+1,y3+0), (x3+piv_j+1,y3+m), (x3+piv_j,y3+m)], color=line_color)
    g3 += polygon([(x3+piv_j+pad,y3+m-piv_i-1+pad), (x3+piv_j+1-pad,y3+m-piv_i-1+pad), (x3+piv_j+1-pad,y3+m-piv_i-pad), (x3+piv_j+pad,y3+m-piv_i-pad)], color=piv_color)
    
    for i in range(m):
        for k in range(p):
            g1 += text(A[i,k],(x1+k+0.5,y1+m-i-0.5),rgbcolor=(0, 0, 0),fontsize=25)
            
    for k in range(p):
        for j in range(n):
            g2 += text(B[k,j],(x2+j+0.5,y2+p-k-0.5),rgbcolor=(0, 0, 0),fontsize=25)
            
    for i in range(piv_i):
        for j in range(n):
            g3 += text(C[i,j],(x3+j+0.5,y3+m-i-0.5),rgbcolor=(0, 0, 0),fontsize=25)
            
    for j in range(piv_j):
        g3 += text(C[piv_i,j],(x3+j+0.5,y3+m-piv_i-0.5),rgbcolor=(0, 0, 0),fontsize=25)
        
    curr_sum = sum([A[piv_i,k]*B[k,piv_j] for k in range(piv_k+1)])
    g3 += text(curr_sum,(x3+piv_j+0.5,y3+m-piv_i-0.5),rgbcolor=(0, 0, 0),fontsize=25)
    
    g3 += text(r'$\times$',(p+0.5,0),rgbcolor=(0, 0, 0),fontsize=25)
    g3 += text('$=$',(p+1+n+0.5,0),rgbcolor=(0, 0, 0),fontsize=25)
    
    g1 += polygon([(x1+0,y1+0), (x1+p,y1+0), (x1+p,y1+m), (x1+0,y1+m)], fill=False, thickness=4, color='black')
    g2 += polygon([(x2+0,y2+0), (x2+n,y2+0), (x2+n,y2+p), (x2+0,y2+p)], fill=False, thickness=4, color='black')
    g3 += polygon([(x3+0,y3+0), (x3+n,y3+0), (x3+n,y3+m), (x3+0,y3+m)], fill=False, thickness=4, color='black')
            
    return g1+g2+g3 
    
@interact
def _(m = input_box(default = 3, label='m'), p = input_box(default = 4, label='p'), n = input_box(default = 2, label='n')):
    @interact
    def _(Ain = input_grid(m, p, default = [[(j+1)*(k+1)+j+k for k in range(p)] for j in range(m)], label = 'A = ', to_value=matrix),\
          Bin = input_grid(p, n, default = [[(j+1)*(k+1)+j+k for k in range(n)] for j in range(p)], label = 'B = ', to_value=matrix),\
          delay = slider([10..300], default=50, step_size=5, label="Delay: ", display_value=True)):
        A = matrix(QQ,Ain)
        B = matrix(QQ,Bin)
        steps = [matrix_step(m,p,n,A,B,i,k,j) for i in range(m) for j in range(n) for k in range(p)]
        a = animate(steps,axes=False)
        a.show(delay=delay)