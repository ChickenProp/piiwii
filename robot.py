#! /usr/bin/python
from config import Config
import nunchuk
import wiringpi

def forward():
    Config.motorL.forward()
    Config.motorR.forward()

def back():
    Config.motorL.back()
    Config.motorR.back()

def stop():
    Config.motorL.stop()
    Config.motorR.stop()

nunchuk.setup()

try:
    while True:
        x,y = nunchuk.read_joy_normalized()
        if x == 0:
            if y > 0:
                forward()
            elif y == 0:
                stop()
            else:
                back()
        elif y == 0:
            if x > 0:
                Config.motorL.speed(100)
                Config.motorR.speed(-100)
            else:
                Config.motorL.speed(-100)
                Config.motorR.speed(100)

        wiringpi.delay(1000/60)
except KeyboardInterrupt:
    stop()
