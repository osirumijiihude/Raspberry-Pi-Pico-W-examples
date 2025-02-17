from machine import Pin, ADC
import time

# Define pins
mq6 = ADC(26)  # Analog input from MQ6
red_led = Pin(10, Pin.OUT)  # Red LED on GPIO 10
blue_led = Pin(11, Pin.OUT)  # Blue LED on GPIO 11

# Threshold value (adjust based on testing)
SMOKE_THRESHOLD = 15000  

while True:
    gas_value = mq6.read_u16()  # Read gas sensor value (0-65535)

    if gas_value > SMOKE_THRESHOLD:
        red_led.on()
        blue_led.off()
        print("Smoke detected! Gas value is:", gas_value)
    else:
        red_led.off()
        blue_led.on()
        print("No smoke detected. Gas value is:", gas_value)
    
    time.sleep(1)  # Delay for stability
