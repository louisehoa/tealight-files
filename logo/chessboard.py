from tealight.logo import move, turn

def square(side):
  for i in range(0,4):
    move(side)
    turn(90)

for count in range(0,8):
    square(30)
    move(30)
