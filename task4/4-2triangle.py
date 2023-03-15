import RPi.GPIO as gpio
import time as time

gpio.setmode(gpio.BCM)

dac = [26, 19, 14, 6, 5, 11, 9, 10]

gpio.setup(dac, gpio.OUT)

T = 1


def dec_to_bin(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

try:
    while (True):
        for i in range(255):
            array = []
            array = dec_to_bin(i)

            for j in range(8):
                gpio.output(dac[j], array[j])
            
            time.sleep(T/512)

        for i in range(255, 0, -1):
            array = []
            array = dec_to_bin(i)

            for j in range(8):
                gpio.output(dac[j], array[j])
            
            time.sleep(T/512)


finally:
    gpio.output(dac, 0)
    gpio.cleanup()