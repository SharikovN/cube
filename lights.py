from machine import Pin, I2C
import neopixel, time
np = neopixel.NeoPixel(Pin(5), 14)
def success_blink():
    for i in range(14):
        np[i] = (48, 252, 3)
        np.write()
    time.sleep(0.5)
    for i in range(14):
        np[i] = (0, 0, 0)
        np.write()


def error_blink():
    for i in range(14):
        np[i] = (252, 3, 127)
        np.write()
    time.sleep(0.5)
    for i in range(14):
        np[i] = (0, 0, 0)
        np.write()

def no():
    for i in range(14):
        np[i] = (0,0,0)
        np.write()

def state(mood):
    if mood == 'sad':
        col = (128,128,128)
    elif mood == 'joy':
        col = (255,79,0)
    elif mood == "normal":
        col = (205,0,205)
    elif mood == 'ill':
        col = (100,149,237)    
    
    for i in range(14):
        np[i] = col
        np.write()

def lamp():
    for i in range(14):
        np[i] = (254,254,34)
        np.write()
    time.sleep(2)