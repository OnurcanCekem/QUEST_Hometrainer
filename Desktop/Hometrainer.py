# Full program hometrainer
# Authors: Onurcan Cekem & Bob Rip
# 
# Program designed for the hometrainer to be used by deaf, blind (or both) people.
# Hometrainer's main purpose is to make exercise more interactive. The project group came with the idea of using
# 4 methods to achieve this goal: Wind, Audio, Vibrator and Light. As of 2021-2022 wind and audio will be achieved

# Version 0.1 10/01/2022 - Start of program
# Version 0.2 24/01/2022 - Added all individual functions. Started coding main loop. Added comment lines. Added template for pins.
# Version 0.3   /01/2022 - 


#=========================================================================
#                              IMPORTS
#=========================================================================
import pygame, sys, time
from pygame.locals import *
import os
import glob
import random
import RPi.GPIO as GPIO
from MCP3008 import MCP3008



#=========================================================================
#                  VARIABLES (INITIALIZE/GPIO PINS)
#=========================================================================
# audio
pygame.init() # initialize pygame
pygame.mixer.set_num_channels(8) # Allow 8 audio channels to be loaded in

channel1 = pygame.mixer.Channel(0) # initialize channel 1
channel2 = pygame.mixer.Channel(1) # initialize channel 2

# GPIO Pins
GPIO.setwarnings(False) # Disable warnings, because they are annoying
GPIO.setmode(GPIO.BCM)
magnetsensor = 12 # max current 25 mA, use a resistor of 200 Ohm --> 220 Ohm (E-reeks)
feedback_button = 5
skip_button = 6
PSM1 = 13
ZERO_CROSSING = 26
Wind_slider_pin = 0
Audio_slider_pin = 1

# Analoge slider GPIO 8,9,10,11 door MCP3008

# previous states from sensors template
prev_feedback_button = 0
prev_skip_button = 0
wind_strength = 1
volume = 1

# analog slider
adc = MCP3008()
#value = adc.read( channel = 0 ) # You can of course adapt the channel to be read out
#print("Applied voltage adc1: %.2f" % (value / 1023.0 * 3.3))

