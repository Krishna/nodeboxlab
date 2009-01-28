
def graph(str, ox, oy):
    str_width = textwidth(str)
    str_height = textheight(str) 
    text(str, ox, oy + str_height)

    gap = 10
    bar_height = 10
    
    bar_x = ox + str_width + gap 
    bar_y = oy + str_height 
    rect(bar_x, bar_y, str_width, -str_height/2)

graph("Strawberry", 0, 0)
graph("Apple", 0, 40)