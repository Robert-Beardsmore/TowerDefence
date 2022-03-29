#pygame imported: Used to render graphics and for collision detection
import pygame

#String imported: Used to provide list of accepted characters
import string

#Colours from colours imported: Used to access pre made colours
from .colours import Colours

from .settings import Settings

#Textbox class created: Used to define a textbox that can be used to enter input
class Textbox:
    #Stores valid characters
    Accepted = string.ascii_letters+string.digits+" "

    #Function creates attributes needed for a textbox to work
    def __init__(self,x,y,name,char_limit,private=False):
        self.x = x
        self.y = y
        self.name = name
        self.char_limit = char_limit
        self.private = private

        self.width = 520
        self.height = 60
        self.textbox_box = pygame.Rect(x,y,self.width,self.height)
        self.active = False
        self.active_col = Colours.white
        self.inactive_col = Colours.grey
        self.col = self.inactive_col

        self.input_text = ''
        self.display_text = ''
        self.font = pygame.font.Font(None,64)

        self.name_surface = self.font.render(self.name,True,Colours.white)
        self.name_rect = self.name_surface.get_rect(midbottom=(self.x+self.width/2,self.y))

        self.create_display_text_image()

    #Returns the surface and the rect for the text in the textbox
    def create_display_text_image(self):
        self.display_text_sur = self.font.render(self.display_text,True,Colours.white)
        self.display_text_rect = self.display_text_sur.get_rect(center=(self.x+self.width/2,self.y+self.height/2))

    #Function returns true if mouse is over textbox
    def check_collision(self):
        if self.textbox_box.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False

    #Function makes the textbox active
    def make_active(self):
        self.col = self.active_col
        self.active = True

    #Function makes the textbox inactive
    def make_inactive(self):
        self.col = self.inactive_col
        self.active = False

    #Function will update the display text
    def update_display_text(self):
        if self.private:
            self.display_text= '*'*len(self.input_text)
        else:
            self.display_text = self.input_text

    #Changes the text stored in settings so buttons can access it
    def update_text(self):
        if self.private:
            Settings.password = self.input_text
        else:
            Settings.username = self.input_text

    def text_change(self):
        self.update_display_text()
        self.create_display_text_image()
        self.update_text()


    #Function converts user input into textbox actions
    def events(self,event):
        #Checks if the user has pressed the textbox or not
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.check_collision():
                self.make_active()
            else:
                self.make_inactive()

        #Checks for any keyboard input from the user
        if self.active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                else:
                    if event.unicode in Textbox.Accepted and len(self.input_text) < self.char_limit:
                        self.input_text += event.unicode
                self.text_change()

    #Draws the input text to the screen
    def draw_display_text(self):
        Settings.screen.blit(self.display_text_sur,self.display_text_rect)

    #Draw function: Used to render textbox to screen
    def draw(self):
        #box
        pygame.draw.rect(Settings.screen,self.col,self.textbox_box,1,5)

        #name
        Settings.screen.blit(self.name_surface,self.name_rect)

        #inputted text
        self.draw_display_text()