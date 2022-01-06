# Full program hometrainer
# Authors: Onurcan Cekem & Bob Rip
# 
# Program designed for the hometrainer to be used by deaf, blind (or both) people.
# Version 0.1 10/01/2022 - Start of program


import pygame, sys, time
from pygame.locals import *
import os
import glob
        
# (developer function) shows all music in the music folder found on Desktop.
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


# shows all music in the music folder found on Desktop.
#def select_new_song(selectedsong):
    
#    pygame.mixer.music.load(f'/home/pi/Desktop/Music/{selectedsong}')
#    pygame.mixer.music.play()

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
pygame.mixer.music.set_volume(0.1) # max volume before sound becomes cracked


while True: # infinite loop
    query = input(" ")
    select_new_song(query)
