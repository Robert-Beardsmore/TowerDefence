import pygame

from .settings import Settings

from .colours import Colours

import random

from .enemies import *

from .sound import *


#Round class for round management
class Round:
    def __init__(self):
        self.yet_to_spawn = []

        #Stores the framecount since the start of the round
        self.frame_count = 0

        #1 - difficulty level from enemy
        self.easy = True
        #2 - difficulty level from enemy
        self.medium = False
        #3 - difficulty level from enemy
        self.hard = False
        #4 - difficulty level from enemy
        self.run_and_hide = False

        #gets the startings coordinates that all enemies will spawn at
        self.x,self.y = Settings.grid_to_screen(Settings.current_Map.start[0]-1,Settings.current_Map.start[1]-1)

        #Stores the time of the last enemy spawn
        self.last_spawn = 0

        self.running = False

        self.make_round()

    def make_difficulty(self):
        #Enemies will get harder as the player progresses through the rounds
        if Settings.game_round ==5:
            self.medium = True
            self.decrease_speed(1,2)

        elif Settings.game_round == 15:
            self.hard = True
            self.decrease_speed(2,2)

        elif Settings.game_round == 30:
            self.run_and_hide = True
            self.decrease_speed(3,2)

    #Increase the rate at which enemies in the previous difficulty/s spawn
    def decrease_speed(self,dif,num):
        for enemy in Enemy.enemies:
            if enemy.difficulty <= dif:
                enemy.cool_down /=num

    def add_Enemy(self,i):
        if self.run_and_hide:
            if i //5 == 0:
                self.random_Enemy(Enemy.run_and_hide)
            elif i // 2 == 0:
                self.random_Enemy(Enemy.hard)
            else:
                self.random_Enemy(Enemy.medium)

        elif self.hard:
            if i //5 == 0:
                self.random_Enemy(Enemy.hard)
            elif i // 2 == 0:
                self.random_Enemy(Enemy.medium)
            else:
                self.random_Enemy(Enemy.easy)

        elif self.medium:
            if i //3 == 0:
                self.random_Enemy(Enemy.medium)
            else:
                self.random_Enemy(Enemy.easy)
        else:
            self.random_Enemy(Enemy.easy)



    #Function will use the round number from Settings to calculate which enemies should appear on the map and when
    def make_round(self):

        number_of_enemies = 2 + int(1.5*Settings.game_round)

        self.make_difficulty()
        for i in range(number_of_enemies):
            self.add_Enemy(i)

        if Settings.game_round == Settings.current_Map.end+1: #uses the end attribute from a map class that will determine the ending round
            self.win()

    #Function will make the player win
    def win(self):
        self.make_reward()
        Sound_Effects.play_sound(5)
        Settings.end_Game_state = True
        Settings.won = True
        Settings.changed_display = True

    def make_reward(self):
        Settings.Money += 10 * Settings.game_round
        Settings.add_Experience()

    #Returns a random enemy from the list
    def random_Enemy(self,en_list):
        self.yet_to_spawn.append(random.choice(en_list))



    #Function will reset data ready for next round
    def end_round(self):
        self.yet_to_spawn = []
        #self.frame_count = 0
        self.last_spawn = 0

    #Function will spawn an enemy to the screen
    def spawn(self):
        enemy = self.yet_to_spawn.pop(0)
        Settings.active_Enemies.append(Active_Enemy(self.x,self.y,enemy))

    #Function will determine if an enemy can be spawned
    def can_spawn(self):
        now = pygame.time.get_ticks()
        time_between_spawn = now - self.last_spawn

        #Cool down in seconds time_between_spawn in ms
        if time_between_spawn >= (self.yet_to_spawn[0].cool_down *1000):
            self.last_spawn = now
            return True
        else:
            return False

    def can_end(self):
        if not Settings.active_Enemies and not self.yet_to_spawn:
            return True
        else:
            return False

    def end(self):
        Settings.game_round +=1
        self.last_spawn = 0
        self.make_round()
        self.running = False
        self.go_again()

    #Function determines if the round should start automatically
    def go_again(self):
        if Settings.auto_Start:
            self.running = True

    #Function will spawn enemies onto the map
    def spawner(self):
        if not self.is_Empty():
            if self.can_spawn():
                self.spawn()
        else:
            if self.can_end():
                self.end()

    def is_Empty(self):
        if not self.yet_to_spawn:
            return True

    def events(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.running = True

    #Function will update the frame count
    def update(self):
        if self.running:
            self.spawner()

    def draw(self):
        pass


#Issue game round not updating - not changing round before making round


