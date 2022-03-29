#Pygame is imported: Used for collision detection and graphics rendering
import pygame

#sys is imported: Used for closing program
import sys

#Colours from colours is imported: Used for accessing pre-made colours
from .colours import Colours

#Player_Accounts from player accounts is imported: Used to check username and password
from .player_accounts import Player_Accounts

from .player_account import Player_Account

#Settings from settings imported: Used to access screen
from .settings import Settings

from .maps import Maps

from .towers import Towers

from .sound import *

from time import sleep


#------------------------------General Buttons---------------------------#

#Button class made: Used for making buttons on screen
class Button:
    buttons = []

    #This data holds the message that will be displayed to screen when something has been done wrong
    message = None
    #The initialisation function: Called when class instance is created. Takes the paramters needed and makes all button attributes
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):

        #Parameters assigned to attributes
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name
        self.active_colour = active_colour
        self.inactive_colour = inactive_colour

        #Attributes that can be made from paramters
        self.font = pygame.font.Font(None,64)
        self.name_surface = self.font.render(self.name,True,Colours.black)
        self.name_rect = self.name_surface.get_rect(center=(self.x+self.width/2,self.y+self.height/2))
        self.colour = inactive_colour
        self.rect = pygame.Rect(x,y,width,height)
        message_surface = self.font.render('',True,Colours.black)
        Button.buttons.append(self)

    #Checks if mouse is clicked and colliding with button
    def events(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                Sound_Effects.play_sound(2)
                self.on_press()

    #on_press function: Empty in parent class
    def on_press(self):
        pass

    #update function: Used to update colour of button depending on mouse position
    def update(self):
        if self.collision():
            self.colour = self.active_colour
        else:
            self.colour = self.inactive_colour

    #draw function: Used to render graphics to the screen that is passed as a parameter
    def draw(self):
        pygame.draw.rect(Settings.screen, self.colour, self.rect)
        Settings.screen.blit(self.name_surface, self.name_rect)


    #collision function: Used to determine if current mouse position is in the buttons coordinates
    def collision(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())


    #display_message function: Used to change the message that will be displayed to screen
    def display_message(self, message,x,y):#20,600
        surface = self.font.render(message,True,Colours.white)
        Settings.screen.blit(surface,(x,y))
        pygame.display.flip()
        sleep(0.4)

class ButtonText(Button):
    def __init_(self,x,y,width,height,name,active_colour,inactive_colour,alt_text):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)
        self.text = self.name
        self.alt_text = alt_text

    def change(self):
        if self.text == self.alt_text:
            self.text = self.name
        else:
            self.text = self.alt_text
        self.name_surface = self.font.render(self.text,True,Colours.black)
        self.name_rect = self.name_surface.get_rect(center=(self.x+self.width/2,self.y+self.height/2))

#------------------------------Account System Buttons---------------------------#
#Quit button is made: Used to quit the game when pressed
class Quit_Button(Button):

    #Initialisation function: Used to create class attributes when object is made
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    #on_press function: Used to quit the game
    def on_press(self):
        pygame.quit()
        sys.exit()

#login_Button is made: Used to log player into their account
class Login_Button(Button):

    #Initialisation function: Used to create class attributes when object is made
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    #on_press function
    def on_press(self):
        #0 is username 1 is password
        if Settings.username and Settings.password:
            if Player_Accounts.check_username(Settings.username):
                if Player_Accounts.check_password(Settings.username,Settings.password):
                    Settings.Game_Data = Player_Accounts.Accounts[Settings.username]
                    #loads main menu
                    Player_Accounts.set_data()
                else:
                    self.display_message('Incorrect Password',20,600)
            else:
                self.display_message('Username does not exist',20,600)
        else:
            self.display_message('Invalid Username or Password',20,600)

