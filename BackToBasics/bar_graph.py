
ox = 10
str = "Arbitary Text"
str_width = textwidth(str)
str_height = textheight(str) 
text(str, ox, 24)

gap = 10
rect(ox + str_width + gap, 0, str_width, str_height)