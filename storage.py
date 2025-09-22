
import machine
import time
 
# Initialize the photoresistor and the button
photoresistor = machine.ADC(machine.Pin(26))
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
 
# File to store data
filename = "light_data.txt"
 
def read_sensor_data():
    light_level = photoresistor.read_u16()
    return light_level
 
def store_data(data):
    with open(filename, 'a') as f:
        f.write(f"{data}\n")
 
def retrieve_data():
    try:
        with open(filename, 'r') as f:
            data = f.readlines()
            return data
    except OSError:
        return []
 
while True:
    if button.value() == 1:
        light_level = read_sensor_data()
        store_data(light_level)
        print(f"Data Stored Successfully")
        time.sleep(2)
       
        print(f"Retrieving stored data")
        file_content = retrieve_data()
        time.sleep(1)

        print(f"Retrieved data is: {file_content}")

