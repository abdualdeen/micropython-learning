from machine import Pin
import time
 
# Initialize the LED and button pins
led1 = Pin(16, Pin.OUT)
led2 = Pin(17, Pin.OUT)
led3 = Pin(18, Pin.OUT)
 
 
while True:
    led1.on()
    time.sleep(0.5)
    led1.off()
    led2.on()
    time.sleep(0.5)
    led2.off()
    led3.on()
    time.sleep(0.5)
    led3.off()
    time.sleep(0.5)