import random

@interact
def _(reload=selector(['Load random triangle'],buttons=True, label='')):
    
    A = vector([10*random.random(),10*random.random()])
    B = vector([10*random.random(),10*random.random()])
    C = vector([10*random.random(),10*random.random()])

    a = C-B
    b = A-C
    c = B-A

    I = CC.0
    b_angle=(-b[0]-I*b[1]).argument()
    c_angle=(c[0]+I*c[1]).argument()

    if c_angle-b_angle >= pi:
        b_angle += 2*pi
        angle = b_angle-c_angle
        minor = 'c'
    elif b_angle-c_angle >= pi:
        c_angle += 2*pi
        angle = c_angle-b_angle
        minor = 'b'
    elif c_angle <= b_angle:
        angle = b_angle-c_angle
        minor = 'c'
    else:
        angle = c_angle-b_angle
        minor = 'b'
    
    @interact
    def _(sol=checkbox(False, label='Show solution')):
                
        g = Graphics()

        g += text(r"$\alpha="+str((angle*180/pi).n(digits=4))+"^\circ$", A-1.2*(c-b).normalized(), color='steelblue', fontsize=20)
        
        g += line([A, B], thickness=3, color='steelblue')
        g += line([A, C], thickness=3, color='steelblue')
        g += line([B, C], thickness=3, color='darkred', linestyle='--')
        
        if minor == 'b':
            g += arc(A, 0.5, sector=(b_angle,c_angle), thickness=3, color='steelblue')
            if sol:
                g += text("$a="+str(a.norm().n(digits=3))+"$", (B+C)/2+1.2*(vector([-a[1],a[0]])).normalized(), color='darkred', fontsize=20)
            else:
                g += text("$?$", (B+C)/2+0.7*(vector([-a[1],a[0]])).normalized(), color='darkred', fontsize=20)
            g += text("$b="+str(b.norm().n(digits=3))+"$", (C+A)/2+1.2*(vector([-b[1],b[0]])).normalized(), color='steelblue', fontsize=20)
            g += text("$c="+str(c.norm().n(digits=3))+"$", (A+B)/2+1.2*(vector([-c[1],c[0]])).normalized(), color='steelblue', fontsize=20)
        else:
            g += arc(A, 0.5, sector=(c_angle,b_angle), thickness=3, color='steelblue')
            if sol:
                g += text("$a="+str(a.norm().n(digits=3))+"$", (B+C)/2-1.2*(vector([-a[1],a[0]])).normalized(), color='darkred', fontsize=20)
            else:
                g += text("$?$", (B+C)/2-0.7*(vector([-a[1],a[0]])).normalized(), color='darkred', fontsize=20)
            g += text("$b="+str(b.norm().n(digits=3))+"$", (C+A)/2-1.2*(vector([-b[1],b[0]])).normalized(), color='steelblue', fontsize=20)
            g += text("$c="+str(c.norm().n(digits=3))+"$", (A+B)/2-1.2*(vector([-c[1],c[0]])).normalized(), color='steelblue', fontsize=20)
            
        if sol:
            bb=str(b.norm().n(digits=3))
            cc=str(c.norm().n(digits=3))
            aa=str((angle*180/pi).n(digits=4))
            sq=b.norm()^2+c.norm()^2-2*b.norm()*c.norm()*cos(angle)
            pretty_print(html(r'$$a^2=b^2+c^2-2bc\cos(\alpha)='+bb+'^2+'+cc+r'^2-2\times'+bb+r'\times'+cc+r'\times\cos('+aa+'^\circ)='+str(sq.n(digits=3))+'$$'))
            pretty_print(html(r'$$a=\sqrt{'+str(sq.n(digits=3))+'}='+str(sqrt(sq).n(digits=3))+'$$'))
    
        show(g, axes=False)