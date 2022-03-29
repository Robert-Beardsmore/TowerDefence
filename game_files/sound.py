import os

import pygame

from .settings import Settings

pygame.init()

#Sound effects class will contain all logic needed for a sound effect to play
class Sound_Effects:
    hit_sound = pygame.mixer.Sound(os.path.join("game_files/sounds","hit.wav"))
    press_sound = pygame.mixer.Sound(os.path.join("game_files/sounds","press.wav"))
    lose = pygame.mixer.Sound(os.path.join("game_files/sounds","lose.wav"))
    enemy = pygame.mixer.Sound(os.path.join("game_files/sounds","enemy.wav"))
    win = pygame.mixer.Sound(os.path.join("game_files/sounds","win.wav"))
    '''button_press
    upgrade
    sell
    purchase
    place_tower
    hit
    deafeat_enemy
    win
    lose
    pause
    resume'''
    Sounds  = {1: hit_sound,
        2: press_sound,
        3: lose,
        4: enemy,
        5: win}

    @staticmethod
    def play_sound(number):
        if not Settings.Sound_Effect:
            return
        pygame.mixer.Sound.play(Sound_Effects.Sounds[number])
