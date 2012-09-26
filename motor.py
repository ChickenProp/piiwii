import wiringpi
gpio = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO)

class Motor:
    def __init__(self, pf, pb):
        self.pinForward = pf
        self.pinBack = pb

        wiringpi.softPwmCreate(pf, 0, 100)
        wiringpi.softPwmCreate(pb, 0, 100)

    def forward(self):
        wiringpi.softPwmWrite(self.pinForward, 100)
        wiringpi.softPwmWrite(self.pinBack, 0)

    def back(self):
        wiringpi.softPwmWrite(self.pinForward, 0)
        wiringpi.softPwmWrite(self.pinBack, 100)

    def stop(self):
        wiringpi.softPwmWrite(self.pinForward, 0)
        wiringpi.softPwmWrite(self.pinBack, 0)

    def speed(self, speed):
        if (speed >= 0):
            wiringpi.softPwmWrite(self.pinForward, speed)
            wiringpi.softPwmWrite(self.pinBack, 0)
        else:
            wiringpi.softPwmWrite(self.pinForward, 0)
            wiringpi.softPwmWrite(self.pinBack, -speed)
