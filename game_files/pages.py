#Pages
import pygame
from .button import *
from .colours import Colours
from .display import *

class Page:
    def __init__(self,name,go_back=True):
        self.displays = []
        self.buttons = []
        self.name = name
        self.go_back = self.make_go_back(go_back)
        self.title = self.new_display(Display(140,140,True,self.name,200))

    def new_display(self,display):
        self.displays.append(display)
        return display

    def new_button(self,button):
        self.buttons.append(button)
        return button

    def make_go_back(self,go_back):
        if go_back == False:
            return None
        return self.new_button(Go_Back_button(0,700,200,200,'X',Colours.lightBlue,Colours.blue))

    def events(self,event):
        for button in self.buttons: button.events(event)

    def update(self):
        for button in self.buttons: button.update()

    def draw(self):
        Settings.screen.fill(Colours.black)
        for button in self.buttons: button.draw()
        for title in self.displays: title.draw()


class Main_Menu_page(Page):
    def __init__(self,name,go_back=True):
        super().__init__(name,go_back)
        self.play_Button = self.new_button(open_game_Button(250,300,500,100,'Play',Colours.lightBlue,Colours.blue))
        self.buy_Button = self.new_button(open_Buy_Page_Button(250,450,500,100,'Buy',Colours.lightBlue,Colours.blue))
        self.settings_Button = self.new_button(open_Settings_Page_Button(250,600,500,100,'Settings',Colours.lightBlue,Colours.blue))
        self.save_Button = self.new_button(Save_Button(250,750,500,100,'Save & Quit',Colours.lightBlue,Colours.blue))

#Page will allow the user to turn sound effects on or off and open the select map page
class Settings_page(Page):
    def __init__(self,name,go_back=True):
        super().__init__(name,go_back)
        self.sound_effects_Button = self.new_button(Sound_Effects_Button(250,300,500,100,'Sound Effects: On',Colours.lightBlue,Colours.blue,'Sound Effects: Off'))
        self.select_map_Page = self.new_button(open_select_Map_Page_Button(250,450,500,100,'Select Map',Colours.lightBlue,Colours.blue))

    def update(self):
        super().update()
        if Settings.changed_sound_effects or Settings.changed_display:
            self.change_sound_effect()
            Settings.changed_sound_effects = False

    def change_sound_effect(self):
        if self.sound_effects_Button.text == self.sound_effects_Button.name and not Settings.Sound_Effect:
            self.sound_effects_Button.change()
        elif self.sound_effects_Button.text == self.sound_effects_Button.alt_text and Settings.Sound_Effect:
            self.sound_effects_Button.change()



class Buy_Page(Page):
    def __init__(self,name,go_back=True):
        super().__init__(name,go_back)
        self.tower_Page = self.new_button(open_buy_Tower_Page_Button(250,300,500,100,'Tower',Colours.lightBlue,Colours.blue))
        self.map_Page = self.new_button(open_buy_Map_Page_Button(250,450,500,100,'Map',Colours.lightBlue,Colours.blue))


#Page will allow the player to buy a map
class Maps_Page(Page):
    def __init__(self,name,go_back=True):
        super().__init__(name,go_back)
        self.left_arrow = self.new_button(left_buy_Map_Button(0,400,200,100,'Left',Colours.lightBlue,Colours.blue))
        self.right_arrow = self.new_button(right_buy_Map_Button(800,400,200,100,'Right',Colours.lightBlue,Colours.blue))
        self.buy_Button = self.new_button(Buy_Map_Button(250,750,500,100,'Buy: '+str(Settings.current_Map.cost),Colours.lightBlue,Colours.blue,'Purchased'))
        self.map_Display = self.new_display(Display(300,300,False,pygame.transform.scale(Settings.current_Map.new_screen,(500,500))))

    def update(self):
        super().update()
        if Settings.changed_buy_map:
            self.update_display()
            self.update_button()
            Settings.changed_buy_map = False

    def update_display(self):
        self.displays.remove(self.map_Display)
        self.map_Display = self.new_display(Display(300,300,False,pygame.transform.scale(Settings.current_buy_Map.new_screen,(500,500))))

    def update_button(self):
        self.buttons.remove(self.buy_Button)
        self.buy_Button = self.new_button(Buy_Map_Button(250,750,500,100,'Buy: '+str(Settings.current_buy_Map.cost),Colours.lightBlue,Colours.blue,'Purchased'))
        self.is_Bought()

    def is_Bought(self):
        if Settings.current_buy_Map in Settings.maps and self.buy_Button.text == self.buy_Button.name:
            self.buy_Button.change()
        elif Settings.current_buy_Map not in Settings.maps and self.buy_Button.text == self.buy_Button.alt_text:
            self.buy_Button.change()


#the Towers Page will allow the player to view and buy new Towers
class Towers_Page(Page):
    #The __init__ function will define all of the unique features of the Towers_Page
    def __init__(self,name,go_back=True):
        super().__init__(name,go_back)
        self.left_arrow = self.new_button(left_Tower_Arrow(0,400,200,100,'Left',Colours.lightBlue,Colours.blue))
        self.right_arrow = self.new_button(right_Tower_Arrow(800,400,200,100,'Right',Colours.lightBlue,Colours.blue))
        self.buy_Button = self.new_button(Buy_Tower_Button(250,750,500,100,'Buy',Colours.lightBlue,Colours.blue,'Purchased'))
        self.tower_Display = self.new_display(Stat_Display(225,350,Settings.current_Tower))

    def update(self):
        super().update()
        if Settings.changed_tower:
            self.displays.remove(self.tower_Display)
            self.tower_Display = self.new_display(Stat_Display(225,350,Settings.current_Tower))
            Settings.changed_Tower = False
            self.is_Bought()

    def is_Bought(self):
        if Settings.current_Tower in Settings.towers and self.buy_Button.text == 'Buy':
            self.buy_Button.change()

        elif Settings.current_Tower not in Settings.towers and self.buy_Button.text == 'Purchased':
            self.buy_Button.change()




#Page will allow the player to select a map to use in the game
class Select_Map_Page(Page):
    def __init__(self,name,go_back=True):
        super().__init__(name,go_back)
        self.left_arrow = self.new_button(left_select_Map_Button(0,400,200,100,'Left',Colours.lightBlue,Colours.blue))
        self.right_arrow = self.new_button(right_select_Map_Button(800,400,200,100,'Right',Colours.lightBlue,Colours.blue))
        self.set_active_Button = self.new_button(Set_Active_Button(250,750,500,100,'Set Active',Colours.lightBlue,Colours.blue,'Active'))
        self.map_display = self.new_display(Display(300,300,False,pygame.transform.scale(Settings.current_Map.new_screen,(500,500))))


    def update(self):
        super().update()
        if Settings.changed_select_map:
            self.displays.remove(self.map_display)
            self.map_display = self.new_display(Display(300,300,False,pygame.transform.scale(Settings.current_select_Map.new_screen,(500,500))))
            Settings.changed_select_map = False
            self.is_Active()

    #Function will determine if the map being displayed is the active map or not and will change the text of the set active button
    def is_Active(self):
        if Settings.current_select_Map != Settings.active_Map and self.set_active_Button.text == 'Active':
            self.set_active_Button.change()
        elif Settings.current_select_Map == Settings.active_Map and self.set_active_Button.text == 'Set Active':
            self.set_active_Button.change()



