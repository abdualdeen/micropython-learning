import machine
import time

led1 = machine.Pin(16, machine.Pin.OUT)
led2 = machine.Pin(17, machine.Pin.OUT)

button1 = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_DOWN)
button2 = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button1.value() == 1:
        led1.on()
    else:
        led1.off()
   
    if button2.value() == 1:
        led2.on()
    else:
        led2.off()
   
    time.sleep(0.1)
