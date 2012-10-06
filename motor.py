import wiringpi
gpio = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)

class Motor:
    def __init__(self, pf, pb):
        self.pinForward = pf
        self.pinBack = pb

        wiringpi.softPwmCreate(pf, 0, 80)
        wiringpi.softPwmCreate(pb, 0, 80)

    def forward(self):
        wiringpi.softPwmWrite(self.pinForward, 80)
        wiringpi.softPwmWrite(self.pinBack, 0)

    def back(self):
        wiringpi.softPwmWrite(self.pinForward, 0)
        wiringpi.softPwmWrite(self.pinBack, 80)

    def stop(self):
        wiringpi.softPwmWrite(self.pinForward, 0)
        wiringpi.softPwmWrite(self.pinBack, 0)

    def speed(self, speed):
        speed = int(speed)
        if (speed >= 0):
            wiringpi.softPwmWrite(self.pinForward, speed)
            wiringpi.softPwmWrite(self.pinBack, 0)
        else:
            wiringpi.softPwmWrite(self.pinForward, 0)
            wiringpi.softPwmWrite(self.pinBack, -speed)
