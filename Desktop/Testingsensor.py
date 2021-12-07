#!/usr/bin/env python3
# Testing sensor on pin 26
# This program is used to track how long it takes for the sensor to read a magnet, which is pretty fast.
# If the sensor reads a magnet, it's locked until it doesn't. 
                
import signal                   
import sys
import time
import RPi.GPIO as GPIO

HALsensor = 26 # HALsensor GPIO pin 26

should_blink = False # can be removed, if button_released_callback gets removed

# function to start the program, so leds won't stay turned on
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

# function for button
def button_released_callback(channel): # action what to do when button is released
    global should_blink
    should_blink = not should_blink
    print("It's ya boy, start button")


if __name__ == '__main__':
    #setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(HALsensor, GPIO.IN) # Sensor setup   
    GPIO.setwarnings(False)
    
    startuptime = time.perf_counter() # Remember the start time of when program started
    currenttime = time.perf_counter()-startuptime #I think this line can be removed, but I haven't tested it.
    
    
    signal.signal(signal.SIGINT, signal_handler)
    
    counter = 0 # variable to count the amount of times 
    programtime = 0 # variable to track the release of a button
    
    while True:
        
        currenttime = time.perf_counter() # remember current time in the program
        
        if not(GPIO.input(HALsensor)): # if sensor sees a magnet
            
            if(currenttime-programtime >= 0.01): # If the magnet has moved and we see another magnet 
                
                counter+=1 # Put anything here
                print("Counter: " + str(counter)) # debug output
                print("programtime: " + ("{:.4f}".format(currenttime))) # debug time output 
                programtime = currenttime # remember that we already counted
                
            else: # else the magnet hasn't moved
                
                programtime = currenttime
                #print("high And this the ---- thanks I get?")
        
        




