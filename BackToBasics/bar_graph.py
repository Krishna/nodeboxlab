
def graph(str, ox, oy):
    str_width = textwidth(str)
    str_height = textheight(str) 
    text(str, ox, oy + str_height)

    gap = 10
    bar_height = 10
    
    bar_x = max([ox + str_width + gap, 130])
    bar_y = oy + str_height 
    rect(bar_x, bar_y, str_width, -str_height/2)

graph("Strawberry", 10, 0)
graph("Apple", 10, 40)
graph("Pears", 10, 80)
graph("Markov Chains", 10, 120)