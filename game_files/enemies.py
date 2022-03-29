import pygame

from .settings import Settings

from .sound import Sound_Effects

from .colours import Colours

import os
import sys
import random
import math

#Enemy class will define base of enemy
class Enemy:
    enemies = []
    easy = []
    medium = []
    hard = []
    run_and_hide = []
    def __init__(self,img_ref,health,speed,damage,reward,difficulty,cool_down):
        self.img = self.make_image(img_ref)
        self.health = health
        self.speed = speed
        self.damage = damage
        self.reward = reward
        self.difficulty = difficulty
        self.cool_down = cool_down

        Enemy.enemies.append(self)
        if self.difficulty == 1:
            Enemy.easy.append(self)
        elif self.difficulty == 2:
            Enemy.medium.append(self)
        elif self.difficulty == 3:
            Enemy.hard.append(self)
        elif self.difficulty == 4:
            Enemy.run_and_hide.append(self)

    def make_image(self,ref):

        img = pygame.image.load(os.path.join("game_files/enemy_img", ref)).convert()
        img = pygame.transform.scale(img,(60,60))
        img = img.convert()
        return img
#active Enemy class will define enemy on map
class Active_Enemy:

    horizontal ={
        'east':1,
        'west':-1}
    vertical = {
        'north':-1,
        'south':1}
    number = 0

    def __init__(self,x,y,enemy): #map start starts at 1 not 0
        self.x = x #x coord on screen
        self.y = y #y coord on screen
        self.enemy = enemy
        self.current_direction = 'south'
        self.past_direction = self.current_direction
        self.temp_list = self.make_temp_list() #Stores the current plane of direction in a list format
        self.alive = True
        self.number = Active_Enemy.number
        Active_Enemy.number +=1
        self.width = Settings.width
        self.height = Settings.height
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.health = self.enemy.health

    def make_temp_list(self):
        if self.current_direction in self.horizontal:
            return list(self.vertical)
        else:
            return list(self.horizontal)



    def Follow_Path(self):
        self.tar_x,self.tar_y = self.set_Target()
        if self.alive:
            if self.move(self.tar_x,self.tar_y):
                self.past_direction = self.current_direction
                self.apply()
                self.temp_list = self.make_temp_list()
                return
            else:
                self.tar_x,self.tar_y = self.set_Target()


    #Calculates the next tile in the current direction until a valid tile is found
    def set_Target(self):
        set_target = False
        while not set_target and self.alive:
            #Needs spceial consideration if going north or south
            if self.current_direction == 'north':
                grid_x,grid_y = Settings.screen_to_grid(self.x,self.y+59)
                grid_y -=1

            elif self.current_direction == 'east':
                grid_x,grid_y = Settings.screen_to_grid(self.x,self.y)
                grid_x +=1

            elif self.current_direction == 'south':
                grid_x,grid_y = Settings.screen_to_grid(self.x,self.y)
                grid_y +=1

            elif self.current_direction == 'west':
                grid_x,grid_y = Settings.screen_to_grid(self.x+59,self.y)
                grid_x -= 1

            set_target = self.is_Valid(grid_x,grid_y)
            if not set_target:
                self.current_direction = self.change_direction()
        return Settings.grid_to_screen(grid_x,grid_y)

    def is_Valid(self,grid_x,grid_y):
        try:
            if Settings.current_Map.path_grid[grid_y][grid_x] == '1' and grid_x >=0 and grid_y>=0: #map_grid contains true false values with a path tile being False
                return True
            else:
                return False
        except IndexError: #The enemy could be at the edge of the map so this need to be taken into account
            return False

    def change_direction(self):
            if self.temp_list:
                choice = self.temp_list.pop() #Dictionary put into list format for random.choice to be used
                return choice
            else:
                self.deal_damage()

    def deal_damage(self):
        #deal damage
        Settings.take_damge(self.enemy.damage)
        self.die()

    def die(self):
        self.alive = False
        Sound_Effects.play_sound(4)
        Settings.active_Enemies.remove(self)


        #pygame.quit()
        #sys.exit()
        #Settings.active_Enemies.remove(Settings.current_enemy)



    def move(self,x,y): #Takes the target x and the target y coord
        dis_x,dis_y = x - self.x,y-self.y #Using vectors to calculate movement
        if int(dis_x) ==0 and int(dis_y) ==0: #If the enemy is past the target the distance between them will be negative
            self.movement_x = self.movement_y = 0
            return False
        angle = math.atan2(dis_y,dis_x)
        self.movement_x = math.cos(angle) * self.enemy.speed
        self.movement_y = math.sin(angle) * self.enemy.speed
        return True

    def apply(self):
        self.x += int(self.movement_x)
        self.y += int(self.movement_y)

    def update(self):
        self.Follow_Path()


    def draw(self):
        Settings.screen.blit(self.enemy.img,(self.x,self.y))

    #Takes damage form a projectile
    def take_damage(self,damage):
        self.health -= damage
        pygame.draw.rect(Settings.screen,Colours.red,(self.x,self.y,self.width,self.height))
        pygame.display.update()
        if self.health <= 0:
            self.alive = False
            Settings.active_Enemies.remove(self)
            Settings.money += self.enemy.reward

#ref, health, speed, damage, reward, difficulty,cool_down
#easy enemies
enemy_3 = Enemy('enemy_3.png',1,3,1,5,1,1.5)
#medium enemies
enemy_1 = Enemy('enemy_1.png',7,2,2,20,2,2)
#hard enemies
enemy_5 = Enemy('enemy_5.png',3,60,1,5000,3,1)
enemy_2 = Enemy('enemy_2.png',100,1,5,100,3,3)
#run and hide enemies
enemy_4 = Enemy('enemy_4.png',500,1,50,1000,4,2)
