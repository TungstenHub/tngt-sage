radius = 100

graph_color = 'steelblue'
cosine_arrow_color = 'deepskyblue'
cosine_color = 'mediumseagreen'
angle_color = 'salmon'

def cosine_and_unit_circle(angle=30):
	ccenter_x, ccenter_y = -2*radius, 0
	cosine_x = angle
	current_y = circle_y = radius * sin(angle*pi/180)
	circle_x = ccenter_x + radius * cos(angle*pi/180)
	cosine_y = radius * cos(angle*pi/180)
	graph = Graphics()

	unit_circle = circle((ccenter_x, ccenter_y), radius, color=graph_color)

	x = var('x')
	cosine = plot( radius * cos(x*pi/180) , (x, 0, 360), color=graph_color )
	graph += unit_circle + cosine

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

	graph += arrow( [cosine_x,0], [cosine_x, cosine_y], width=1, arrowsize=3, color=cosine_arrow_color)
	graph += arrow( [ccenter_x,circle_y], [circle_x, circle_y], width=1, arrowsize=3, color=cosine_arrow_color)
	
	graph += line(([circle_x, current_y], [circle_x, cosine_y]), rgbcolor=cosine_color, linestyle = "--", alpha=0.5)
	graph += line(([circle_x, cosine_y], [cosine_x, cosine_y]), rgbcolor=cosine_color, linestyle = "--", alpha=0.5)
	graph += text("$(%d^{\circ}, %3.2f)$"%(cosine_x, float(cosine_y)/radius), [cosine_x+40, cosine_y], color = cosine_color)

	graph += line( [[ccenter_x, ccenter_y], [circle_x, circle_y]],rgbcolor='gray')
	
	graph += line( [[0,0], [cosine_x, 0]],  color=angle_color, thickness=1.5)
	graph += disk( (ccenter_x, ccenter_y), float(radius)/4, (0, angle*pi/180), color=angle_color, fill=True, thickness=1.5)
	
	
	show (graph, xmin = -3*radius-40, xmax = 360+40, ymin = -(radius+30), ymax = radius+30, aspect_ratio=1, axes = False, figsize=10)

@interact
def _( angle = slider([0..360], default=30, step_size=5,
label="Angle: ", display_value=True) ):
	cosine_and_unit_circle(angle)