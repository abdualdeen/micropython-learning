import machine

led = machine.Pin(15, machine.Pin.OUT)
btn = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if btn.value() == 1:
        led.on()
    else:
        led.off()
