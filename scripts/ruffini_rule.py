@interact
def _(p = input_box(default=x^5 + x^4 - 8*x^3 + 11*x^2 - 15*x + 2, label = 'P(x) = '),
	a = input_box(default=2, type = int, label = 'Root = ')):
	
	coeffs = p.list()[::-1]
	n = len(p.list())
	ruffini_table = [[''] * (n+1),[''] * (n+1),[''] * (n+1)]
	for k in range(n):
		ruffini_table[0][k+1] = coeffs[k]
	ruffini_table[1][0] = a
	ruffini_table[2][1] = coeffs[0]
	for k in range(n-1):
		ruffini_table[1][k+2] = a * ruffini_table[2][k+1]
		ruffini_table[2][k+2] = ruffini_table[0][k+2] + ruffini_table[1][k+2]
	
	row0 = '<tr><td style="border-right: solid 2px black; padding:10px;" align="center"></td>' +\
		''.join(['<td style=" padding:10px;" align="center">' + str(k) + '</td>'\
		for k in ruffini_table[0][1:]]) + '</tr>'
	row1 = '<tr><td style="border-right: solid 2px black; padding:10px;" align="center">' +\
		str(a) + '</td>' +\
		''.join(['<td style=" padding:10px;" align="center">' + str(k) + '</td>'\
		for k in ruffini_table[1][1:]]) + '</tr>'
	row2 = '<tr><td style="border-right: solid 2px black; padding:10px;" align="center"></td>' +\
		''.join(['<td style=" padding:10px;" align="center">' + str(k) + '</td>'\
		for k in ruffini_table[2][1:-1]]) +\
		'<td style=" padding:10px; background-color:#2196F3" align="center">' +\
		str(ruffini_table[2][-1]) + '</td>' + '</tr>'
	line = '<tr style="border-bottom:2px solid black"><td colspan="100%"></td></tr>'
	pretty_print(html('<table align="center">' + row0 + row1 + line + row2 + '</table>'))
	
	
	quotient, remainder = p.maxima_methods().divide(x-a)
	pretty_print(p, '=', quotient.mul(x-a, hold=True).add(remainder))
	pretty_print(html('$$P(' + str(a) + ')=' + str(p).replace('x','(' + str(a) + ')')\
					.replace('*', '\\times') + '=' + str(remainder) + '$$'))