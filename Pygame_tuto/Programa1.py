import pygame, sys

pygame.init()

size= width, height = 300,300
color = 0,0,0
display=pygame.display.set_mode(size)
helmet= pygame.image.load("daedric.jpg")
display.fill(color)
display.blit(helmet, [0,0])
pygame.display.flip()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
