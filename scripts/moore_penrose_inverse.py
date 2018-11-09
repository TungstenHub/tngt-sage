@interact
def _(num_rows = input_box(default = 3, label='n. rows'), num_cols = input_box(default = 4, label='n. columns')):
	@interact
	def _(Min = input_grid(num_rows, num_cols, default = [[(j+1)*(k+1)+j+k for k in range(num_cols)] for j in range(num_rows)], label = 'A = ', to_value=matrix)):
	
		M = matrix(AA,Min)
		pretty_print(html( "The Moore-Penrose inverse of" ))
		pretty_print(M)
		pretty_print(html( "is" ))
		pretty_print(M.pseudoinverse())