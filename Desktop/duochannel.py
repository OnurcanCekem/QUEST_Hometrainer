#################################################
# Part of the first prototype designed for the hometrainer to be used by deaf, blind (or both) people.
# This program allows the user to play .ogg audio files from the Raspberry Pi. This program uses a user interface through serial monitor.
#
# Version 0.3 10/01/2022 - Expanded select_new_song and added suffix 
# Authors: Onurcan Cekem & Bob Rip
#################################################
import pygame, sys, time
from pygame.locals import *
import os
import glob
import random
        
# shows all music in the music folder found on Desktop.
def show_all_music(): 
    os.chdir("/home/pi/Desktop/Music") # folder destination
    for file in glob.glob("*.ogg"): # select all files that end with .ogg
        print(file)

#function to select new song
def select_new_song(selectedsong):
    #if programmer is lazy
    index = selectedsong.find(".ogg") #find .ogg in file
    if (index == -1): #if string is not found, return -1
        pygame.mixer.music.load(f"/home/pi/Desktop/Music/{selectedsong}.ogg")
    
    #else input is normal, string is found
    else:
        pygame.mixer.music.load(f"/home/pi/Desktop/Music/{selectedsong}")
    
    pygame.mixer.music.play() # play audio

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

# Function for the first button to play feedback on how long the user has been cycling
# Play order: je hebt x minuten gefietst
def feedback_button():
    pygame.mixer.music.pause() # pause music
    channel = 2 # select channel, developer mode
    counter = 0
    time_m = 10 # time in minutes
    
    # Play first sound
    play_sound("je_hebt", channel)
    while True: # Loop until everything has been played
        
        # Play second sound
        if((channel2.get_busy() == 0) & (counter == 0)):
            counter += 1
            play_sound(f"{time_m}",channel)
            print(counter)
            
        # Play third sound
        elif((channel2.get_busy() == 0) & (counter == 1)):
            counter+=1
            play_sound("minuten_gefietst", channel)
            print(counter)
        
        # End loop as we played all sounds
        elif((channel2.get_busy() == 0) & (counter == 2)):
            break
        
    #play_sound(str(10),channel)
    #play_sound("minuten_gefietst", channel)
    
    if((channel2.get_busy() == 0) & pygame.mixer.music.get_busy()):
        pygame.mixer.music.unpause()

# Function for the second button to skip the current route and play the next one
# Randomly selects an audio file from given music_list with a random amount of time it plays the file
def skiproute_button(music_list):

    #randomizer
    music_file = music_list[random.randint(0, len(music_list)-1)]#choose random audio file
    pygame.mixer.music.load(f"/home/pi/Desktop/Music/{music_file}")#load music file
    pygame.mixer.music.play()

# Function to read and return all playable audio files in Music folder 
def DivideAllMusic(): 
    file_counter = 0
    music_list = []
    os.chdir("/home/pi/Desktop/Music") # folder destination
    for file in glob.glob("*.ogg"): # select all files that end with .ogg
        music_list.append(file) #put all files in an array  
        file_counter += 1
    return music_list

#print all found music files to pick from
#list = os.listdir("/home/pi/Desktop/Music/")
#print("Here is a list of all found music files: ")
#print(list)
#print("\n")

#print only .ogg files
list = glob.glob("/home/pi/Desktop/Music/*.ogg")
print("Here is a list of all found music files with .ogg: ")
print(list)
print("\n")

#print only suffix files
suffix = "background" 
list = glob.glob(f"/home/pi/Desktop/Music/*{suffix}.ogg")
print("Here is a list of all found music files with background.ogg: ")
print(list)
print("\n")

pygame.init() # initialize pygame
pygame.mixer.set_num_channels(8) # set max number channels to 8

sound1 = pygame.mixer.Sound('/home/pi/Desktop/Music/gamer.ogg') # load in sound1
sound2 = pygame.mixer.Sound('/home/pi/Desktop/Music/wheez.ogg')

pygame.mixer.music.set_volume(0.1)

#pygame.mixer.music.load("/home/pi/Desktop/Music/gamer.ogg")
#pygame.mixer.music.play()

