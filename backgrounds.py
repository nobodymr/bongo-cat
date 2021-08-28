import pygame

from settings import Settings as SETTINGS


concert = pygame.transform.scale(pygame.image.load(SETTINGS.IMAGEFOLDER + 'concert.png'), SETTINGS.SCREENSIZE)
bedroom = pygame.transform.scale(pygame.image.load(SETTINGS.IMAGEFOLDER + 'bedroom.png'), SETTINGS.SCREENSIZE)
party = pygame.transform.scale(pygame.image.load(SETTINGS.IMAGEFOLDER + 'party.png'), SETTINGS.SCREENSIZE)