# led pin 26
# Doesn't have try and finally. Meaning the led can remain
# on when interrupted

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED = 26 # GPIO pin
ledState = False
GPIO.setup(LED, GPIO.OUT)

while True:
    ledState = not ledState
    GPIO.output(LED, ledState)
    time.sleep(0.5)