from random import randint

import pygame.midi


# Создаем note player
pygame.midi.init()
midi_out = pygame.midi.Output(0)
midi_out.set_instrument(2) # Electric Grand Piano

def midi(note, volume=127): # 74 is middle C, 127 is "how loud" - max is 127
    for n in note:
        midi_out.note_on(n, volume)
def play_random_note():
    midi([randint(60, 96)])