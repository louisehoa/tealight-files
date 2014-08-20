from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import sin, cos, pi

def star(x, y, c, size, spines, width, height):
  
  color(c)
  
  angle = 0
  
  width = 100
  height = 100
  
  for i in range(0, spines):
    x0 = x + ((size * width) * sin(angle))
    y0 = y + ((size * height) * cos(angle))
    
    line(x, y, x0, y0)
    
    angle = angle + (2 * pi / spines)
   

star(300, 400, "blue", 100, 30)
star(600, 400, "purple", 200, 100)
star(450, 200, "orange", 125, 30)