#!/usr/bin/env python3
# Program to test interrupts using blinking LED and a button
                                
import signal                   
import sys
import time
import RPi.GPIO as GPIO

BUTTON_GPIO = 19
LED_GPIO = 26
should_blink = False

# at end of program, clean gpio's so LED won't remain on
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

# action what to do when button is released
def button_released_callback(channel):
    global should_blink
    should_blink = not should_blink # led blink on/off button
    print("It's ya boy, start button")

# basically setup, code that runs once
if __name__ == '__main__':
    #setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Pull-up
    GPIO.setup(LED_GPIO, GPIO.OUT)   
    GPIO.setwarnings(False) # optional, I prefer to turn warnings off


    GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING, 
            callback=button_released_callback, bouncetime=200) # button interrupt
    
    signal.signal(signal.SIGINT, signal_handler) # 
    
    while True:
        button_pressed = True # release the trigger for button
        
        if should_blink: # if button is turned on
            GPIO.output(LED_GPIO, GPIO.HIGH) 
        time.sleep(0.5)
        if should_blink:
            GPIO.output(LED_GPIO, GPIO.LOW)  
        time.sleep(0.5)
