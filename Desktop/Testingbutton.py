# Button program to interrupt an LED from blinking
# button pin 19, led 26
# Connect LED to pin and GND
# Connect button top left with resistor to GND
# Connect button top right with Vcc
# Connect button bottom left with GPIO input
import RPi.GPIO as GPIO
import time

#Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
sleepTime = 0.1

lightPin = 26 # LED
buttonPin = 19 # buttonpin
GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Pull-down button

try: # when program starts, go to this loop
    while True:

        if GPIO.input(buttonPin) == GPIO.LOW: # if low
            print("Low can I get witcha")
        elif GPIO.input(buttonPin) == GPIO.HIGH: # else high, but elif does the same
            print("High call back I'm busy")
        GPIO.output(lightPin, GPIO.input(buttonPin)) # Turn lightpin on/off depending on the input of button
        time.sleep(0.1)

#when keyinterrupted or at the end of program, do this
# This is to prevent the LED from staying on when interrupted at the wrong time
finally: 
    GPIO.output(lightPin, False)
    GPIO.cleanup()
                    