import pygame, sys
from pygame.locals import *
from time import sleep
pygame.init()
pygame.font.init()


def drawLine (x0, y0, x1, y1, screen, color):
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
        if steep: screen.set_at([y, x], color)
        else: screen.set_at([x,y], color)
        error = error - dy
        if error < 0:
            y = y + ystep
            error = error + dx    
        
    
screen =pygame.display.set_mode((800, 600))
myfont = pygame.font.SysFont("monospace", 14)
screen.fill((255,255,255))
pygame.display.set_caption("Line Drawer 0.5")
inst_label= myfont.render("Press 'm' to change drawing mode, 'c' to change color, press Space to clear", 1, (0,0,0), (255,255,255))
screen.blit(inst_label, (10, 20))
flag = 1
x0 = 0
y0 = 0
x1 = 1
y1 = 1
flag2 = 1
numcolor = 0
colors = ((0,0,0), (255, 0, 0), (0, 255, 0), (0,0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255))
while 1:
    pos_label = myfont.render("X:%s Y:%s" % (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 1, (0,0,0), (255, 255, 255))
    screen.blit(pos_label, (10, 580))
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT: 
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_m:
                flag2 = not flag2
                flag = not flag
            if event.key == K_c:
                if numcolor >= len(colors) - 1:
                    numcolor = 0
                else:
                    numcolor = numcolor + 1
            if event.key == K_SPACE:
                screen.fill((255,255,255))
                screen.blit(inst_label, (10, 20))
                flag = 1               
    if pygame.mouse.get_pressed()[0]:
        if flag:
            x0 = pygame.mouse.get_pos()[0]
            y0 = pygame.mouse.get_pos()[1]
            if (x0 !=  x1 or y0 != y1) or flag2: flag = 0
        else:
            x1 = pygame.mouse.get_pos()[0]
            y1 = pygame.mouse.get_pos()[1]
            if (x0 !=  x1 or y0 != y1):
                drawLine(x0,y0, x1, y1, screen, colors[numcolor])
                flag = 1
    pygame.display.flip()        

