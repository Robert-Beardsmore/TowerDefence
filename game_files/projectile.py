import pygame

from .settings import Settings

from .colours import Colours

from .sound import *

import math


#Projectile class for a projectile that a tower can spawn to deal damage to an enemy
class Projectile:
    def __init__(self,x,y,target,damage):
        self.x = x
        self.y = y
        self.target= target
        self.speed = 40
        self.angle = self.cal_vector()
        self.radius = 10
        self.damage = damage


    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    def update(self):
        self.move()
        self.check_collision()

    def cal_vector(self):
        dis_x = (self.target.x+30) - self.x
        dis_y = (self.target.y+30) - self.y
        angle = math.atan2(dis_y,dis_x)
        return angle

    def check_collision(self):
        pro_rect = pygame.Rect(self.x,self.y,self.radius,self.radius)
        enemy_rect = pygame.Rect(self.target.x,self.target.y,self.target.width,self.target.height)
        if pro_rect.colliderect(enemy_rect):
            self.die(enemy_rect)

    def die(self,enemy_rect):

        Settings.projectiles.remove(self)
        pygame.draw.rect(Settings.screen,Colours.red,enemy_rect)
        pygame.display.update()
        Sound_Effects.play_sound(1)
        if self.target.alive:
            self.target.take_damage(self.damage)


    def draw(self):
        pygame.draw.circle(Settings.screen,Colours.red,(self.x,self.y),self.radius)#5 is radius