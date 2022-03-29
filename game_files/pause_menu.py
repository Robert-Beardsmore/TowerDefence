import pygame

from .settings import Settings

from .colours import Colours

from .button import Resume_Button,Game_Quit_Button

#Puase Menu
class Pause_Menu:
    def __init__(self):
        self.Class_instances = []
        self.resume_button = self.new_instance(Resume_Button(250,300,500,100,'Resume',Colours.lightBlue,Colours.blue))
        self.quit_button = self.new_instance(Game_Quit_Button(250,450,500,100,'Quit',Colours.lightBlue,Colours.blue))
        self.surface = pygame.Surface(Settings.screen.get_size())
        self.surface.fill(Colours.grey)
        self.surface.set_alpha(20)

    def new_instance(self,instance):
        self.Class_instances.append(instance)
        return instance

    def run(self):
        if not Settings.Pause_state:
            return
        self.events()
        self.update()
        self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Settings.Pause_state = False
            for instance in self.Class_instances: instance.events(event)

    def update(self):
        for instance in self.Class_instances: instance.update()

    def draw(self):
        Settings.screen.blit(self.surface,(0,0))
        for instance in self.Class_instances: instance.draw()
        pygame.display.update()
