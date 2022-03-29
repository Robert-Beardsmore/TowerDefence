import pygame

from .settings import Settings

from .colours import Colours

from .button import end_Game_Quit_Button,Continue_Button

from .sound import *

#End Game class will store either the win display or the lose display
class End_Game:
    def __init__(self):
        self.font = pygame.font.Font(None,192)
        self.win_buttons = []
        self.lose_buttons = []

        #Both win and lose button
        self.quit_Button = self.both_Buttons(end_Game_Quit_Button(250,750,500,100,'Quit',Colours.lightBlue,Colours.blue))

        #Win button
        self.continue_Button = self.make_Button(Continue_Button(250,600,500,100,'Continue',Colours.lightBlue,Colours.blue),True)

        #Stores the title and the position of the title that will tell the player if they won or lost
        self.win_title_sur,self.win_title_rect = self.make_title(True)
        self.lose_title_sur,self.lose_title_rect = self.make_title(False)


    def both_Buttons(self,button):
        self.win_buttons.append(button)
        self.lose_buttons.append(button)
        return button

    def make_Button(self,button,win):
        if win:
            self.win_buttons.append(button)
            return button
        else:
            self.lose_buttons.append(button)
            return button


    def make_title(self,won):
        #won is a bool that is passed when the class is created, it will determine if the display needs to be a win screen or a lose screen
        if won:
            text_surface = self.font.render('Victory',True,Colours.white)
        else:
            text_surface = self.font.render('Defeat',True,Colours.white)
        x,y = Settings.screen.get_size()
        rect = text_surface.get_rect(center=(x/2,y*0.25))
        return text_surface,rect

    def run(self):
        if not Settings.end_Game_state:
            return
        self.events()
        self.update()
        self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Settings.end_Game_state = False
                Settings.Game_state = False
                Settings.Main_Menu_state = True
            if Settings.won:
                for button in self.win_buttons: button.events(event)
            else:
                for button in self.lose_buttons: button.events(event)

    def update(self):
        if Settings.won:
            for button in self.win_buttons: button.update()
        else:
            for button in self.lose_buttons: button.update()

    def draw(self):
        Settings.screen.fill(Colours.black)
        if Settings.won:
            for button in self.win_buttons: button.draw()
            Settings.screen.blit(self.win_title_sur,self.win_title_rect)
        else:
            for button in self.lose_buttons: button.draw()
            Settings.screen.blit(self.lose_title_sur,self.lose_title_rect)

        pygame.display.update()
#not calling draw function - fixed

''' code from before buttons
import pygame

from settings import Settings

from colours import Colours


#End Game class will store either the win display or the lose display
class End_Game:
    def __init__(self):
        self.font = pygame.font.Font(None,64)
        self.win_buttons = []
        self.lose_buttons = []

        #Both win and lose button
        self.quit_Button = None

        #Lose button
        self.restart_Button = None

        #Win button
        self.continue_Button = None

        #Stores the title and the position of the title that will tell the player if they won or lost
        self.win_title_sur,self.win_title_rect = self.make_title(True)
        self.lose_title_sur,self.lose_title_rect = self.make_title(False)


    def make_Button(self,button,win):
        if win:
            self.win_buttons.append(button)
            return button
        else:
            self.lose_buttons.append(button)
            return button


    def make_title(self,won):
        #won is a bool that is passed when the class is created, it will determine if the display needs to be a win screen or a lose screen
        if won:
            text_surface = self.font.render('Victory',True,Colours.white)
        else:
            text_surface = self.font.render('Defeat',True,Colours.white)
        x,y = Settings.screen.get_size()
        rect = text_surface.get_rect(center=(x/2,y/2))
        return text_surface,rect

    def make_reward(self):
        if self.won:
            #Add reward for completing map onto player money
            #Add experience to the player
            pass

    def run(self):
        if not Settings.end_Game_state:
            return
        self.events()
        self.update()
        self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Settings.end_Game_state = False
                Settings.Game_state = False
                Settings.Main_Menu_state = True

    def update(self):
        if Settings.won:
            for button in self.win_buttons: button.update()
        else:
            for butotn in self.lose_buttons: button.update()

    def draw(self):
        Settings.screen.fill(Colours.black)
        for button in self.buttons: button.draw()
        if Settings.won:
            Settings.screen.blit(self.win_title_sur,self.win_title_rect)
        else:
            Settings.screen.blit(self.lose_title_sur,self.lose_title_rect)

        pygame.display.update


'''
