from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import sin, cos, pi

def star(x, y, c, size, spines):
  
  color(c)
  
  angle = 0
  
  for i in range(0, spines):
    x0 = x + (size * sin(angle))
    y0 = y + (size * cos(angle))
    
    line(x, y, x0, y0)
    
    angle = angle + (2 * pi / spines)

star(300, 400, "blue", 100, 20)
star(600, 400, "purple", 400, 100)
star(450, 200, "orange", 125, 30)