#pygame imported to access built in functions for screen rendering
import pygame

#Settings from settings imported to access the games important information
from .settings import Settings

#Colours from colours imported to access pre defined colours
from .colours import Colours

from .button import Speed_Button,Pause_Button

from .pause_menu import Pause_Menu

from .tower_select import Tower_Select

from .information_display import Information_Display

from .enemies import *

from .rounds import Round

from .endgame import End_Game

from .maps import Maps


#Game class, stores game loop
class Game:

    #All class instances initialised
    def __init__(self):
        self.init_game()
        self.Class_instances = []
        self.pause_button = self.new_instance(Pause_Button(0,0,90,90,'||',Colours.lightBlue,Colours.blue))
        self.pause_menu = Pause_Menu()
        self.info_display = self.new_instance(Information_Display(90,0))
        self.speed_button = self.new_instance(Speed_Button(0,90,90,90,'>>',Colours.lightBlue,Colours.blue))
        self.tower_select = self.new_instance(Tower_Select(720,0,280,900))
        self.round = self.new_instance(Round())
        self.end_game = End_Game()

    def init_game(self):
        Settings.health = 10
        Settings.money = 75
        Settings.active_Towers = []
        Settings.active_Enemies = []
        Settings.game_round = 1
        Settings.active_Tower = None
        Settings.active_Map.map_grid = Settings.active_Map.make_array()
        Settings.won = False


    def new_instance(self,instance):
        self.Class_instances.append(instance)
        return instance


    #The actual game loop
    def run(self):
        if not Settings.Game_state:
            return
        Settings.clock.tick(Settings.Framerate)
        if Settings.Pause_state:
            self.pause_menu.run()
        elif Settings.end_Game_state:
            self.end_game.run()
        else:
            self.events()
            self.update()
            self.draw()

    #Converts user input into game commands
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Settings.Game_state = False
                Settings.Main_Menu_state = True
            for instance in self.Class_instances: instance.events(event)
            Bools = []
            for tower in Settings.active_Towers:
                Bools.append(tower.events(event)) #Collisions return True if collided
                if True not in Bools and None not in Bools: #If no True value or no values at all no tower has been pressed
                    Settings.active_Tower = None #Player has not pressed a tower
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    Settings.Sound_Effect = not Settings.Sound_Effect

    #Updates game based on user input
    def update(self):
        for instance in self.Class_instances: instance.update()
        for tower in Settings.active_Towers: tower.update()
        for enemy in Settings.active_Enemies: enemy.update()
        for projectile in Settings.projectiles: projectile.update()


    #Renders all graphics to the screen
    def draw(self):
        Settings.screen.fill(Colours.black)
        Settings.active_Map.draw(0,180) #Coords of map on the screen
        for enemy in Settings.active_Enemies: enemy.draw() #Draws all the enemies to the screen
        if Settings.active_Tower: Settings.active_Tower.draw_radius() # Draws the radius of the active tower to the screen
        for tower in Settings.active_Towers: tower.draw() #Draws each tower placed on the map to the screen
        for projectile in Settings.projectiles: projectile.draw()
        for instance in self.Class_instances: instance.draw() #Renders all of the class instances made with the new_instance function
        pygame.display.update()


#Framerate goes to 30 if speed up and then paused. - fixed by adding new update function


'''
Current track of changes while google docs is down
- edited deselecting tower by making invlaid region the tower select and main buttons
- issue found: tower being placed appears under all other towers - fixed by changing order of drawing
- need to change sell button to display the amount given when sold - solved by adding new update function
- issue - making a tower the active tower slows the enemies down caused by draw function for active tower - changed draw function still issues with references to active tower
-temp fix for enemy path finding, added to isvalid function with if and elif statements

'''