r, t = var('r, t')
poisson_kernel = [plot((1-r**2)/(2*pi*(1+r**2-2*r*cos(t))), (t,-pi,pi), ymin=-0.5, ymax=1, thickness=3, rgbcolor=(0.1,0.4,0.9)) for r in sxrange(0,1,0.05)]
animate(poisson_kernel)