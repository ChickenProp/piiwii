#! /usr/bin/python
from __future__ import division
import math
from config import Config
import nunchuk
import wiringpi

def motors(l, r):
    Config.motorL.speed(l)
    Config.motorR.speed(r)

nunchuk.setup()

try:
    while True:
        x,y = nunchuk.read_joy_normalized()
        r = nunchuk.clamp(math.sqrt(x*x + y*y), -8, 8)
        # It would perhaps be better if both motors were scaled by r when
        # x != 0. But this gives results which feel good, so there's no
        # particular need.
        if x == 0:
            motors(y*10, y*10)
        elif x < 0:
            if y >= 0:
                motors((y-4)*20, r*10)
            elif y < 0:
                motors(-r*10, (y+4)*20)
        elif x > 0:
            if y >= 0:
                motors(r*10, (y-4)*20)
            elif y < 0:
                motors((y+4)*20, -r*10)

        wiringpi.delay(int(1000/60))
except KeyboardInterrupt:
    motors(0, 0)
