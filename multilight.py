import machine
import time

led_blue = machine.Pin(13, machine.Pin.OUT)
led_yellow = machine.Pin(14, machine.Pin.OUT)
led_red = machine.Pin(15, machine.Pin.OUT)

while True:
    led_blue.on()
    time.sleep(0.5)
    led_blue.off()

    led_yellow.on()
    time.sleep(0.5)
    led_yellow.off()

    led_red.on()
    time.sleep(0.5)
    led_red.off()

    time.sleep(0.5)
