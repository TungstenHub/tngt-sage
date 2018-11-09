mu_range = [a.n(digits = 1) for a in [-5,-4.9,..,5]] 
mu_range[50] = 0
sigma_range = [a.n(digits = 1) for a in [0.1,0.2,..,5]]
 
@interact
def _(mu = slider(mu_range, default=0, label="$\mu$"), sigma = slider(sigma_range, default=1, label="$\sigma$")):
	values = [(x, sage.misc.prandom.gauss(mu,sigma)) for x in [0,0.01,..,50]]
	show(points(values, rgbcolor=(0.1,0.1,0.2), pointsize=10, ymin=-5, ymax=5, ticks=[[],[-5,-4,..,5]], tick_formatter=[[],['']*11]))