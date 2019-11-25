import time
import pigpio

SW01 = 4
SW02 = 17
SW03 = 27
SW04 = 18
SW05 = 5
SW06 = 6
SW07 = 13
SW08 = 12
SW09 = 22
SW10 = 23


class Switch:
    def __init__(self, on, off):
        self.on = on
        self.off = off


pc_roon = Switch(SW01, SW02)
kitchen = Switch(SW03, SW04)

rooms = [
    pc_roon,
    kitchen,
]


def switch(sw_no):
    pi = pigpio.pi()
    pi.set_mode(sw_no, pigpio.OUTPUT)
    pi.write(sw_no, 0)
    time.sleep(0.5)
    pi.write(sw_no, 1)


def all_off():
    for room in rooms:
        switch(room.off)
        time.sleep(1)
