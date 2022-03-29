#Pygame imported and initialised
import pygame
pygame.init()

#Settings class from settings module imported
from .settings import Settings

#Colours class from colours module imported
from .colours import Colours

#Imports buttons needed
from .button import Resume_Button,Game_Quit_Button

#Pause Menu for game will run when game is paused.
class Pause:
    def __init__(self):
        self.resume = Resume_Button(250,300,500,100,'Resume',Colours.lightBlue,Colours.blue)
        self.quit = Game_Quit_Button(250,450,500,100,'Quit',Colours.lightBlue,Colours.blue)
        self.surface = pygame.Surface(Settings.screen.get_size())
        self.surface.fill(Colours.grey)
        self.surface.set_alpha(20)
        self.buttons = [self.resume, self.quit]

    def run(self):
        self.events()
        self.update()
        self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Settings.Pause_state = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                for button in self.buttons: button.event()

    def update(self):
        for button in self.buttons: button.update()

    def draw(self):
        Settings.screen.blit(self.surface,(0,0))
        for button in self.buttons: button.draw()

        pygame.display.update()
