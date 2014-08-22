from tealight.net import(connect, send)

connect ('Dinosaurs.py')
message = "Meerkat"
send(message)

def handle_message(message):
  print "You have one message: " + str(message)