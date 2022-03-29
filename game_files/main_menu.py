#Main Menu
import pygame
import sys
from .pages import *
from .settings import Settings
from .game import Game

pygame.init()

class Main_Menu:
    def __init__(self):
        self.displays = []
        Settings.page_Dict = {
            1:Main_Menu_page('Main Menu',False),
            2:Settings_page('Settings'),
            3:Buy_Page('Buy'),
            4:Maps_Page('Buy Maps'),
            5:Towers_Page('Buy Towers'),
            6:Select_Map_Page('Select Map')
        }
        Settings.current_Page = Settings.page_Dict[1]
        self.Level = self.new_display(Display(0,0,True,'Level: '+str(Settings.Level)))
        self.Money = self.new_display(Display(560,0,True,'Money: '+str(Settings.Money)))

    def new_display(self,display):
        self.displays.append(display)
        return display

    def to_game(self):
        Settings.Main_Menu_state = False
        Settings.Game_state = True
        Settings.active_Map = Settings.current_Map
        Settings.game = Game()

    def update_displays(self):
        self.displays.remove(self.Level)
        self.displays.remove(self.Money)
        self.Level = self.new_display(Display(0,0,True,'Level: '+str(Settings.Level)))
        self.Money = self.new_display(Display(560,0,True,'Money: '+str(Settings.Money)))

    def run(self):
        if not Settings.Main_Menu_state:
            return
        self.events()
        self.update()
        self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            Settings.current_Page.events(event)

    def update(self):
        self.check_change()

        Settings.current_Page.update()

        self.check_display()

    def check_change(self):
        if Settings.change_to_game:
            self.to_game()
            Settings.change_to_game = False

    def check_display(self):
        if Settings.changed_display:
            self.update_displays()
            Settings.changed_display = False
        elif Settings.changed_tower:
            self.update_displays()


    def draw(self):
        Settings.current_Page.draw()
        for display in self.displays: display.draw()
        pygame.display.update()

