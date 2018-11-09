@interact
def _(
a = (0.61803,(0,1))):
	c = continued_fraction(a).convergent(7)
	b = continued_fraction(c)
	flower = list_plot([(sqrt(k)*cos(2*pi*a*k),sqrt(k)*sin(2*pi*a*k)) for k in [1..300]], axes=False, aspect_ratio=1, color='yellow', size=30, marker='o', markeredgecolor='orange')
	t1 = ('$' + str(latex(b)) + '$').replace('\n','').replace('\displaystyle','').replace(' ','')
	t2 = ('$' + str(latex(b.convergents())) + '$').replace('\n','').replace('\displaystyle','').replace(' ','')
	textb1 = text(t1, (40, 0), fontsize=40, color='black')
	textb2 = text(t2, (80, 0), fontsize=20, color='black')
	g = flower + textb1 + textb2
	g.show(figsize=[9,4])