from tealight.logo import move, turn

def square(side):
  for i in range(0,4):
    move(side)
    turn(90)

for count2 in range(0,64):
  turn(180)
  for count in range(0,64):
     square(30)
     move(30)
      
    
