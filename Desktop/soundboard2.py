import pygame, sys, time
from pygame.locals import *
import os
import glob
        
# shows all music in the music folder found on Desktop.
def show_all_music(): 
    os.chdir("/home/pi/Desktop/Music") # folder destination
    for file in glob.glob("*.ogg"): # select all files that end with .ogg
        print(file)

# shows all music in the music folder found on Desktop.
def select_new_song(selectedsong): 
    pygame.mixer.music.load(f'/home/pi/Desktop/Music/{selectedsong}')
    pygame.mixer.music.play()

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

#DISPLAYSURF = pygame.display.set_mode((400,300))
#pygame.display.set_caption('Memes.')
pygame.mixer.music.set_volume(0.8)
#pygame.mixer.music.load("/home/pi/Desktop/tupac.ogg")
pygame.mixer.music.load("/home/pi/Desktop/Music/biggie.ogg")
#soundChannelA = pygame.mixer.Channel(1)
pygame.mixer.music.play()



while True: #infinite loop
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    print("Press 'v' to check and adjust volume")
    print("Press 'a' to get_sound")
    print("Press 'q' to change music")
    query = input("  ")
    
    if query == 'p':
        pygame.mixer.music.pause()
    elif query == 'r':
        pygame.mixer.music.unpause()
    elif query == 'e':
        pygame.mixer.music.stop()
        break
    elif query == 'v':
        print(" Current volume: " + str(pygame.mixer.music.get_volume()))
        print(" Please input a value between 0.0 and 1.0")
        setvolume = float(input("  "))
        pygame.mixer.music.set_volume(setvolume)
        print(" Volume set to: " + str(pygame.mixer.music.get_volume()))
    elif query == 'a': # returns 1 when paused, interesting
        print("  Current busy status: " + str(pygame.mixer.music.get_busy()))
    elif query == 'q':
        print("Here is a list of all eligible music files with .ogg: ")
        show_all_music()
        requestsong = input("  ")
        print("\n")
        select_new_song(requestsong)


#pygame.mixer.music.play()
#time.sleep()
#pygame.mixer.music.stop()
#pygame.quit()
