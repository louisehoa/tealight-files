#from tealight.logo import (move, turn,
                           #pen_down, pen_up,
                           #show_turtle, hide_turtle,
                           #color, speed)

#def square(side):
  #for i in range(0,4):
    #move(side)
    #turn(90)

#def drawboard():
   #for count in range(0,63):
      #square(50 + (count * 10))

#drawboard()

from tealight.logo import move, turn

def spiral(size):
  
  if size > 300:
    return
  
  move(size)
  turn(90)
  spiral(size)
  
spiral(0)