import pygame, sys, time
from pygame.locals import *

pygame.init()

#DISPLAYSURF = pygame.display.set_mode((400,300))
#pygame.display.set_caption('Memes.')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load("/home/pi/Desktop/tupac.ogg")
#soundChannelA = pygame.mixer.Channel(1)
pygame.mixer.music.play()
while True: #infinite loop
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    print("Press 'v' to check and adjust volume")
    print("Press 'a' to get_sound")
    print("Press 'b' has no use so far")
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
    elif query == 'b':
        print("  Currently has no use lmao")
#pygame.mixer.music.play()
#time.sleep()
#pygame.mixer.music.stop()
#pygame.quit()
