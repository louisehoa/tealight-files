from tealight.net import(connect, send)

connect ('Dinosaurs.py')
message = (image("http://i.imgur.com/0zoXV5h.png"))
send(message)

def handle_message(message):
  print "Received message: " + str(message)