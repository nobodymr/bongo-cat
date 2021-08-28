from random import randint

import pygame

from settings import Settings as SETTINGS


pygame.font.init()


class Text(object):
    def __init__(self, size, message, color, xpos, ypos):
        self.font = pygame.font.Font(SETTINGS.FONTPATH, size)
        self.surface = self.font.render(message, True, color)
        self.rect = self.surface.get_rect(topleft=(xpos, ypos))

        self.bg = pygame.Surface(self.surface.get_size())
        self.bg.fill((255, 165, 0)) # orange
        self.bg.blit(self.surface, (0, 0))

    def draw(self, surface):
        surface.blit(self.bg, self.rect)


class BongoCat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.skins = {'left': 'cat_l.png', 'right': 'cat_r.png'}
        self.get_skin()
        self.rect = self.image.get_rect()
        self.rect.center = (SETTINGS.WIDTH / 2, SETTINGS.HEIGHT / 2)


    def get_skin(self, name='left'):
        self.skin = name
        self.image = pygame.image.load(SETTINGS.IMAGEFOLDER + self.skins[name])
        return self.skins[name]


    def next_skin(self):
        return self.get_skin('left') if self.skin == 'right' else self.get_skin('right')


class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.skins = {'left': 'arrow-l.png', 'right': 'arrow-r.png', 'top': 'arrow-t.png', 'bottom': 'arrow-b.png'}
        self.next_skin()
        self.rect = self.image.get_rect()
        self.rect.topright = (SETTINGS.WIDTH - (15 if self.skin in ('left', 'right') else 35), 15)


    def get_skin(self, name):
        self.skin = name
        self.image = pygame.image.load(SETTINGS.IMAGEFOLDER + self.skins[name])
        return self.skins[name]


    def next_skin(self):
        self.skin = list(self.skins.keys())[randint(0, 3)]
        return self.get_skin(self.skin)