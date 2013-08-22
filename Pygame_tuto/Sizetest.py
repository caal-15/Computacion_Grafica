import sys, math, pygame
from time import sleep

pygame.init()

maxh=1300

for i in range(10,maxh):
    size = i, i
    display=pygame.display.set_mode(size)
    pygame.display.flip()
    sleep(30)
    
