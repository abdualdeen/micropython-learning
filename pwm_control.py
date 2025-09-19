from machine import Pin, PWM
import time
 
# Initialize the LED pin for PWM
led = PWM(Pin(15))
led.freq(1000) # this is where the freq in hz is set. if you go 30 and below, you can see the blinking.

while True:
    for duty_cycle in range(0, 6000):
        led.duty_u16(duty_cycle)
        time.sleep(0.005)
    for duty_cycle in range(6000, -1, -1):
        led.duty_u16(duty_cycle)
        time.sleep(0.005)
