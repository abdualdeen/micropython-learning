from machine import Pin, ADC
import time
 
# Initialize the LEDs, photoresistor, and button
led1 = Pin(13, Pin.OUT)
led2 = Pin(14, Pin.OUT)
led3 = Pin(15, Pin.OUT)
photoresistor = ADC(Pin(26))
button = Pin(16, Pin.IN, Pin.PULL_DOWN)
 
while True:
    # Read the value from the photoresistor
    light_level = photoresistor.read_u16()
 
    # Read the value from the button
    button_state = button.value()
 
    # Print the light level and button state (optional for debugging)
    print(f"Light level: {light_level}, Button state: {button_state}")
 
    # Control the LEDs based on the sensor inputs
    if light_level < 20000 and button_state == 1:
        led3.on()
        led2.off()
        led1.off()
    elif light_level < 20000 and button_state == 0:
        led3.off()
        led2.off()
        led1.on()
    elif button_state == 1:
        led3.off()
        led2.on()
        led1.off()
    else:
        led3.off()
        led2.off()
        led1.off()
 
    # Delay for a short period
    time.sleep(0.5)
