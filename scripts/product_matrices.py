@interact
def _(m = input_box(default = 3, label='m'), p = input_box(default = 4, label='p'), n = input_box(default = 2, label='n')):
    @interact
    def _(Ain = input_grid(m, p, default = [[(j+1)*(k+1)+j+k for k in range(p)] for j in range(m)], label = 'A = ', to_value=matrix),\
          Bin = input_grid(p, n, default = [[(j+1)*(k+1)+j+k for k in range(n)] for j in range(p)], label = 'B = ', to_value=matrix)):
        A = matrix(QQ,Ain)
        B = matrix(QQ,Bin)
        C=A*B
        pretty_print(latex(A)+latex(B)+'='+latex(C))