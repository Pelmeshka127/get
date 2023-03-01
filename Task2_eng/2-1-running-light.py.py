import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

leds  = [21, 20, 16, 12, 7, 8, 25, 24]
array = [0,  0,  0,  0,  0, 0, 0,  0 ]

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

for i in range(3):

    for j in range(8):

        for k in range(8):
            array[k] = 0
        
        array[j] = 1
        GPIO.output(leds, array)
        time.sleep(0.2)
        GPIO.output(leds, 1)
        GPIO.output(leds, 0)


GPIO.cleanup()