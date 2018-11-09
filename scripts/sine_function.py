radius = 100

graph_color = 'steelblue'
sine_arrow_color = 'deepskyblue'
sine_color = 'mediumseagreen'
angle_color = 'salmon'

def sine_and_unit_circle(angle=30):
	ccenter_x, ccenter_y = -2*radius, 0
	sine_x = angle
	current_y = circle_y = sine_y = radius * sin(angle*pi/180)
	circle_x = ccenter_x + radius * cos(angle*pi/180)
	graph = Graphics()

	unit_circle = circle((ccenter_x, ccenter_y), radius, color=graph_color)

	x = var('x')
	sine = plot( radius * sin(x*pi/180) , (x, 0, 360), color=graph_color )
	graph += unit_circle + sine

	graph += text("$(0, 0)$", [-2*radius-24, -16], color = 'black')
	graph += text("$(1, 0)$", [-radius+24, -16], color = 'black')
	graph += text("$(0, 1)$", [ccenter_x-24, radius+15], color = 'black')
	
	graph += line( [[ccenter_x,-radius-40], [ccenter_x, radius+40]], color = 'black' )
	graph += line( [[-3*radius-40, 0], [-radius+40, 0]], color = 'black' )

	graph += arrow( [0-20,0], [360+20, 0], color = 'black', width=1, arrowsize=3 )
	
	for x in range(0, 361, 30):
		graph += point( [x, 0] )
		angle_label = ". $%3d^{\circ}$ " % x
		angle_label += " $(%s\pi) $"% str(x/180)
		graph += text(angle_label, [x, 0], rotation=-90,
		vertical_alignment='top', fontsize=8, color='black' )

	graph += arrow( [sine_x,0], [sine_x, sine_y], width=1, arrowsize=3, color=sine_arrow_color)
	graph += arrow( [circle_x,0], [circle_x, circle_y], width=1, arrowsize=3, color=sine_arrow_color)
	
	graph += line(([circle_x, current_y], [sine_x, current_y]), rgbcolor=sine_color, linestyle = "--", alpha=0.5)
	graph += text("$(%d^{\circ}, %3.2f)$"%(sine_x, float(sine_y)/radius), [sine_x+40, current_y], color = sine_color)

	graph += line( [[ccenter_x, ccenter_y], [circle_x, circle_y]],rgbcolor='gray')
	
	graph += line( [[0,0], [sine_x, 0]],  color=angle_color, thickness=1.5)
	graph += disk( (ccenter_x, ccenter_y), float(radius)/4, (0, angle*pi/180), color=angle_color, fill=True, thickness=1.5)
	
	show (graph, xmin = -3*radius-40, xmax = 360+40, ymin = -(radius+30), ymax = radius+30, aspect_ratio=1, axes = False, figsize=8)

@interact
def _( angle = slider([0..360], default=30, step_size=5, label="Angle: ", display_value=True) ):
	sine_and_unit_circle(angle)