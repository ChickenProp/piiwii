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

#Config.motorL.speed(50)
#Config.motorR.speed(-25)

try:
    while True:
        print nunchuk.read_joy_normalized()
        wiringpi.delay(500)
except KeyboardInterrupt:
    stop()
