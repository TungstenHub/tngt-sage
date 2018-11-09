x,y = var('x,y')
@interact
def _(ineqs = input_box(default=[y>=x-3,x>=-y-3,y<=5, x>=-4], label = 'Inequations: '), xr=10, yr=10):
	l = []
	for (k,ineq) in enumerate(ineqs):
		l.append(region_plot(ineq,(x,-xr,xr),(y,-yr,yr), incol=hue(0.618*k), bordercol=hue(0.618*k), borderwidth=2, alpha=0.3))
	p=region_plot(ineqs,(x,-xr,xr),(y,-yr,yr), incol='#181824', bordercol='#181824', borderwidth=2, alpha=0.8)
	show(graphics_array(l))
	show(p,axes=True,frame=False)