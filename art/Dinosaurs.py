from tealight.net import(connect, send)

connect ('Dinosaurs.py')
message = 'Meerkat'
send(message)

def handle_message(message):
  print "Received message: " + message