
ox = 10
str = "Arbitary Text"
str_width = textwidth(str)
str_height = textheight(str) 
text(str, ox, 20)

gap = 10
rect(ox + str_width + gap, 10, str_width, 139)