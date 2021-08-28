import os
import pygame.freetype

pygame.font.init()


class Settings():
	WIDTH = 768
	HEIGHT = 432
	SCREENSIZE = WIDTH, HEIGHT
	FPS = 30
	FULLSCREEN = False

	GAMEFOLDER = os.path.dirname(__file__)
	DATABASE = GAMEFOLDER + '\\bongocat.db'
	IMAGEFOLDER = os.path.join(GAMEFOLDER, 'assets', 'img\\')
	SOUNDFOLDER = os.path.join(GAMEFOLDER, 'assets', 'sounds\\')
	FONTPATH = os.path.join(GAMEFOLDER, 'assets', 'fonts', 'zametka\\') + 'zametka.otf'

	WINSCORE = 50
	ATTEMPTS = 5