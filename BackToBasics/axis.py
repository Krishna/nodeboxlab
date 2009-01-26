import math

width = 300
height = 300
size(width, height)

def dot(x, y, dot_size = 1):
    #oval(x - dot_size/2, y - dot_size/2, dot_size, dot_size)
    oval(x, y, dot_size, dot_size)


def draw_axis():
    stroke(0.2)
    strokewidth(2)
    line(0, -height/2, 0, height)
    line(-width/2, 0, width, 0) # x-axis    
    

# just some dots to show the old co-od space...
dot(0,0)
dot(width-3, height-3)

translate(width/2, height/2)
draw_axis()
    
stroke(1.0, 0.0, 0.5)

for x in range(-width/2, width/2, 3):
    y = x
    y *= -1 # flip y co-ods to get standard cartesian axis
    dot(x, y)
