from sage.misc import prandom
 
def m():
	if prandom.randint(0,1):
		return prandom.uniform(-1,1)
	else:
		return prandom.gauss(0,2)
		
@interact
def _(trials = slider([20,40,..,10000], default=1000, label="$n$"), zoom=range_slider([-10,-9,..,10], default=(-5,5))):
	values = [(x, m()) for x in range(trials)]
	p1 = points(values, rgbcolor=(0.1,0.1,0.2), pointsize=10, ymin=zoom[0], ymax=zoom[1], ticks=[[],[zoom[0],zoom[0]+1,..,zoom[1]]], tick_formatter=[[],['']*(zoom[1]-zoom[0]+1)])
	p2 = plot(lambda x:sum(v[1] <= x for v in values)/trials, (x,zoom[0],zoom[1]))
	g = graphics_array([p1, p2])
	g.show(figsize=[12,4])