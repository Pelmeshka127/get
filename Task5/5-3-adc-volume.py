import RPi.GPIO as gpio
import time

def dec_to_bin(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]



def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        gpio.output(dac, dec_to_bin(k))
        time.sleep(0.1)
        comp_val = gpio.input(comp)
        if (comp_val == 0):
            k -= 2**i
    return k


dac    = [26, 19, 13, 6, 5, 11, 9, 10]
leds   = [21, 20, 16, 12, 7, 8, 25, 24]
comp   = 4
troyka = 17
bits   = len(dac)
levels = 2 ** bits


gpio.setmode(gpio.BCM)
gpio.setup(leds, gpio.OUT)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

try:
    while True:
        val = adc()
        k = 0
        for i in range(bits):
            if (val > i / 8 * levels):
                k += 2 ** i
        gpio.output(leds, dec_to_bin(k))
        
finally:
    gpio.output(dac, gpio.LOW)
    gpio.output(leds, gpio.LOW)
    gpio.output(troyka, gpio.LOW)
    gpio.cleanup()