# Button
GPIO.setup(skip_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(feedback_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#PSM Ventilator
GPIO.setup(PSM1, GPIO.OUT)
GPIO.setup(ZERO_CROSSING, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #pull down
# HAL sensor
GPIO.setup(magnetsensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Sensor setup

#=========================================================================
#                             VARIABLES
#=========================================================================
# audio variables
pygame.mixer.music.set_volume(0.1) # max volume before sound becomes cracked
channel1.set_volume(0.2)
channel2.set_volume(0.2)
suffix = "_background" # suffix, used to find audio files. Example: Jungle_background.ogg

# Ventilator
ventilator_snelheid = 0
PSM_counter = 0

#rotation speed
rotation_time = 0.01
rotation_speed = 0.01

max_rotation_per_sec = 1.5
#=========================================================================
#                             FUNCTIONS
#=========================================================================
# (developer function) shows all music in the music folder found on Desktop.
def show_all_music(): 
    os.chdir("/home/pi/Desktop/Music") # folder destination
    for file in glob.glob("*.ogg"): # select all files that end with .ogg
        print(file)

# function to load in and play a new song
# variables:
# selectedsong - name (or file name) of song 
def select_new_song(selectedsong):
    #if programmer is lazy
    index = selectedsong.find(".ogg") #find .ogg in file
    if (index == -1): #if string is not found, return -1
        pygame.mixer.music.load(f"/home/pi/Desktop/Music/{selectedsong}.ogg") # load in audio file
    
    #else input is normal, string is found
    else:
        pygame.mixer.music.load(f"/home/pi/Desktop/Music/{selectedsong}")
    
    pygame.mixer.music.play() # play audio  

# function to generate and return a music list depending on suffix.
# Returns all music (.ogg) in the music folder found on Desktop with the given suffix.
# variables:
# suffix - If suffix is given, function returns all music in destination with given suffix. Else it returns all music (default = 0)
#          suffix has to be a string.
def generate_music_list(suffix=0): 
    file_counter = 0
    print("Suffix: " + str(suffix)) # debug
    music_list = []
    os.chdir("/home/pi/Desktop/Music") # folder destination
    
    if suffix == 0:
        for file in glob.glob("*.ogg"): # select all files that end with .ogg
            music_list.append(file) #put all files in an array  
            file_counter += 1
    else:
        for file in glob.glob(f"*{suffix}.ogg"): # select all files that end with .ogg
            music_list.append(file) #put all files in an array  
            file_counter += 1
    return music_list

# randomly selects an audio file from given music_list with a random amount of time it plays the file
# variables:
# music list - array of music from generate_music_list
def Randomizer(music_list):
    music_file = music_list[random.randint(0, len(music_list)-1)] # choose random audio file
    pygame.mixer.music.load(f"/home/pi/Desktop/Music/{music_file}") # load music file
    pygame.mixer.music.play()    
    

# function to play a sound on a channel
# variables:
# sound - file name
# channel - select which channel to play sound on (default = 1)
def play_sound(sound, channel=1):
    
    # simple if/elif statements. This could be a dictionary, but I'm lazy
    sound_file = pygame.mixer.Sound(f"/home/pi/Desktop/Music/{sound}.ogg") # select sound file
    if channel == 1:
        channel1.play(sound_file) # play sound file on channel 1
        print("Channel One") # debug
        
    elif channel == 2:
        channel2.play(sound_file) # play sound file on channel 2
        print("Channel Two") # debug
    # if more channels are being added
#    elif channel == 3:
#        print("Channel Three" + str(channel3.get_busy()))
#        
#    elif channel == 4:
#        print("Into the Four" + str(channel4.get_busy()))
        
    else:
        print("Snoop Doggy Dogg and Dr.Dre is at the door. Channel not accepted. Programmer skill issue.")



# function for the first button to play feedback on how long the user has been cycling
# play order: je hebt | x | minuten gefietst
# variables: time_s - time in seconds
def feedback_button_func(time_s):
    pygame.mixer.music.pause() # pause music
    channel = 2 # select channel, developer mode
    counter = 0
    time_m = int(time_s / 1000) # time in minutes
    print("Time_m: " +str(time_m))
    # play first sound
    play_sound("je_hebt", channel)
    while True: # Loop until everything has been played
        
        # play second sound
        if((channel2.get_busy() == 0) & (counter == 0)):
            counter += 1
            play_sound(f"{time_m}",channel)
            print(counter)
            
        # play third sound
        elif((channel2.get_busy() == 0) & (counter == 1)):
            counter+=1
            play_sound("minuten_gefietst", channel)
            print(counter)
        
        # end loop when we played all sounds
        elif((channel2.get_busy() == 0) & (counter == 2)):
            break
        
    #play_sound(str(10),channel)
    #play_sound("minuten_gefietst", channel)
    
    if((channel2.get_busy() == 0) & pygame.mixer.music.get_busy()): # if channel 2 is done, as it should be from the last elif, play music again
        pygame.mixer.music.unpause()

# function for the second button to skip the current route and play the next one
# randomly selects an audio file from given music_list with a random amount of time it plays the file
# variables:
# music list - array of music from generate_new_music
def skip_button_func(music_list):
    music_file = music_list[random.randint(0, len(music_list)-1)] # choose random audio file
    pygame.mixer.music.load(f"/home/pi/Desktop/Music/{music_file}") # load music file
    pygame.mixer.music.play()

# at end of program, clean gpio's so LED won't remain on
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
    

# function to read all button states. This is used to keep the main code clean.
def button_routine():
    prev_skip_button = skip_button
    prev_feedback_button = feedback_button
    

#function that caluclates the PSM sgnal for the wind speed
#arguments: 
    #rotation: the rotation speed in rotations per second
    #slider: slider value from 0 to 1
#return:
    #PSM_duty: PSM duty cycle from 0 to 100
def wind_speed_calculator(rotatie, slider):
    
    #calculate rotation speed to PSM signal 
    PSM_strength = rotatie*100/max_rotation_per_sec #rotatie snelheid * 100%/ max rotatie snelheid(2 rotaties per sec) 
    
    #calculate slider offsetof the PSM signal
    PSM_duty = int(slider * PSM_strength)
    
    # if over limit, put at max
    if(PSM_duty > 100):
        PSM_duty = 100
        
    return PSM_duty


#function that caluclates value of the slider in a value form 0 to 1
#arguments: 
    #sliderVal: slider value from 0 t 1023
#return:
    #slider value form 0 to 1 
def slider_value_calculator(sliderVal):
    return sliderVal / 1023.0 #slider waarde/ aantal bits * reference voltage

#=========================================================================
#                  INTERRUPTS
#=========================================================================

programtime = 5
# interrupt function to read the HAL magneticsensor
# note, untested function
def read_magnetsensor(channel):
    global programtime
    currenttime = int(time.perf_counter_ns() / 1000000) #runntime of program in ms
    if ( (currenttime - programtime) >= 30): # if the magnet has moved and rotated within 30 milliseconds
        global rotation_time
        rotation_time = currenttime-programtime
        print("WEE-WOO: " + str(rotation_time)) # debug
    programtime = currenttime # remember that we already counted

# Magneet sensor
GPIO.add_event_detect(magnetsensor, GPIO.FALLING, callback=read_magnetsensor, bouncetime=10) # zero crossing interrupt


# interrupt function to send a PSM signal to the ventilator
# action what to do when the sinus crosses zero
def PSM_CHANNEL1(channel):
    global ventilator_snelheid
    global PSM_counter
    
    # basic PWM function. Example: speed = 20. ventilator is 20% high, 80% low.
    if PSM_counter < ventilator_snelheid:
        GPIO.output(PSM1, GPIO.HIGH)
    else:
        GPIO.output(PSM1, GPIO.LOW)
    
    PSM_counter += 1 # keep counting
    
    if PSM_counter >= 100 : # reset counter
        PSM_counter = 0

# Ventilator
GPIO.add_event_detect(ZERO_CROSSING, GPIO.RISING, callback=PSM_CHANNEL1, bouncetime=10) # zero crossing interrupt

#=========================================================================
#                             DEBUG CODE
#=========================================================================

# print only .ogg files
list = glob.glob("/home/pi/Desktop/Music/*.ogg")
print("Here is a list of all found music files with .ogg: ")
print(list)
print("\n")

# print only suffix files
suffix = "_background" # variable is a suffix to store 
list = glob.glob(f"/home/pi/Desktop/Music/*{suffix}.ogg")
print("Here is a list of all found music files with background.ogg: ")
print(list)
print("\n")


#wind_slider = MCP3008.read( Wind_slider_pin) # read out wind slider
#query = input(" ")
#select_new_song(query)
#=========================================================================
#                             MAIN (LOOP)
#=========================================================================
#setup code 


# global vars
suffix_music_list = generate_music_list(suffix) # music list with all audio files of given suffix
starttime = int(time.perf_counter_ns() / 1000000) # start time of program

# infinite loop
query = input("")
select_new_song(query)
while True:
    currenttime = int(time.perf_counter_ns() / 1000000) - starttime
    
    #debug purposes, don't need to add back
    #print(currenttime)
    #currenttime = int(time.perf_counter_ns() / 1000000000)-starttime # time in seconds
    #print(str(currenttime) + " seconds active")
    #feedback_button_func(currenttime)
    
    # rotationspeed (working)
    #print("Rotation time: " + str(rotation_time))
    #rotation_speed = 1000/rotation_time # calculate rotations/second
    #print("rotation speed: " + str(rotation_speed))
          
    # wind slider (working)
    #wind_slider = slider_value_calculator(adc.read( Wind_slider_pin)) # read out wind slider
    #print("wind_slider: " + str(wind_slider))#debuging
    #ventilator_snelheid = wind_speed_calculator(rotation_speed, wind_slider)#determen the fan speed
    #print("ventilator_snelheid: " + str(ventilator_snelheid)) #debuging
      
     # feedback button
    #print(GPIO.input(feedback_button))
    if((GPIO.input(feedback_button) != prev_feedback_button) & 1): # if pressed and new
         prev_feedback_button = True #True
         feedback_button_func(currenttime)
    prev_feedback_button = GPIO.input(feedback_button)
     # skip button
    if((GPIO.input(skip_button) != prev_skip_button) & 1): # if pressed and new 
         print("Hallo daar")
         prev_skip_button = True # remember that the button has been pressed
         skip_button_func(suffix_music_list)
    prev_skip_button = GPIO.input(skip_button)
    
     #audio slider 
    audio_slider = slider_value_calculator(adc.read(channel = Audio_slider_pin)) # read out audio slider
    
    print(audio_slider)
    if (audio_slider != volume):
         volume = audio_slider
         pygame.mixer.music.set_volume(volume*0.8) #x0.8 bucause a higher volume produces bad audio performence  
    
    # Check route
    if(pygame.mixer.music.get_busy() == 0): # if route is not busy, play a random route
        Randomizer(suffix_music_list)
     # update buttons, timers, etc.
#     button_routine()
        
signal.signal(signal.SIGINT, signal_handler) #if program ends clean up GPIOS