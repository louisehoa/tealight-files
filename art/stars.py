from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import sin, cos, pi

def star(x, y, c, size, spines, width, height):
  
  color(c)
  
  angle = 0
  
  for i in range(0, spines):
    x0 = x + ((size * width) * sin(angle))
    y0 = y + ((size * height) * cos(angle))
    
    x1 = x + ((size * width) * sin(angle + (2 * pi / spines)))
    y1 = y + ((size * height) * cos(angle + (2 * pi / spines)))
    
    line(x0, y0, x1, y1)
    
    angle = angle + (2 * pi / spines)
   

star(300, 400, "blue", 100, 30, 1, 1)
star(600, 400, "purple", 200, 100, 2, 1)
star(450, 200, "orange", 125, 30, 1, 1)
