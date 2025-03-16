import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1080,720))
pygame.display.set_caption('GAME')

cx,cy = 540,360

running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[K_RIGHT] and cx <= 1055:
        cx += 20
    elif keys[K_LEFT] and cx >= 25:
        cx -= 20
    elif keys[K_UP] and cy >= 25:
        cy -= 20
    elif keys[K_DOWN] and cy <= 695:
        cy += 20
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(255,0,0),(cx,cy), 25)
    pygame.display.flip()

pygame.quit()