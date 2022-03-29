import pygame
pygame.font.init()
from .settings import Settings

from .colours import Colours

from .button import Sell_Button, Upgrade_Button

#Information Display
class Information_Display:
    font = pygame.font.Font(None,45)
    def __init__(self,x,y): #x 90,y 0
        self.x = x
        self.y = y
        self.width = 630
        self.height = 180
        self.surface = pygame.Surface((self.width,self.height))
        self.surface.fill(Colours.purple)
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.money_display = self.make_money()
        self.round_display = self.make_round()
        self.health_display = self.make_health()
        self.sell_Button = Sell_Button(480,0,240,90,'Sell',Colours.lightBlue,Colours.blue)
        self.upgrade_Button =Upgrade_Button(480,90,240,90,'Upgrade: ',Colours.lightBlue,Colours.blue)

    def make_money(self):
        surface = self.font.render(f"Money: {Settings.money}",True,Colours.black) #uses current money that the player has
        return surface

    def make_round(self):
        surface = self.font.render(f"Round: {Settings.game_round}",True,Colours.black) #Uses current round number
        return surface

    def make_health(self):
        surface = self.font.render(f"Health: {Settings.health}",True,Colours.black)
        return surface

    def events(self,event):
        self.sell_Button.events(event)
        self.upgrade_Button.events(event)

    def update(self):
        self.money_display = self.make_money()
        self.round_display = self.make_round()
        self.health_display = self.make_health()
        self.sell_Button.update()
        self.upgrade_Button.update()

    def draw(self):
        Settings.screen.blit(self.surface,self.rect)
        Settings.screen.blit(self.money_display,(90,15))
        Settings.screen.blit(self.round_display,(90,75))
        Settings.screen.blit(self.health_display,(90,135))
        if Settings.active_Tower:
            Settings.screen.blit(pygame.transform.scale(Settings.active_Tower.tower.img,(180,180)),(300,0))
        self.sell_Button.draw()
        self.upgrade_Button.draw()
