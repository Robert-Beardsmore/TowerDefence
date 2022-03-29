#Display Class
import pygame
from .colours import Colours
from .settings import Settings

pygame.init()
class Display:
    def __init__(self,x,y,imgOrtxt,img_txt,font_size=64):
        self.x = x
        self.y = y
        #True for Text;False for Image
        self.imgOrtxt = imgOrtxt
        self.img_txt = img_txt
        self.font_size = font_size
        self.surface = self.get_surface()

    def get_surface(self):
        if self.imgOrtxt == True:
            Font = pygame.font.Font(None,self.font_size)
            Surface = Font.render(self.img_txt,True,Colours.white)
            return Surface
        else:
            return self.img_txt

    def draw(self):
        Settings.screen.blit(self.surface,(self.x,self.y))


class Stat_Display():
    def __init__(self,x,y,tower):
        self.x = x
        self.y = y
        self.font = pygame.font.Font(None,64)
        self.tower = tower
        self.surface = self.make_surface()

    def make_surface(self):
        surface = pygame.Surface((900,450),pygame.SRCALPHA)
        img = pygame.transform.scale(self.tower.img,(420,420))
        surface.blit(img,(0,0))
        #name,attack,t_range,attack_rate,cost,deploy_cost
        attack = self.return_surface('Attack: ',self.tower.attack)
        t_range = self.return_surface('Range: ',self.tower.t_range)
        attack_rate = self.return_surface('Attack Rate: ',self.tower.attack_rate)
        cost = self.return_surface('Cost: ',self.tower.cost)
        deploy_cost = self.return_surface('Deploy Cost: ',self.tower.deploy_cost)

        surface.blit(attack,(420,42))
        surface.blit(t_range,(420,126))
        surface.blit(attack_rate,(420,210))
        surface.blit(cost,(420,294))
        surface.blit(deploy_cost,(420,378))
        surface = pygame.transform.scale(surface,(675,300))
        return surface

    def return_surface(self,name,stat):
        return self.font.render(name+str(stat),True,Colours.white)

    def draw(self):
        Settings.screen.blit(self.surface,(self.x,self.y))
