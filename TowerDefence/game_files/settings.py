#Settings module: Used to store settings needed for game to work
#pygame imported: Used to make screen and clock
import pygame

import sys



#Settings class created
class Settings:

    #General Settings
    Screen_Width = 1000
    Screen_Height = 900
    Screen_Name = 'Tower Defence Game'
    Framerate = 30
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((Screen_Width,Screen_Height))
    height = 60 #Stores the height of a tile
    width = 60 #Stores width of a tile
    tile = 12 #Stores the tiles so grid is 12 x 12

    #Stores the maps that the player has access too
    maps = []
    #Stores the towers that the player has access too
    towers = []
    #Stores the Money that the player has
    Money = 0
    #Stores the Level that the player is
    Level = 0
    #Determines if sound effects should play
    Sound_Effect = True

    changed_display = False

    Account_System_state = True
    Main_Menu_state = False
    Game_state = False
    Pause_state = False
    end_Game_state = False

    username = ''
    password = ''

    Game_Data = None #
    Speed_Up = False #Determines if game should be sped up

    page_Stack = [] #Used to access previous pages
    page_Dict = {} #Used to access the differnet pages
    current_Page = None #Used to store the current page
    current_Map = None #Used to store the current map being displayed on the buy map page
    current_Tower = None #Stores which tower is currently being displayed on the buy towers page

    #Stores the map being displayed on the buy map page
    current_buy_Map = None

    #Stores the map being displayed on the select map page
    current_select_Map = None

    auto_Start = False #Used to determine if next round should start automatically

    selected_Tower = None #Used to store tower currently selected from tower select
    active_Towers = [] #Used to store all towers placed on the map
    active_Tower = None #Stores tower currently selected on the map
    active_Map = None #Stores the map that has been selected to use in the game

    #Stores the index of the current tower being displayed
    tower_index = 0
    #Stores the index of the map being displayed on the buy maps page
    buy_map_index = 0
    #Stores the index of teh map being displayed on the select maps page
    select_map_index = 0

    #Stores how many maps the player has unlocked
    select_map_total = 0

    #Bool changed if the current tower has been changed
    changed_tower = False
    changed_buy_map = False
    changed_select_map = False
    changed_sound_effects = False


    active_Enemies = [] #Stores all enemies currently on the map
    current_enemy = None

    #Stores all the projectiles being fired on the map
    projectiles = []

    #temporary variable
    money = 75
    health = 10 #Stores the amount of health a player has left

    game_round = 1 #Current round number

    start_round = False
    won = None

    #Determines if a tower has been selected
    selected_Tower = False


    game = None
    change_to_game = False


    def Quit():
        pygame.quit()
        sys.exit()

    @staticmethod
    def grid_to_screen(x,y):
        new_x = x * Settings.width #positon of grid
        new_y = (y*Settings.height)+180 #positon of map
        return int(new_x),int(new_y)

    @staticmethod
    def screen_to_grid(x,y):
        new_x = x // Settings.width
        new_y = (y-180)//Settings.height
        return int(new_x),int(new_y)

    #Function added so when player health is less than or equal to 0 the game stops
    @staticmethod
    def take_damge(damage):
        Settings.health -= damage

        if Settings.health <=0:
            Settings.won = False
            Settings.end_Game_state = True
            #Settings.Pause_state = False
            #Settings.Game_state =False

    @staticmethod
    def add_Experience():
        Settings.Level +=1






