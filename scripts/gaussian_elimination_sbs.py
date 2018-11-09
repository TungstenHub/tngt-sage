@interact
def _(num_rows = input_box(default = 3, label='n. rows'), num_cols = input_box(default = 4, label='n. columns')):
	@interact
	def _(Min = input_grid(num_rows, num_cols, default = [[(j+1)*(k+1)+j+k for k in range(num_cols)] for j in range(num_rows)], label = 'A = ', to_value=matrix)):
	
		M = matrix(QQ,Min)
		pretty_print(M)

		col = 0   # all cols before this are already done
		pivots = [] # keeps track of pivots
		for row in range(0,num_rows):
			# ?Need to swap in a nonzero entry from below
			while (col < num_cols
				   and M[row][col] == 0):
				found_pivot = False
				for i in M.nonzero_positions_in_column(col):
					if i > row:
						pretty_print(html( " Swap row " + str(row+1) + " with row " + str(i+1) ))
						M.swap_rows(row,i)
						pretty_print(M)
						found_pivot = True
						break
				if not found_pivot:
					col += 1

			if col >= num_cols:
				break

			# Now guaranteed M[row][col] != 0
			pivots.insert(0,[row,col])
			if (M[row][col] != 1):
				pretty_print(html(  " Multiply row " + str(row+1) + " by " + str(1/M[row][col]) ))
				M.rescale_row(row,1/M[row][col])
				pretty_print(M)
			change_flag=False
			for changed_row in range(row+1,num_rows):
				if M[changed_row][col] != 0:
					change_flag=True
					factor=-1*M[changed_row][col]/M[row][col]
					pretty_print(html( " Take " + str(factor) + " times row " + str(row+1) + " and add it to row " + str(changed_row+1) ))
					M.add_multiple_of_row(changed_row,row,factor)
			if change_flag:
				pretty_print(M)
			col +=1
			
			
		for pivot in pivots:
			change_flag=False
			row = pivot[0]
			col = pivot[1]
			for k in range(row):
				if M[k][col] != 0:
					change_flag=True
					pretty_print(html( " Take " + str(-M[k][col]) + " times row " + str(row+1) + " and add it to row " + str(k+1) ))
					M.add_multiple_of_row(k,row,-M[k][col])
			if change_flag:
				pretty_print(M)