import pygame
from settings import Settings as SETTINGS


pygame.mixer.init()

meow = pygame.mixer.Sound(SETTINGS.SOUNDFOLDER + 'meow.wav')
wobble = pygame.mixer.Sound(SETTINGS.SOUNDFOLDER + 'wobble.wav')
tada = pygame.mixer.Sound(SETTINGS.SOUNDFOLDER + 'tada.wav')
lose = pygame.mixer.Sound(SETTINGS.SOUNDFOLDER + 'lose.wav')