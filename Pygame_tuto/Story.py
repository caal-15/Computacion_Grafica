import pygame, sys
from time import sleep

pygame.init()

size = width, height = 614 ,461
display = pygame.display.set_mode(size)
pygame.mixer.init()
song=pygame.mixer.Sound("PFS.ogg") 
song.set_volume(1.0)
song.play()
for i in range (1, 230):
    if(i<10):
        image=pygame.image.load("Frames/00%s.jpg" % i)
        
    elif (i<100):   
        image=pygame.image.load("Frames/0%s.jpg" % i)
    else:
        image=pygame.image.load("Frames/%s.jpg" % i)
    display.blit(image, [0,0])
    pygame.display.flip()
    sleep(0.13)
sleep(2)    
song.fadeout(3000)
sys.exit()

  

        