#Create_Account_Button is made: Used to create an account for the player
class Create_Account_Button(Button):

    #Initialisation function: Used to create class attributes when object is made
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    #on_press function
    def on_press(self):
        if Settings.username and Settings.password:
            if Player_Accounts.check_username(Settings.username) == False:
                print('Account added')
                Player_Accounts.Add_Account(Settings.username,Settings.password)
                Settings.Game_Data = Player_Accounts.Accounts[Settings.username]
                Player_Accounts.set_data()
            else:
                self.display_message('Username already exists',20,600)
        else:
            self.display_message('Invalid Username or Password',20,600)

#------------------------------Main Menu Buttons---------------------------#

class Go_Back_button(Button):
    #Initialisation function: Used to create class attributes when object is made
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    def on_press(self):
        Settings.current_Page = Settings.page_Stack.pop()


    #---------------------------Main Menu Page Buttons-------------------------#



class open_game_Button(Button):
    #Initialisation function: Used to create class attributes when object is made
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    def on_press(self):
        if Settings.current_Map and Settings.towers:
            Settings.change_to_game = True
        else:
            self.display_message('You cannot start a game',20,800)

#class opens the buy page
class open_Buy_Page_Button(Button):
    #Initialisation function: Used to create class attributes when object is made
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    def on_press(self):
        Settings.page_Stack.append(Settings.current_Page)
        Settings.current_Page = Settings.page_Dict[3]
        Settings.changed_display = True

#class opens the settings page
class open_Settings_Page_Button(Button):
    #Initialisation function: Used to create class attributes when object is made
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    def on_press(self):
        Settings.page_Stack.append(Settings.current_Page)
        Settings.current_Page = Settings.page_Dict[2]
        Settings.changed_display = True
        Settings.changed_sound_effects = True

#Class opens the select map page
class open_select_Map_Page_Button(Button):
    #Initialisation function: Used to create class attributes when object is made
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    def on_press(self):
        Settings.page_Stack.append(Settings.current_Page)
        Settings.current_Page = Settings.page_Dict[6]
        Settings.changed_display = True
        self.set_data()

    def set_data(self):
        Settings.changed_select_map = True
        Settings.page_Dict[6].is_Active()

#class opens the buy map page
class open_buy_Map_Page_Button(Button):
    #Initialisation function: Used to create class attributes when object is made
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    def on_press(self):
        Settings.page_Stack.append(Settings.current_Page)
        Settings.current_Page = Settings.page_Dict[4]
        Settings.changed_display = True
        self.set_data()

    def set_data(self):
        Settings.changed_buy_map = True
        Settings.page_Dict[4].is_Bought()

#class opens the buy towers page
class open_buy_Tower_Page_Button(Button):
    #Initialisation function: Used to create class attributes when object is made
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    def on_press(self):
        Settings.page_Stack.append(Settings.current_Page)
        Settings.current_Page = Settings.page_Dict[5]
        Settings.page_Dict[5].is_Bought()
        Settings.changed_display = True

#button is used to save and quit game
class Save_Button(Button):
    #Initialisation function: Used to create class attributes when object is made
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    def on_press(self):
        #Save Game
        Player_Accounts.Save_Accounts()
        pygame.quit()
        sys.exit()

    #------------------------------Settings Page Buttons---------------------------#

#Button is used to turn sound effects on or off
class Sound_Effects_Button(ButtonText):
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour,alt_text):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)
        self.text = self.name
        self.alt_text = alt_text

    def on_press(self):
        Settings.Sound_Effect = not Settings.Sound_Effect
        Settings.changed_sound_effects = True

    #------------------------------Buy Page Buttons---------------------------#


    #------------------------------Maps Page Buttons---------------------------#

    #------------------------------Tower Page Buttons---------------------------#

#Class will make a button that will chagne the tower being displayed
class left_Tower_Arrow(Button):
    #Function calls Button __init__ function
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    #Function will display the next tower in the list
    def on_press(self):
        Settings.tower_index = (Settings.tower_index-1) % Towers.total
        Settings.current_Tower = Towers.towers[Settings.tower_index]
        Settings.changed_tower = True

