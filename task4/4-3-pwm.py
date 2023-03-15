import RPi.GPIO as gpio
import time as time

gpio.setmode(gpio.BCM)

pin = 2

gpio.setup(pin, gpio.OUT)


def dec_to_bin(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

p = gpio.PWM(pin, 1000)
duty_cycle = 0
p.start(duty_cycle)

try:
    while (True):
        print("Введитe дута какле")
        duty_cycle = int(input())
        p.ChangeDutyCycle(duty_cycle)

finally:
    p.stop()
    gpio.output(pin, 0)
    gpio.cleanup()