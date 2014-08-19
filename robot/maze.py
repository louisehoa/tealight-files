from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
while touch() != 'wall':
  look(1)
  left_side(1)
  move(1)
  if touch() == 'wall':
    look(1)
    turn(-1)
    if touch () == 'wall':
      look(1)
      turn(-2)
      

    