import pygame, sys
from pygame.locals import *

pygame.init()

c = pygame.time.Clock()
image = pygame.image.load("./PySaver/pylogo.png")

window = pygame.display.set_mode((1920,1080))
trigger = True


x = 0
y = 0
speedx = 400
speedy = 250


while (trigger):
    for event in pygame.event.get():
        if event.type == QUIT:
            trigger = False
            
        delta = c.tick(60) / 1000
    
    x += speedx * delta
    y += speedy * delta
    
    if y + 200 > window.get_height() or y < 0:
        speedy *= -1    
    if x  + 200 > window.get_width() or x < 0:
        speedx *= -1  
            
    window.fill((0,0,0))
    window.blit(image,(x,y))
    pygame.display.update()        
            



pygame.quit()
