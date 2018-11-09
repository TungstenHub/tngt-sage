@interact
def _(D = input_box(default = 3, label = 'dim = ')):
	@interact
	def _(Min = input_grid(D,D, default = [[1 if k==j else (-1 if k+1==j else 0) for k in range(D)] for j in range(D)], label = 'A = ', to_value=matrix)):
	
		M = matrix(AA,Min)
		pretty_print(html( "The eigenvalues of" ))
		pretty_print(M)
		pretty_print(html( "are" ))
		pretty_print([ev.radical_expression() for ev in M.eigenvalues()])