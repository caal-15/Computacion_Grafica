import pygame, sys, math

pygame.init
size = width, height = 1000, 700
x = 3
y = 3
ymov= 0
g=0.2

screen= pygame.display.set_mode(size)
helmet= pygame.image.load("daedric.jpg")
rect_helmet=helmet.get_rect()
color= 0,0,0
counter=0
while 1:
    if rect_helmet.bottom == height:
        y=0.8*y
        x=0.6*x
    if (g<0 and (y<=0 or rect_helmet.top < 0)) or (g>0 and rect_helmet.bottom < height):
        g=0.2
        y=y+g
        ymov=y
        
    else:
        g=-0.2
        y=y+g
        ymov=-y
    if(rect_helmet.left<0 or rect_helmet.right>width):
        x=-x
    
    if height - rect_helmet.bottom <= 0.5:
        counter=counter+1
    else:
        counter=0
    if counter > 16:
        x=0
    
    rect_helmet=rect_helmet.move(x,ymov)
    screen.fill(color)
    screen.blit(helmet, rect_helmet)
    pygame.display.flip()
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT: 
            sys.exit()
