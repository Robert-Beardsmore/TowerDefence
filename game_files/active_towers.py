#Active Towers
import pygame
pygame.font.init()

from .settings import Settings

from .colours import Colours

from .projectile import Projectile

import math

class Active_Tower:
    font = pygame.font.Font(None,35) #font used to render level of tower to the screen
    def __init__(self,x,y,tower):
        #Stores the grid position that the tower is on
        self.x = x
        self.y = y

        #Stores the x and y coord of the circle for the radius
        self.circle_x = self.x
        self.circle_x, self.circle_y = Settings.grid_to_screen(self.x,self.y)
        self.circle_x +=30
        self.circle_y +=30

        #Stores the x and y position of the tower on the screen
        self.pos_x,self.pos_y = Settings.grid_to_screen(self.x,self.y)

        #Store the tower that the active tower is
        self.tower = tower

        #Stores the width and height of the tower
        self.width = Settings.width
        self.height = Settings.height

        #Stores the tower as a pygame.Rect object to make use of inbuilt collision
        self.tower_rect = pygame.Rect(self.pos_x,self.pos_y,self.width,self.height)

        #Stores the decrease of the total cost that the tower can be sold for
        self.sell_per = 0.75

        #Stores the total amount of money that has been spent on the tower
        self.total_cost = self.tower.deploy_cost

        #Stores the amount of money that is returned to the player when the tower is sold
        self.sell_cost = self.total_cost * self.sell_per

        #Stores how much each upgrade cost will increase by
        self.upgrade_in = 1.5

        #Stores how much it will cost to upgrade the tower to the next level
        self.upgrade_cost = self.tower.deploy_cost * self.upgrade_in

        #Stores the current level of the tower
        self.level = 1

        #Stores the level of the tower as a pygame.Surface object so it can be rendered to the screen
        self.level_surface = self.font.render(str(self.level),True,Colours.white)

        #Stores the radius of the tower as a pygame.Surface object so it can be rendered to the screen
        self.radius_surface = self.make_radius()

        #Data needed for attacking
        self.target = None

        #Stores the framecount used to calculate the time between each shot
        self.frame_count = 0

        #Stores the damage that the tower deals
        self.damage = self.tower.attack

    #Function will find a new enemy to shoot at
    def set_target(self):
        found = False
        for enemy in Settings.active_Enemies:
            distance = self.cal_distance(enemy.x-30,enemy.y+30)
            #If the enemy is outside of the range of the tower
            if self.tower.radius >= abs(distance):
                if enemy == self.target and enemy.alive: return
                #If there is already a target this code will run
                elif self.target:
                    #Does the enemy have a lower number than the target enemy
                    if enemy.number < self.target.number and enemy.alive:
                        self.target = enemy
                        found = True
                #If no current target this target needs to be set as the target
                else:
                    self.target= enemy
                    found = True
        #No targets found means nothing in range
        if not found:
            self.target = None

    #Function will fire a projectile towards the target enemy
    def attack(self):
        if self.target:
            if self.target.alive == True and self.can_attack():
                Settings.projectiles.append(Projectile(self.circle_x,self.circle_y,self.target,self.damage))
                self.set_timer()


    #Function will take the centre of the enemy and return the distance from it to the player
    def cal_distance(self,x,y):
        dis_x = x - self.circle_x
        dis_y = y - self.circle_y
        distance = math.sqrt((dis_x**2)+(dis_y**2))
        return distance

    def can_attack(self):
        time  = self.frame_count // Settings.Framerate
        if Settings.auto_Start:
            time /=2
        if time >= self.tower.attack_rate:
            return True
        else:
            return False

    def set_timer(self):
        self.frame_count = 0
        #frame_count // frame_rate

    #converts user input into valid commands
    def events(self,event):
        x,y = pygame.mouse.get_pos()
        #Condition to keep mouse within map and tower select by using x and y of infor display and buttons
        if 0<=y<=180 and  0<=x<=720:
            return
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:#left click
            if self.tower_rect.collidepoint((x,y)):
                Settings.active_Tower = self
                return True
            else:
                return False

    #Function will update tower data
    def update(self):
        self.frame_count +=1
        self.set_target()
        self.attack()

    #Makes the transparent radius of the tower that can then be drawn to the screen in the draw radius function
    def make_radius(self):
        surface = pygame.Surface(Settings.screen.get_size(), pygame.SRCALPHA)#Makes transparent surface
        pygame.draw.circle(surface,Colours.grey,(self.circle_x,self.circle_y),self.tower.radius) #Draws circle to new surface
        surface.set_alpha(128) #Makes circle transparent
        return surface

    def draw_radius(self):
        Settings.screen.blit(self.radius_surface,(0,0)) #Draws surface to screen

    #Draws tower from Settings.active_Towers
    def draw(self):
        Settings.screen.blit(self.tower.img,(self.pos_x,self.pos_y))
        Settings.screen.blit(self.level_surface,(self.pos_x,self.pos_y))

    #These functions are used to store logic for upgrading a button
    def can_upgrade(self):
        if self.upgrade_cost <= Settings.money:
            return True

    #Deduct upgrade cost from player money
    def make_payment(self):
        #Integer used to keep player money as an int
        Settings.money -= int(self.upgrade_cost)

    #Calculate new total cost of tower
    def new_total(self):
        self.total_cost += self.upgrade_cost

    #Function will update the cost of upgrading the tower to match the new level
    def update_cost(self):
        #Adds the amount spent to the toal cost so new sell cost can be calculated
        self.upgrade_cost *= self.upgrade_in
        self.upgrade_cost = int(self.upgrade_cost)

        #The sell cost of the tower also needs changing
        self.sell_cost = self.total_cost * self.sell_per

    #function will update the level of the tower to match the new level
    def update_level(self):
        #Changes the level of the tower so new level can be seen
        self.level +=1

        #Reassigns the level surface so new level can be seen
        self.level_surface =  self.font.render(str(self.level),True,Colours.white)

    def upgrade(self):
        self.damage +=1

    #These functions allow the tower to be sold
    #Function will return money to the player
    def refund_money(self):
        Settings.money += int(self.sell_cost)

    #Function will remove the tower from active towers
    def remove_Tower(self):
        Settings.active_Towers.remove(self)
        Settings.current_Map.map_grid[self.y][self.x] = '2'
        Settings.active_Tower = None


