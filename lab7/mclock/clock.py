import pygame
import math
import time
from pygame.locals import *

pygame.init()

#images
bg = pygame.image.load('clock.png')
rh = pygame.image.load('mh.png')
lh = pygame.image.load('sh.png')
#display settings
screen = pygame.display.set_mode(bg.get_size())
pygame.display.set_caption('MICKEY')
W,H = bg.get_size()
center = (W//2,H//2)

def rotate_center(image,angle,position):
    rimage = pygame.transform.rotate(image,angle)
    new_r = rimage.get_rect(center=position)
    return rimage, new_r

stime = time.time()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    screen.fill((255,255,255))
    screen.blit(bg, (0,0))
    #timemechanic
    et = int(time.time()-stime)
    em = (et//60)%60
    es= et%60
    ma = - (em*6)
    sa = - (es*6)
    rm, mr = rotate_center(rh,ma, center)
    rs, sr = rotate_center(lh,sa,center)
    screen.blit(rm,mr.topleft)
    screen.blit(rs,sr.topleft)
    pygame.display.flip()
pygame.quit()