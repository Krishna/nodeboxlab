width = 640
height = 480
size(width, height)

def dot(x, y, dot_size = 3):
    oval(x, y, dot_size, dot_size)
    
dot_size = 5
for i in range(0, 400, 20):
    x = (width/2)
    y = i

    dot(x, y, dot_size)
    dot_size += 1