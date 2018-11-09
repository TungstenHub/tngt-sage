R.<x, y> = QQbar[]

@interact
def _(eq = input_box(default='3*(x-7+2*y) = 5*(x/4)-(y/3+2)', type = str, label = 'Equation: ')):
	
	pretty_print(html( 'Your initial equation is' ))
	pretty_print(html( '$$' + str(eq).replace('', '') + '$$' ))
	
	eq_sides = eq.replace(" ", "").split('=')
	if len(eq_sides) != 2:
		pretty_print(html( '!! The equation must have to mathematical expressions separated separated by an = ' ))
		return None
	
	pretty_print(html( 'We simplify the LHS of the first equation' ))
	eqlhs = sage_eval(eq_sides[0], locals={'x':x, 'y':y})
	pretty_print(html( '$' +
					   str(eq_sides[0]).replace('*', '') +
					   '\,\longrightarrow\,' +
					   latex(eqlhs) +
					   '$' ))
	
	pretty_print(html( 'We simplify the RHS of the first equation' ))
	eqrhs = sage_eval(eq_sides[1], locals={'x':x, 'y':y})
	pretty_print(html( '$' +
					   str(eq_sides[1]).replace('*', '') +
					   '\,\longrightarrow\,' +
					   latex(eqrhs) +
					   '$' ))
	
	if eqlhs.degree() > 1:
		pretty_print(html( '!! The LHS is not a linear expression' ))
		return None
	if eqrhs.degree() > 1:
		pretty_print(html( '!! The RHS is not a linear expression' ))
		return None
		
	pretty_print(html( 'Now we face the following equation:' ))
	pretty_print(html( '$' +
					   latex(eqlhs) +
					   '=' +
					   latex(eqrhs)
					   + '$' ))
		
	pretty_print(html( 'Let\'s restructure the equation:' ))
	coefx0 = eqlhs.coefficient({x:1,y:0})
	coefy0 = eqlhs.coefficient({x:0,y:1})
	coefu0 = eqlhs.coefficient({x:0,y:0})
	coefx1 = eqrhs.coefficient({x:1,y:0})
	coefy1 = eqrhs.coefficient({x:0,y:1})
	coefu1 = eqrhs.coefficient({x:0,y:0})
	pretty_print(latex(coefx0) + 'x' + ('' if (sgn(-coefx1) == -1) else '+') +
				 latex(-coefx1)+ 'x' + ('' if (sgn( coefy0) == -1) else '+') +
				 latex(coefy0) + 'y' + ('' if (sgn(-coefy1) == -1) else '+') +
				 latex(-coefy1)+ 'y' +
				 '=' +
				 latex(coefu1) + ('' if (sgn(-coefu0) == -1) else '+') +
				 latex(-coefu0))
	
	pretty_print(html( 'We add everything up' ))
	pretty_print(latex(coefx0-coefx1) + 'x' + ('' if (sgn(coefy0-coefy1) == -1) else '+') +
				 latex(coefy0-coefy1) + 'y' +
				 '=' +
				 latex(coefu1-coefu0) )