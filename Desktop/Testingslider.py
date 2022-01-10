# slider pin 26
# Testing slider, but the slider is an analog input meaning you only read 0 or 1.

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

slider = 26 # GPIO pin
GPIO.setup(Slider, GPIO.IN)

while True:
    print(GPIO.input(slider))
    time.sleep(0.1)
