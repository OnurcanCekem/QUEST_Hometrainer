import pygame
import tkinter
root=tkinter.Tk()
pygame.mixer.pre_init(44100, -16, 2, 2048)
file = '/home/pi/Desktop/2pac.mp3'
pygame.init()
pygame.mixer.init()
volume = pygame.mixer.music.get_volume()
printable_vol = "{:.2f}".format(volume)
print("Volume: "+ printable_vol)
pygame.mixer.music.load(file)
#pygame.mixer.music.load('/home/pi/Desktop/2pac.mp3')
pygame.mixer.music.play(-1)
#pygame.event.wait()
#pygame.mixer.music.play(-1)
#while pygame.mixer.music.get_busy():
#    pygame.time.Clock().tick(10)

#continue
#    pygame.time.Clock().tick(60)
root.mainloop()
#    pygame.event.poll()