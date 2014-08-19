from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
while touch() != 'wall':
  look()
  left_side(1)
  move(1)
  if touch() == 'wall':
    turn(-1)
    if touch () == 'wall':
      turn(-2)
    if touch () == 'wall':
      turn(1)
      

    