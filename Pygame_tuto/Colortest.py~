import pygame, sys 
from time import sleep

pygame.init()

size= width, height = 300,300
color = 0,0,0
display=pygame.display.set_mode(size)


for i in range(0,255):
    for j in range (0, 255):
        for k in range(0, 255):
            color=i,j,k
            display.fill(color)
            pygame.display.flip()
            sleep(0.0005)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()

