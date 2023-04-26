import matplotlib.pyplot as plt
import time as time
import RPi.GPIO as gpio



leds = [21, 20, 16, 12, 7, 8 , 25, 24]
dac  = [26, 19, 13, 6 , 5, 11, 9 , 10]

comp = 4
troyka = 17

gpio.setmode(gpio.BCM)
gpio.setup(leds, gpio.OUT)
gpio.setup(dac, gpio.OUT, initial=gpio.HIGH)
gpio.setup(troyka, gpio.OUT, initial=gpio.LOW)
gpio.setup(comp, gpio.IN)

gpio.output(troyka, 0)
time.sleep(1)

def dec_to_bin(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]

def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        gpio.output(dac, dec_to_bin(k))
        time.sleep(0.001)
        comp_val = gpio.input(comp)
        if (comp_val == 0):
            k -= 2**i
    return k

try:
    volt = 0
    results = []
    time_start = time.time()
    count = 0

    print("Конденсатор заряжается\n")
    while (volt <= 230):
        volt = adc()
        print(volt, "В")
        results.append(volt)
        count += 1
        gpio.output(leds, dec_to_bin(volt))

    gpio.output(troyka, 1)

    print("Разрядка конденсатора\n")
    while (volt >= 63):
        volt = adc()
        print(volt, "В")
        results.append(volt)
        count += 1
        gpio.output(leds, dec_to_bin(volt))

    time_stop = time.time()
    res_time = time_stop - time_start

    results_str = [str(item) for item in results]

    with open("data.txt", "w") as data_file:
        data_file.write("\n".join(results_str))

    with open("settings.txt", "w") as settings_file:
       settings_file.write(str(len(results) / res_time) + "\n" + str(3.3 / 256))


    print("Время измерений ", res_time, " с\n")
    print("Период одного измерения ", res_time / len(results), " с\n")
    print("Частота дискретизации ", len(results) / res_time, " Гц\n")
    print("Шаг квантования ", 3.3 / 256 , "В\n")

    plt.plot(results)
    plt.show()


finally:
    gpio.output(dac, 0)
    gpio.output(leds, 0)
    gpio.cleanup()