from gpiozero import Button
from signal import pause

def button_0():
  print("Button 0")

def button_1():
  print("Button 1")

def button_2():
  print("Button 2")

def button_3():
  print("Button 3")

def button_4():
  print("Button 4")

def button_5():
  print("Button 5")

def button_6():
  print("Button 6")

def button_7():
  print("Button 7")

def button_8():
  print("Button 8")

def button_9():
  print("Button 9")

buttonPins = [2, 3, 4, 14, 15, 18, 17, 27, 22, 23]
buttonFunc = [button_0, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]

def setup_button(pin, index):
  button = Button(pin)
  button.when_pressed = buttonFunc[index]

for i, pin in enumerate(buttonPins):
  setup_button(pin, i)

pause()