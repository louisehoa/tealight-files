from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
while touch() != 'wall':
  left_side()
  move()
  if touch() == 'wall':
    left_side()
    turn(-1)
  if touch() == 'wall':
    turn(2)
  if touch() == 'wall':
    turn(1)

    