#DISPLAYSURF = pygame.display.set_mode((400,300)) # if you want to work with GUI's, be my guest.
#pygame.display.set_caption('Memes.')

# initialize channels
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel1.set_volume(0.2)
channel2.set_volume(0.2)


running = True
counter = 0

music_list = DivideAllMusic() # music list with all audio files

#while True: #infinite loop
while True:
    print("Press 'a' to get_sound")
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    print("Press 'v' to check and adjust volume")
    print("Press 'q' to change music")
    print("Press 'd' to DUOOOOOO 1")
    print("Press 'f' to imitate feedback_button press")
    print("Press 's' to imitate skip_button press")
    print("Press 'c' to do nothing at the moment (placeholder)")
    query = input("  ") # wait for input from user, type a key and press enter
#    query = 'c'    
    if query == 'a': # returns 1 when paused, interesting
        print("  Current busy status: " + str(pygame.mixer.music.get_busy()))
    elif query == 'p':
        pygame.mixer.music.pause()
    elif query == 'r':
        pygame.mixer.music.unpause()
    elif query == 'e':
        pygame.mixer.music.stop()
        
    elif query == 'v':
        print(" Current volume: " + str(pygame.mixer.music.get_volume()))
        print(" Please input a value between 0.0 and 1.0")
        setvolume = float(input("  "))
        pygame.mixer.music.set_volume(setvolume)
        print(" Volume set to: " + str(pygame.mixer.music.get_volume()))
    elif query == 'q':
        print("Here is a list of all eligible music files with .ogg: ")
        show_all_music()
        requestsong = input("  ")
        print("\n")
        select_new_song(requestsong)
    elif query == 'd':
        #print("Input song: ")
        #selectedsong = input(" ")
        pygame.mixer.music.pause()
        channel1.play(sound1)
        print(pygame.mixer.get_busy())
    elif query == 'f':
        feedback_button()
    elif query == 's':
        skiproute_button(music_list)
        #print("Input song: ")
        #selectedsong = input(" ")
        #channel2.play(sound1)
        #break

trigger = 0
    
# "In due time you will know the tragic extent of my failings."
# Debug channels. Tried to make it work with events (set_endevent, get_endevent). It works with pygame.mixer.music.load, but not with channels

#MUSIC_END = pygame.USEREVENT+1
#pygame.mixer.music.set_endevent(MUSIC_END)
#channel1.set_endevent(MUSIC_END)
while running:
    # pygame.music.mixer.load(), general
    end1 = channel1.get_busy()
    end2 = channel2.get_busy()
    
    # Infinite play sound1 and 2. Code works, don't touchie
    #if(end1 == 0):
    #    channel1.play(sound1)
    #elif(end2 == 0):
    #    channel2.play(sound2)
    
    #if((end1 == 0) & (end2 == 0) & (trigger == 0)):
    #    trigger = 1
    #    channel1.play(sound1)
    #    print("Gamer")
    #elif((end1 == 0) & (end2 == 0) & (trigger == 1)):
    #    trigger = 0
    #    channel2.play(sound2)
    #    play_sound("Wheez", 2)
    #    print("kekW")
    #sound1 = pygame.mixer.Sound('/home/pi/Desktop/Music/wheez.ogg')    
    #if end == MUSIC_END:
    #    print("Kunta Kinte")
    #else:
    #    print("IDK man")
    
    #for event in pygame.event.get():
    #    if event.type == pygame.QUIT:
    #        running = False
    #    
    #    if event.type == MUSIC_END:
    #        print("music end event")
    #        pygame.mixer.music.play()
        
    #channel1
    
        #sound1.play()
        #pygame.mixer.Sound('/home/pi/Desktop/Music/tupac.ogg')
        #channel1.play(pygame.mixer.Sound('/home/pi/Desktop/Music/tupac.ogg'))
        #pygame.mixer.Channel.play('/home/pi/Desktop/Music/tupac.ogg')
        #selectedsong = input(" ")
        #pygame.mixer.music.pause()
        #sound1 = pygame.mixer.Sound(f"/home/pi/Desktop/Music/{selectedsong}.ogg")


#time.sleep()
#pygame.quit()