#Class will make a button that will change the tower bieng displayed
class right_Tower_Arrow(Button):
    #Function calls Button __init__ function
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    def on_press(self):
        Settings.tower_index = (Settings.tower_index+1) % Towers.total
        Settings.current_Tower = Towers.towers[Settings.tower_index]
        Settings.changed_tower = True

#Class will make a button that will change the map being displayed
class left_buy_Map_Button(Button):
    #Function calls Button __init__ function
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    def on_press(self):
        Settings.buy_map_index = (Settings.buy_map_index-1) % Maps.total
        Settings.current_buy_Map = Maps.maps[Settings.buy_map_index]
        Settings.changed_buy_map = True
        Settings.changed_display = True

#Class will make a butotn that will change the map being displayed
class right_buy_Map_Button(Button):
    #Function calls Button __init__ function
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    def on_press(self):
        Settings.buy_map_index = (Settings.buy_map_index+1) % Maps.total
        Settings.current_buy_Map = Maps.maps[Settings.buy_map_index]
        Settings.changed_buy_map = True
        Settings.changed_display = True

#Class will make a button that will change the map being displayed
class left_select_Map_Button(Button):
    #Function calls Button __init__ function
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    def on_press(self):
        Settings.select_map_index = (Settings.select_map_index-1) % Settings.select_map_total
        Settings.current_select_Map = Settings.maps[Settings.select_map_index]
        Settings.changed_select_map = True

#Class will make a butotn that will change the map being displayed
class right_select_Map_Button(Button):
    #Function calls Button __init__ function
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    def on_press(self):
        Settings.select_map_index = (Settings.select_map_index+1) % Settings.select_map_total
        Settings.current_select_Map = Settings.maps[Settings.select_map_index]
        Settings.changed_select_map = True

#Button will attempt to purchase the selected tower
class Buy_Tower_Button(ButtonText):
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour,alt_text):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)
        self.alt_text = alt_text
        self.text = self.name

    def on_press(self):
        if Settings.current_Tower not in Settings.towers:
            #Check for money
            if Settings.current_Tower.cost <= Settings.Money:
                self.make_purchase()

            else:
                self.display_message("You do not have enough to buy this.",20,630)
        else:
            self.display_message('You already have this tower',20,630)

    def make_purchase(self):
        #Subtracts the money from the player
        Settings.Money -= Settings.current_Tower.cost

        #Adds tower to list and then updates the button display
        Settings.towers.append(Settings.current_Tower)
        Settings.changed_tower = True

#Button will attempt to purchase the selected map
class Buy_Map_Button(ButtonText):
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour,alt_text):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)
        self.alt_text = alt_text
        self.text = self.name

    def on_press(self):
        if Settings.current_buy_Map not in Settings.maps:
            if Settings.current_buy_Map.cost <=Settings.Money:
                self.make_purchase()

            else:
                self.display_message("You do not have enough to buy this.",20,630)
        else:
            self.display_message("You already have this map",20,630)

    def make_purchase(self):
        #Makes purchase
        Settings.Money -= Settings.current_buy_Map.cost

        #Adds map to list of maps and updates button display
        Settings.maps.append(Settings.current_buy_Map)
        Settings.select_map_total +=1
        Settings.changed_buy_map = True
        Settings.changed_display = True

    #------------------------------Select Maps Page Buttons---------------------------#

#Butotn will Set the active map to the map being selected
class Set_Active_Button(ButtonText):
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour,alt_text):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)
        self.alt_text = alt_text
        self.text = name


    def on_press(self):
        Settings.current_Map = Settings.current_select_Map
        Settings.active_Map = Settings.current_select_Map
        self.change()


#------------------------------Game Buttons---------------------------#

class Pause_Button(Button):
    #Initialisation function: Used to create class attributes when object is made
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    #Pause button will pause game and open up pause menu
    def on_press(self):
        Settings.Pause_state = True
        Settings.Framerate = 30
        Settings.Speed_Up = False
        Settings.auto_Start = False

