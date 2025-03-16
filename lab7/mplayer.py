import pygame
import os
from pygame.locals import *

pygame.init()



music_folder = "musics/"  
playlist = [os.path.join(music_folder, file) for file in os.listdir(music_folder) if file.endswith('.mp3')]

if not playlist:
    exit()

cs = 0
pygame.mixer.music.load(playlist[cs])
pygame.mixer.music.play()
playing = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                elif not playing:
                    pygame.mixer.music.unpause()
                    playing = True
            elif event.key == K_RIGHT:
                cs = (cs+1)%len(playlist)
                pygame.mixer.music.load(playlist[cs])
                pygame.mixer.music.play()
            elif event.key == K_LEFT:
                cs = (cs-1)%len(playlist)
                pygame.mixer.music.load(playlist[cs])
                pygame.mixer.music.play()

pygame.quit()
