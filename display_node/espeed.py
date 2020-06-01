import pygame
import time

red    = [255,0,0]
white  = [255,255,255]
blue   = [0,0,255]
yellow = [255,255,0]
black  = [0,0,0]

xres = 800
yres = 600

pygame.init()
pygame.font.init()

#screen = pygame.display.set_mode((1366,768), pygame.FULLSCREEN)
screen = pygame.display.set_mode((xres,yres), pygame.RESIZABLE)
pygame.display.set_caption("ESPeed racing")

displayInfo = pygame.display.Info()

barY = displayInfo.current_h/4
barW = displayInfo.current_w

# draw bars
laneBars = [
        {'t':black,'c':red,'x':0,'y':0,'w':barW,'h':displayInfo.current_h/4},
        {'t':black,'c':white,'x':0,'y':barY,'w':barW,'h':displayInfo.current_h/4},
        {'t':white,'c':blue,'x':0,'y':barY*2,'w':barW,'h':displayInfo.current_h/4},
        {'t':black,'c':yellow,'x':0,'y':barY*3,'w':barW,'h':displayInfo.current_h/4}
    ]
for l in laneBars:
    pygame.draw.rect(screen,l['c'],[l['x'],l['y'],l['w'],l['h']],0)

# draw last lap time
font = pygame.font.Font('freesansbold.ttf', int(barY*.8))
for l in laneBars:
    text = font.render('0.0000',True,l['t'],l['c'])
    screen.blit(text, (10,l['y']))

# draw lap count
font = pygame.font.Font('freesansbold.ttf', int(barY*.3))
for l in laneBars:
    text = font.render('Lap 1/20',True,l['t'],l['c'])
    screen.blit(text,(barW*.6,l['y']+(l['h']*.1)))

# draw best lap time
font = pygame.font.Font('freesansbold.ttf', int(barY*.3))
for l in laneBars:
    text = font.render('Best 0.0000',True,l['t'],l['c'])
    screen.blit(text, (barW*.6,l['y']+(l['h']*.6)))

pygame.display.flip()

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

pygame.quit()
