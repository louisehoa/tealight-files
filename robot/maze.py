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
  left_side()
  move()
  if touch() == 'wall':
    turn(-1)
  elif touch () == 'wall':
    turn(-2)
  elif touch () == 'wall':
    turn(1)
      

    