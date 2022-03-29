import pygame
import sys
from .button import Login_Button, Create_Account_Button, Quit_Button
from .colours import Colours
from .textbox import Textbox
from .settings import Settings
from .player_accounts import Player_Accounts
from .player_account import Player_Account
pygame.init()

#Account_System Account is made: Used to Run the Account System
class Account_System:

    #Initialisation function: Used to asseign attributes
    def __init__(self):
        self.buttons = []
        self.textboxes = []
        #Stores the class instances of the different textboxes on screen
        self.username_Textbox = self.new_textbox(Textbox(300,300,'username',12))
        self.password_Textbox = self.new_textbox(Textbox(300,500,'password',12,True))

        #Stores the class instances of the different buttons on screen
        self.login_Button = self.new_button(Login_Button(25,700,450,200,'Login',Colours.lightBlue,Colours.blue))
        self.create_account_Button = self.new_button(Create_Account_Button(525,700,450,200,'Create Account',Colours.lightBlue,Colours.blue))
        self.quit_Button = self.new_button(Quit_Button(0,0,200,200,'X',Colours.lightBlue,Colours.blue))

    #Takes a button class instance, adds it to the list of buttons and then returns the button
    def new_button(self,button):
        self.buttons.append(button)
        return button

    #Takes a textobx class instance, add it to the list of textboxes and then returns the textbox
    def new_textbox(self,textbox):
        self.textboxes.append(textbox)
        return textbox

    #Function will be called in a loop and run the game
    def run(self):
        if not Settings.Account_System_state:
            return
        self.events()
        self.update()
        self.draw()

    #Function will convert user input into actions
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Settings.Account_System_state = False

                #First state of game so just needs to quit
                Settings.Quit()

            #Event function for each instance called with events passed in
            for button in self.buttons: button.events(event)
            for textbox in self.textboxes: textbox.events(event)

    #Function will update the button to change colour if the mouse is over them
    def update(self):
        for button in self.buttons: button.update()

    #Function will render all graphics to the screen
    def draw(self):
        #Resets screen for new image to be rendered
        Settings.screen.fill(Colours.black)

        #Draws all the class instances
        for button in self.buttons: button.draw()
        for textbox in self.textboxes: textbox.draw()

        #Needed to update display
        pygame.display.update()