class Resume_Button(Button):
    #Initialisation function: Used to create class attributes when object is made
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    #Leaves pause menu and resumes game
    def on_press(self):
        Settings.Pause_state = False

class Game_Quit_Button(Button):
    #Initialisation function: Used to create class attributes when object is made
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    #Leaves pause menu, game and then returns to main menu
    def on_press(self):
        Settings.Pause_state = False
        Settings.Game_state = False
        Settings.Main_Menu_state = True

class Speed_Button(Button):
    #Initialisation function: Used to create class attributes when object is made
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)
        self.active_colour_old = self.active_colour
        self.inactive_colour_old = self.inactive_colour

    #Speed Button will increase or decrease the framerate
    def on_press(self):
        if Settings.auto_Start == False:
            Settings.Framerate *= 2
            Settings.auto_Start = True
        else:
            Settings.Framerate //= 2
            Settings.auto_Start = False
        #self.active_colour,self.inactive_colour = self.inactive_colour,self.active_colour

    def update(self):
        super().update()
        if Settings.auto_Start == False:
            self.inactive_colour = self.inactive_colour_old
            self.active_colour = self.active_colour_old
        else:
            self.inactive_colour = self.active_colour_old
            self.active_colour = self.inactive_colour_old


#Will upgrade the active tower
class Upgrade_Button(Button):
    #Initialisation function: Used to create class attributes when object is made
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)
        self.font = pygame.font.Font(None,32)

    def update(self):
        super().update()
        self.update_image()

    def update_image(self):
        if Settings.active_Tower:
            name = "Upgrade: "+str(int(Settings.active_Tower.upgrade_cost))
        else:
            name = "Upgrade: "
        self.name_surface = self.font.render(name,True,Colours.black)
        self.name_rect = self.name_surface.get_rect(center=(self.x+self.width/2,self.y+self.height/2))

    #Upgrade button will increase the stats of the tower if the player has enough money
    def on_press(self):
        if Settings.active_Tower:
            if Settings.active_Tower.can_upgrade():
                Settings.active_Tower.make_payment()
                Settings.active_Tower.new_total()
                Settings.active_Tower.update_cost()
                Settings.active_Tower.update_level()
                Settings.active_Tower.upgrade()
                self.update_image()

#Button will sell the selected Tower
class Sell_Button(Button):
    #Initialisation function: Used to create class attributes when object is made
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)
        self.font = pygame.font.Font(None,32)

    def update(self):
        super().update()
        self.update_image()


    def update_image(self):
        super().update()
        if Settings.active_Tower:
            name = "Sell: "+str(int(Settings.active_Tower.sell_cost))
        else:
            name = "Sell: "
        self.name_surface = self.font.render(name,True,Colours.black)
        self.name_rect = self.name_surface.get_rect(center=(self.x+self.width/2,self.y+self.height/2))

    #Sell button will sell the tower and remove it from the screen
    def on_press(self):
        if Settings.active_Tower:
            Settings.active_Tower.refund_money()
            Settings.active_Tower.remove_Tower()
            self.update_image()


class end_Game_Quit_Button(Button):
    #Initialisation function: Used to create class attributes when object is made
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    #Button will appear when a player has won or lost a map and will return them to the main menu
    def on_press(self):
        Settings.end_Game_state = False
        Settings.Game_state = False
        Settings.Pause_state = False
        Settings.Main_Menu_state = True
        Settings.game = None

class Continue_Button(Button):
    #Initialisation function: Used to create class attributes when object is made
    def __init__(self,x,y,width,height,name,active_colour,inactive_colour):
        super().__init__(x,y,width,height,name,active_colour,inactive_colour)

    #butotn will reward the player and then continue the game
    def on_press(self):
        #Add money to player account
        #Add experience to player account
        Settings.end_Game_state = False









