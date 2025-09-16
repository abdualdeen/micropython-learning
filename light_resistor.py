import time
from machine import Pin, ADC

led = Pin(15, Pin.OUT)
photoresistor = ADC(Pin(26))

while True:
    # Read the value from the photoresistor
    light_level = photoresistor.read_u16()

    # Print the light level (optional for debugging)
    print(light_level)

    # Control the LED based on the light level
    if light_level < 20000:
        led.on()
    else:
        led.off()

    # Delay for a short period
    time.sleep(0.5)
