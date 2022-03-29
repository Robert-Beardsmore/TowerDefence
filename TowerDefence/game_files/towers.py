from .settings import Settings
import pygame
import os
#Tower class will store all towers in the game and enable more to be added
class Towers:

    #This list will store all of the tower class instances
    towers = []
    total = 0
    #The __init__ function will take unique data about the tower and then add the tower to the list
    def __init__(self,name,attack,t_range,attack_rate,cost,deploy_cost,img):
        #Name of the Tower
        self.name = name

        #Attack of the Tower
        self.attack = attack

        #The Range of the Tower
        self.t_range = t_range

        #The Attack rate of the Tower
        self.attack_rate = attack_rate

        #The cost to buy the Tower
        self.cost = cost

        #The cost to deploy the Tower
        self.deploy_cost = deploy_cost

        #The image of the Tower
        self.img = img.convert()

        #Radius stores size of range on screen
        self.radius = (Settings.height //2) +(self.t_range*Settings.height)

        #This Appends this class instance to the list of Towers.
        Towers.towers.append(self)
        Towers.total +=1



tower_1 = pygame.image.load(os.path.join('game_files/tower_img', 'tower_1.png'))
tower_2 = pygame.image.load(os.path.join('game_files/tower_img', 'tower_2.png'))
tower_3 = pygame.image.load(os.path.join('game_files/tower_img', 'tower_3.png'))
tower_4 = pygame.image.load(os.path.join('game_files/tower_img', 'tower_4.png'))
tower_5 = pygame.image.load(os.path.join('game_files/tower_img', 'tower_5.png'))
tower_6 = pygame.image.load(os.path.join('game_files/tower_img', 'tower_6.png'))
#name, attack, range, attack rate, cost deploy cost img
new_tower = Towers('Tower 1',1,2,0.5,0,50,tower_1)
new_tower = Towers('Tower 2',10,5,2,50,500,tower_2)
new_tower = Towers('Tower 3',1,10,1,1000,1000,tower_3)
new_tower = Towers('Tower 4', 1,10,0.5,5000,100,tower_4)
new_tower = Towers('Tower 5',99999,12,1,9000,10000,tower_5)
new_tower = Towers('Tower 6',1,1,0.1,9000,10,tower_6)
Settings.current_Tower = Towers.towers[0]