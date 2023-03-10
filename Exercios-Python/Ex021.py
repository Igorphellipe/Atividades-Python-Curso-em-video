import pygame
input('Aperte enter para reproduzir o MP3 !!!')
pygame.mixer.init()
pygame.mixer.music.load('jorge.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
