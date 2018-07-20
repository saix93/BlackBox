from gpiozero import Button
from signal import pause

def button_A():
    print("Button A pressed")

def button_B():
    print("Button B pressed")

def button_C():
    print("Button C pressed")

def button_D():
    print("Button D pressed")

def button_E():
    print("Button E pressed")

def button_F():
    print("Button F pressed")

def button_G():
    print("Button G pressed")

def button_H():
    print("Button H pressed")

def button_I():
    print("Button I pressed")

def button_J():
    print("Button J pressed")

buttonPins = [2, 3, 4, 14, 15, 18, 17, 27, 22, 23]
buttonFunc = [button_A, button_B, button_C, button_D, button_E, button_F, button_G, button_H, button_I, button_J]

buttonsArr = []

# Bucle que recoge todos los pines que se utilizan en la BlackBox
for index, pin in enumerate(buttonPins):
    print("Button " + buttonFunc[index].__name__[-1:] + " initialized in pin " + str(pin) + ".")
    button = Button(pin)
    button.when_pressed = buttonFunc[index]
    buttonsArr.append(button)

pause()
