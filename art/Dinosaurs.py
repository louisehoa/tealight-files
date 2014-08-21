from tealight.net import(connect, send)
from tealight.art import (color, line, spot, circle, box, image, text, background)

connect ('Dinosaurs.py')
message = image(200, 100, "http://i.imgur.com/0zoXV5h.png")
send(message)

def handle_message(message):
  print "Received message: " + message