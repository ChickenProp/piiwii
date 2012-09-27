import wiringpi
import fcntl
import os

i2c_file = "/dev/i2c-0"
i2c_fd = -1
i2c_addr = 0x52
i2c_ioctl_num = 0x703

def setup():
    global i2c_fd
    i2c_fd = os.open(i2c_file, os.O_RDWR)
    ret = fcntl.ioctl(i2c_fd, i2c_ioctl_num, i2c_addr)
    ret = os.write(i2c_fd, "\xf0\x55")
    os.write(i2c_fd, "\xfb\x00")

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
