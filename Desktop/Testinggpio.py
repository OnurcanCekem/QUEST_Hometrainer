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
=======
# Blink program to turn led off and on every 0.5s using GPIO pin 26

import RPi.GPIO as GPIO
import time

#Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setwarnings(False) #optional, I prefer to turn warnings off

LED = 26 # GPIO pin 26
ledState = False

while True:
    ledState = not ledState # blink
    GPIO.output(LED, ledState)
    time.sleep(0.5)