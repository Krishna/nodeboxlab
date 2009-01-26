import math

width = 300
height = 300
size(width, height)

def dot(x, y, dot_size = 3):
    oval(x - dot_size/2, y - dot_size/2, dot_size, dot_size)

def draw_axis():
    stroke(0.2)
    strokewidth(2)
    line(0, height/2, width, height/2)
    line(width/2, 0, width/2, height)    
    

draw_axis()

# just some dots to show the old co-od space...
dot(0,0)
dot(width-3, height-3)

translate(width/2, height/2)

stroke(1.0, 0.0, 0.5)
dot(0, 60)
