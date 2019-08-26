import math
def mandel(real, imag):
	""" code to generate fractal images
	"""
	x = 0
	y = 0
	for i in range(0,257):
		if x*x + y*y > 4.0:
			break
		xt = real + x*x - y *y
		y = imag + 2.0 * x * y
		x = xt
	return int(math.log(i) * 256 / math.log(256))-1

def mandelbrot(size_x,size_y):
	"""
	size_x = image_width
	size_y = image_height
	Returns:
	A list of integer range of (0,255)
	"""

	return [[mandel((3.5 * x / size_x)-2.5,
		        (2.0 * y / size_y)-1.0)
	          for x in range(size_x)]
	          for y in range(size_y)]





