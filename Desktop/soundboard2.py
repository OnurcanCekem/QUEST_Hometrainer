import pygame, sys, time
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Memes.')

pygame.mixer.music.load("/home/pi/Desktop/tupac.ogg")
pygame.mixer.music.play()
time.sleep(2)
pygame.mixer.music.stop()
pygame.quit()
