var('z')
@interact
def _(f = input_box(default=z^5 + z - 1 + 1/z), r_rg = slider(1, 10, 1, 4), i_rg = slider(1, 10, 1, 3)):
	show(complex_plot(f, (-r_rg,r_rg), (-i_rg,i_rg), aspect_ratio=1))