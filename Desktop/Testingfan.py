import signal                   
import sys
import time
import RPi.GPIO as GPIO


ZERO_CROSSING = 19
PSM1 = 26
ventilator_snelheid = 0
PSM_counter = 0

# basically setup, code that runs once
if __name__ == '__main__':
    #setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ZERO_CROSSING, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #pull down
    GPIO.setup(PSM1, GPIO.OUT)   
    GPIO.setwarnings(False) # optional, I prefer to turn warnings off


# at end of program, clean gpio's so LED won't remain on
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
    
    
# action what to do when the sinus crosses zero
def PSM_CHANNAL1(channel):
    global ventilator_snelheid
    global PSM_counter
    
    if PSM_counter < ventilator_snelheid:
        GPIO.output(PSM1, GPIO.HIGH)
    else:
        GPIO.output(PSM1, GPIO.LOW)
    
    PSM_counter += 1
    
    if PSM_counter >= 100 :
        PSM_counter = 0
        

GPIO.add_event_detect(ZERO_CROSSING, GPIO.RISING, callback=button_released_callback, bouncetime=10) # zero crossing interupt interrupt
    
signal.signal(signal.SIGINT, signal_handler) #if program ends clean up GPIOS

while True:
    query = input("  ")
    
    if query >= 10 && <= 100:
        ventilator_snelheid = query
    else:
        print("invalid number")
        


    


