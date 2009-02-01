import math

x = 10
y = 10
orig_width = width = 100
height = 50

rect(x, y, width, height)

y += 100

width = orig_width + orig_width
rect(x, y, width, height)
print width
print "--"

y += 100

width = orig_width * math.e ** (1 * 1)
rect(x, y, width, height)
print width

y += 100
rect(x, y, math.e , height)