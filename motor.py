import wiringpi
gpio = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO)

class Motor:
    def __init__(self, pf, pb):
        self.pinForward = pf
        self.pinBack = pb

        gpio.pinMode(pf, gpio.OUTPUT)
        gpio.digitalWrite(pf, False)
        gpio.pinMode(pb, gpio.OUTPUT)
        gpio.digitalWrite(pb, False)

    def forward(self):
        gpio.digitalWrite(self.pinForward, 1)
        gpio.digitalWrite(self.pinBack, 0)

    def back(self):
        gpio.digitalWrite(self.pinForward, 0)
        gpio.digitalWrite(self.pinBack, 1)

    def stop(self):
        gpio.digitalWrite(self.pinForward, 0)
        gpio.digitalWrite(self.pinBack, 0)
