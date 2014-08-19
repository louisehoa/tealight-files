from tealight.logo import (move, turn,
                           pen_down, pen_up,
                           show_turtle, hide_turtle,
                           color, speed)

def square(side):
  for i in range(0,4):
    move(side)
    turn(90)

square( 4)