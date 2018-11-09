ab_range = [a.n(digits = 1) for a in [-5,-4.9,..,5]]
ab_range[50] = 0
	
@interact
def _(a = slider(ab_range, default=-2, label="$a$"), b = slider(ab_range, default=2, label="$b$")):
	values = [(x, sage.misc.prandom.uniform(a, b)) for x in [0,0.01,..,50]]
	show(points(values, rgbcolor=(0.1,0.1,0.2), pointsize=10, ymin=-5, ymax=5, ticks=[[],[-5,-4,..,5]], tick_formatter=[[],['']*11]))