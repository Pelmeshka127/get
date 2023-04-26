import RPi.GPIO as gpio
import time as time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

comp = 4

troyka = 17

gpio.setmode(gpio.BCM)

gpio.setup(dac, gpio.OUT)

gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)

gpio.setup(comp, gpio.IN)

def dec_to_bin(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

def adc():
    k = 0
    for i in range(7, -1, -1):
        k+=2**i
        gpio.output(dac, dec_to_bin(k))
        comp_value = gpio.input(comp)
        time.sleep(0.05)

        if comp_value == 1:
            k-=2**i
    return k

try:
    while True:
        value = adc()
        if value != 0:
            print("Цифровое значение равно = ", value)
            print("Напряжение на выходе V = {:.4f} B".format(value *3.3 / 256))

finally:
    gpio.output(dac, 0)
    gpio.cleanup()