import pygame, sys, math

pygame.init()
size = width, height = 1000, 700
x = 3
y = 3
screen= pygame.display.set_mode(size)
helmet= pygame.image.load("daedric.jpg")
rect_helmet=helmet.get_rect()
color= 0,0,0
while 1:
    if rect_helmet.left < 0 or rect_helmet.right > width:
        x=-x
    if rect_helmet.top < 0 or rect_helmet.bottom > height:
        y=-y 
    rect_helmet=rect_helmet.move(x, y)    
    screen.blit(helmet, rect_helmet)
    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()       
