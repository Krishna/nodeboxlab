width = 640
height = 480
size(width, height)

def vertical_dots(x, step, dot_width, dot_height):
    for y in range(0, height, step):
        oval(x, y, dot_width, dot_height)

def vertical_uniform_dots(x, step, dot_size):
    vertical_dots(x, step, dot_size, dot_size)


x_pos = 3       # the x co-od of the line of dots
step = 5        # the vertical gap between the dots
dot_size = 1    # the size of the dots

for i in range(3, width, 2):
    vertical_uniform_dots(x_pos, step, dot_size)
    x_pos += 10 + (x_pos/3)
    step += 6
    dot_size += 1

"""
vertical_uniform_dots(3, 5, 1)
vertical_uniform_dots(13, 8, 2)
vertical_uniform_dots(26, 12, 3)
"""
