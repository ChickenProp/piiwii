from __future__ import division
import wiringpi
import fcntl
import os

i2c_file = "/dev/i2c-0"
i2c_fd = -1
i2c_addr = 0x52
i2c_ioctl_num = 0x703

joy_x_center = 128
joy_y_center = 128

def setup():
    global i2c_fd
    i2c_fd = os.open(i2c_file, os.O_RDWR)
    ret = fcntl.ioctl(i2c_fd, i2c_ioctl_num, i2c_addr)
    ret = os.write(i2c_fd, "\xf0\x55")
    os.write(i2c_fd, "\xfb\x00")
    calibrate_joystick()

def calibrate_joystick():
    global joy_x_center, joy_y_center
    cur = read_joy()
    joy_x_center = cur[0]
    joy_y_center = cur[1]

# Currently every call to read_*() makes a new read, costing at least 1ms. If
# this becomes serious, there'll need to be a way to store values and only
# update them on demand.

def read_all():
    global i2c_fd
    os.write(i2c_fd, "\x00")
    wiringpi.delay(1)
    ret = bytearray(os.read(i2c_fd, 6))
    acc_x = (ret[2] << 2) + (ret[5] >> 2 & 0x03)
    acc_y = (ret[3] << 2) + (ret[5] >> 4 & 0x03)
    acc_z = (ret[4] << 2) + (ret[5] >> 6 & 0x03)
    btn_z = ret[5] & 0x01 == 0
    btn_c = ret[5] & 0x02 == 0
    return (ret[0], ret[1], acc_x, acc_y, acc_z, btn_z, btn_c)

def read_joy():
    vals = read_all()
    return vals[0], vals[1]

# This is fairly basic. In my tests, without clamping, x ranged from -9 to 10
# and y ranged from -9 to 8, so clamping to [-8, +8] gives us equal ranges
# withou much loss of precision. Dividing by 10 and truncating to int means
# small fluctuations get ignored, which is probably good for most purposes.
def read_joy_normalized():
    x, y = read_joy()
    norm_x = clamp(int((x - joy_x_center)/10), -8, 8)
    norm_y = clamp(int((y - joy_y_center)/10), -8, 8)
    return norm_x, norm_y

def clamp(val, minval, maxval):
    return min(maxval, max(minval, val))
