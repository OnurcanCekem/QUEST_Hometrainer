#################################################
# Part of the first prototype designed for the hometrainer to be used by deaf, blind (or both) people.
# This program allows the user to play randomly play .ogg audio files from the Raspberry Pi.
#
# Version 0.2 10/01/2022 - Tested Randomizer function to work properly 
# Authors: Onurcan Cekem & Bob Rip
#################################################
import pygame, sys, time
from pygame.locals import *
import os
import glob
import random
import time


# shows all music in the music folder found on Desktop.
def DivideAllMusic(): 
    file_counter = 0
    music_list = []
    os.chdir("/home/pi/Desktop/Music") # folder destination
    for file in glob.glob("*.ogg"): # select all files that end with .ogg
        music_list.append(file) #put all files in an array  
        file_counter += 1
    return music_list

#Randomly selects an audio file from given music_list with a random amount of time it plays the file
def Randomizer(music_list):
    #randomizer
    music_file = music_list[random.randint(0, len(music_list)-1)]#choose random audio file
    pygame.mixer.music.load(f"/home/pi/Desktop/Music/{music_file}")#load music file
    pygame.mixer.music.play()

    time_length = random.randint(1, 3)

    #debug
    print("playing music file: " + str(music_file) + " for " + str(time_length) + "s")
    
    
    return time_length
    
    
    

random.seed(time.time())               

#print all found music files to pick from
list = os.listdir("/home/pi/Desktop/Music/")
print("Here is a list of all found music files: ")
print(list)
print("\n")

#print only .ogg files
list = glob.glob("/home/pi/Desktop/Music/*.ogg")
print("Here is a list of all found music files with .ogg: ")
print(list)
print("\n")

pygame.init()

music_list = DivideAllMusic()

#DISPLAYSURF = pygame.display.set_mode((400,300))
#pygame.display.set_caption('Memes.')
pygame.mixer.music.set_volume(0.8)
#pygame.mixer.music.load("/home/pi/Desktop/tupac.ogg")
pygame.mixer.music.load("/home/pi/Desktop/Music/biggie.ogg")
#soundChannelA = pygame.mixer.Channel(1)
pygame.mixer.music.play()

time_length = 0
prev_timer = 0
print("Music list: ")
print(music_list)

while True:
    
    timer = time.time()
    
    if (timer - prev_timer >= time_length): # if time exceeded
        prev_timer = timer
        time_length = Randomizer(music_list)# select new song
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
