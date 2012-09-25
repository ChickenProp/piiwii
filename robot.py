#! /usr/bin/python
from config import Config
import nunchuk

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

forward()
while True:
    print nunchuk.read_all()
