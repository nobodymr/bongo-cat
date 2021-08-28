import tkinter as tk
from tkinter import simpledialog

import pygame

from settings import Settings as SETTINGS
from sprites import BongoCat, Arrow, Text

from midi import *
from backgrounds import *
from sounds import *
from leaderboards import *


tk.Tk().withdraw()
PLAYER = ''

# Создаем игру и окно
pygame.init()
screen = pygame.display.set_mode(SETTINGS.SCREENSIZE, pygame.FULLSCREEN) if SETTINGS.FULLSCREEN else pygame.display.set_mode(SETTINGS.SCREENSIZE)

pygame.display.set_caption("Bongo cat")
pygame.display.set_icon(pygame.image.load(SETTINGS.IMAGEFOLDER + "icon.jpg").convert())


class Abstract(object):
    def update(self, *args):
        screen.blit(self.image, self.rect)


class BongoCat(Abstract, BongoCat):
    pass
class Arrow(Abstract, Arrow):
    pass


sprites = pygame.sprite.Group()

cat = BongoCat()
arrow = Arrow()

sprites.add(cat)
sprites.add(arrow)

clock = pygame.time.Clock()


MAINSCREEN = True
START = False
GAMEOVER = False

soundkeys = [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]


def message(text, surface=screen, x=15, y=30, size=16):
    Text(size, text, (0, 0, 0), x, SETTINGS.HEIGHT - y).draw(surface)


def showtopresults():
    results = get_leaderboards()[:10][::-1]
    for i in range(len(results)):
        row = results[i]
        message(row[0] + ' - ' + str(row[1]), x=SETTINGS.WIDTH // 1.4, y=30 * (i + 1))
    message("Топ-10:", x=SETTINGS.WIDTH // 1.4, y=30*(len(results) + 1))


def inputname():
    global PLAYER

    while not PLAYER:
        PLAYER = simpledialog.askstring(title="", prompt="Как тебя зовут?", initialvalue="Ваня")
    PLAYER = PLAYER.upper()


def main():
    global MAINSCREEN, START, GAMEOVER, PLAYER

    oops = False
    score = 0
    attempts = SETTINGS.ATTEMPTS
    running = True

    allowmeowsound = True
    allowtadasound = True
    allowlosesound = True
    
    allowrecordscore= True
    allowinputname = True

    newrecord = False

    while running:
        if MAINSCREEN:
            screen.fill((255,255,255))
            screen.blit(cat.image, cat.rect)

            message("Привет!", x=SETTINGS.WIDTH // 2 + 20, y=SETTINGS.HEIGHT // 2 + 80, size=30)
            message("Нажми Пробел для новой игры! Достигни счета " + str(SETTINGS.WINSCORE) + "!")

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    MAINSCREEN = False
                    START = True
        elif GAMEOVER:
            START = False
            MAINSCREEN = False

            if attempts <= 0:
                screen.blit(bedroom, (0, 0))
                screen.blit(cat.image, cat.rect)

                message("У тебя получится, " + PLAYER + "! Попробуй ещё!", y=120)

                if allowlosesound:
                    allowlosesound = False
                    lose.play()
            else:
                screen.blit(party, (0, 0))
                screen.blit(cat.image, cat.rect)

                message("Победа! Ты молодец, " + PLAYER + "!", y=120)

                if allowtadasound:
                    allowtadasound = False
                    tada.play()

            if allowrecordscore:
                allowrecordscore = False
                newrecord = leaderboards(PLAYER, score)

            if newrecord:
                message("Рекорд!", x=SETTINGS.WIDTH // 2 + 20, y=SETTINGS.HEIGHT // 2 + 80, size=30)
            
            showtopresults()
            message("Имя: {}".format(PLAYER), y=90)
            message("Счет: {}".format(score), y=60)
            message("Пробел - новая игра. Enter - поменять имя.")

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    PLAYER = ''
                    if allowinputname:
                        allowinputname = False
                        inputname()
                if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    allowmeowsound = True
                    allowtadasound = True
                    allowlosesound = True

                    allowrecordscore = True
                    allowinputname = True

                    score = 0
                    attempts = SETTINGS.ATTEMPTS
                    oops = False

                    GAMEOVER = False
                    START = True
        elif START:
            if attempts <= 0 or score == SETTINGS.WINSCORE:
                GAMEOVER = True
            if not score:
                if allowmeowsound:
                    allowmeowsound = False
                    meow.play()
                
                inputname()

            # Обновление
            sprites.update()

            # Рендеринг
            screen.blit(concert, (0, 0))
            sprites.draw(screen)
            
            if oops:
                message("Упс...", x=SETTINGS.WIDTH // 2 + 20, y=SETTINGS.HEIGHT // 2 + 80, size=30)
            
            message("Имя: {}".format(PLAYER), y=90)
            message("Счет: {}".format(score), y=60)
            message("Прав на ошибку: {}".format(attempts))

            # Ввод процесса (события)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                    running = False
                if event.type == pygame.KEYDOWN and event.key in soundkeys:
                    cat.next_skin()
                    play_random_note()

                    correcttop = event.key == soundkeys[0] and arrow.skin == 'top'
                    correctbottom = event.key == soundkeys[1] and arrow.skin == 'bottom'
                    correctright = event.key == soundkeys[2] and arrow.skin == 'right'
                    correctleft = event.key == soundkeys[3] and arrow.skin == 'left'
                    
                    if correcttop or correctbottom or correctleft or correctright:
                        score += 1
                        oops = False
                    else:
                        attempts -= 1
                        oops = True
                        wobble.play()

                    arrow.next_skin()

        # Держим цикл на правильной скорости
        clock.tick(SETTINGS.FPS)

        pygame.display.update()


main()

pygame.midi.quit()
pygame.mixer.quit()
pygame.quit()