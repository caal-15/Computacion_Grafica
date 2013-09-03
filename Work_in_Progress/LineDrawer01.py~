import pygame, sys
from pygame.locals import *
from time import sleep
pygame.init()



def drawLine (x0, y0, x1, y1, screen):
    steep = abs(y1 - y0) > abs(x1 - x0)
    if steep:
        tmp = x0
        x0 = y0
        y0 = tmp
        tmp = x1
        x1 = y1
        y1= tmp
    if x0 > x1:
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp 
   
    dx = x1 - x0
    dy = abs (y1 - y0)
    error = dx/2
    ystep = 0
    y = y0
    if y0 < y1: ystep = 1
    else: ystep = -1
    for x in range (x0, x1+1):
        if steep: screen.set_at([y, x], [0,0,0])
        else: screen.set_at([x,y], [0,0,0])
        error = error - dy
        if error < 0:
            y = y + ystep
            error = error + dx    
        
    


screen =pygame.display.set_mode([800, 600])
screen.fill([255,255,255])
flag = 1
x0 = 0
y0 = 0
x1 = 1
y1 = 1
flag2=1
while 1:
    events = pygame.event.get()  
    for event in events:
        if event.type == QUIT: 
            sys.exit()
        if event.type == KEYDOWN and event.key == K_m:
            flag2 = not flag2
            flag = not flag
    if pygame.mouse.get_pressed()[0]:
        if flag:
            x0 = pygame.mouse.get_pos()[0]
            y0 = pygame.mouse.get_pos()[1]
            #flag = 0
            if (x0 !=  x1 or y0 != y1) or flag2: flag = 0
        else:
            x1 = pygame.mouse.get_pos()[0]
            y1 = pygame.mouse.get_pos()[1]
            if (x0 !=  x1 or y0 != y1):
                drawLine(x0,y0, x1, y1, screen)
                flag = 1
    pygame.display.flip()
         


'''
myfont = pygame.font.SysFont("monospace", 15)
label = myfont.render("Some text!", 1, (0,0,0))
screen.blit(label, (100, 100))
pygame.display.flip()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
'''
