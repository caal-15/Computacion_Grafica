import pygame, math, sys

size = width,height = 800 , 600
screen = pygame.display.set_mode(size)


a = 0
b = 0
c = 0
d = 0
color = 255,255,255
color_screen = 0,0,0



a=100
b=100
c= 200
d=200

def drawpixel(c,x,y):
    pygame.draw.rect(screen, c,[x,y,3,3])
    pygame.display.flip()

vector_x = 0
vector_y = 0
alfa = 0
vector_x = c-a
vector_y = d-b
c1=255
c2=50
screen.fill([0,0,0])
counter=5
while 1:
      
    for i in range(0,360):
        
        if c1 <=0 :
            c1=255
        else:
            c1= c1-1
        if c2>c1:
            c2=c2-c1
        else:
            c2=c1-c2        
        color=[c2, c1 ,c1]        
        alfa = alfa + 0.01
        pixel_x = int(alfa*((math.sin(i)*counter)**2))
        pixel_y = int(alfa*((math.cos(i)*counter)**2))
        if pixel_x >= 3*width or pixel_y >= 3*height:
            break
        print color    
        drawpixel(color,pixel_x,pixel_y)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    
    

