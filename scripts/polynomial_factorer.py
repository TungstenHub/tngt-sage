@interact
def _(p = input_box(default=x^5 - x^3 - x^2 - 2*x - 1, label = 'P(x) = ')):
	q.<x> = PolynomialRing(QQ, 'x')
	r.<x> = PolynomialRing(AA, 'x')
	c.<x> = PolynomialRing(QQbar, 'x')
	s.<x> = PolynomialRing(SR, 'x')
	factors = [s([coeff for coeff in list(pol[0])]) for pol in factor(q(p))]
	pretty_print(html('The factorization over the rational numbers is'))
	pretty_print(html('$$'+''.join(['\left('+latex(fact)+'\\right)' for fact in factors])+'$$'))
	factors = [s([coeff.radical_expression() for coeff in list(pol[0])]) for pol in factor(r(p))]
	pretty_print(html('The factorization over the real numbers is'))
	pretty_print(html('$$'+''.join(['\left('+latex(fact)+'\\right)' for fact in factors])+'$$'))
	factors = [s([coeff.radical_expression() for coeff in list(pol[0])]) for pol in factor(c(p))]
	pretty_print(html('The factorization over the complex numbers is'))
	pretty_print(html('$$'+''.join(['\left('+latex(fact)+'\\right)' for fact in factors])+'$$'))