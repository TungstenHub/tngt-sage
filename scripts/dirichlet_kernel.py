t = var('t')
dirichlet_kernel = [plot(sum([cos(i*t) for i in range(-n,n)]), (t,-pi,pi), ymin=-10, ymax=10, thickness=3, rgbcolor=(0.1,0.4,0.9)) for n in range(0,20)]
animate(dirichlet_kernel)