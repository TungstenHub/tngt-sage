r, t, z = var('r t z')
trans=(r*cos(t),r*sin(t),z)
plot3d(min_symbolic((1-r**2)/(1+r**2-2*r*cos(t)),2),(r,0,1),(t,0,2*pi),transformation=trans, rgbcolor=(0,0.5,1), opacity=0.7, plot_points=[50,200], viewer='threejs', axes_labels=False) ## cut-off