# button pin 19, led 26
# Connect LED to pin and GND
# Connect button top left with resistor to GND
# Connect button top right with Vcc
# Connect button bottom left with GPIO input
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
sleepTime = 0.1

lightPin = 26 #
buttonPin = 19 # buttonpin
GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Pull-up button

try: # when program starts, go to this loop
    while True:

        if GPIO.input(buttonPin) == GPIO.LOW:
            print("Low can I get witcha")
        elif GPIO.input(buttonPin) == GPIO.HIGH:
            print("High call back I'm busy")
        GPIO.output(lightPin, GPIO.input(buttonPin))
        time.sleep(0.1)

finally: #when interrupted, do this
    GPIO.output(lightPin, False)
    GPIO.cleanup()
                    