import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

dac = [26, 19, 14, 6, 5, 11, 9, 10]

gpio.setup(dac, gpio.OUT)


def dec_to_bin(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

def print_voltage(num):
    print("Напряжение на выходе V = {:.3f} B".format(num / 256.0))

try:
    while(True):
        print("Введите десятичное число:\n")

        str = input()

        if (str == "exit"):
            break

        try:
            num = int(str)
        except ValueError:
            print("Введенное типо-число не является числом))))")
        else:
            if (num < 0):
                print("Число ОБЯЗАНО (служить) быть неотрицательным")
                continue

            if (num > 255):
                print("Э куда херачишь!! Чило не больше 255!!!")
                continue

            gpio.output(dac, dec_to_bin(num))

            print_voltage(num)

finally:
    gpio.output(dac, 0)
    gpio.cleanup()