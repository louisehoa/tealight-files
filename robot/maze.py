from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
while touch(1) != 'wall':
  look(1)
  move(1)
  if touch(1) == 'wall':
    turn(1)
    end
    