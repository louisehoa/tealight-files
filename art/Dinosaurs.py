from tealight.net import(connect, send)

connect ('Dinosaurs.py')
message = ("I'm the meerkat gaaaldem")
send(message)

def handle_message(message):
  print "Received message: " + str(message)