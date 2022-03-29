import pygame
import csv
from .settings import Settings
from .colours import Colours
from .player_account import Player_Account

class Maps:
    maps = []
    total = 0
    width = 12
    height = 12
    colours = {
        1: (133, 79, 43),#Brown - Path
        2: (112, 178, 55) #Green - Tower place
    }
    def __init__(self,map_file,cost,start,end):
        self.map_file = map_file #Stores csv file for map
        self.cost = cost #Stores the cost to buy map
        self.new_screen = self.make_screen() #Makes map image
        self.map_grid = self.make_array() #Makes map array of valid and invalid spaces
        self.map_grid_screen = self.draw_map_grid() #Makes valid and invalid space view
        self.path_grid = [row[:] for row in self.map_grid]
        self.map_rect = self.new_screen.get_rect()
        self.start = start
        self.end = end
        Maps.maps.append(self)
        Maps.total +=1

    #Takes the csv file attribute and uses it to generate map
    def make_screen(self):
        #This function makes a new screen for the map and returns it by iterating through the csv file and drawing a sqaure to the screen with the colour and position that links to the file
        new_screen = pygame.Surface(Settings.screen.get_size(),pygame.SRCALPHA)
        with open(self.map_file) as file:
            reader = csv.reader(file)
            X = 0
            Y = 0
            for row in reader:
                for column in row:
                    pygame.draw.rect(new_screen,Maps.colours[int(column)],(X * 60, Y * 60,60,60))
                    X +=1
                Y += 1
                X = 0
        return new_screen

    #Reads csv file into list
    def make_array(self):
        grid = list(csv.reader(open(self.map_file)))
        for row in grid:
            for value in row:
                if value == '1':
                    value = False
                else:
                    value = True
        return grid



    #Creates the transparent surface of valid and invalid spaces
    def draw_map_grid(self):
        #Local variable created for easier access
        new_screen = pygame.Surface(Settings.screen.get_size())
        #iterates through 2d array of Bools
        for y in range(len(self.map_grid)):
            for x in range(len(self.map_grid[y])):
                if self.map_grid[y][x]:
                    pygame.draw.rect(new_screen,Colours.green,(x * 60, y * 60,60,60),1)
                else:
                    pygame.draw.rect(new_screen,Colours.red,(x * 60, y * 60,60,60),1)
        #Makes screen transparent
        new_screen.set_alpha(128)
        #Returns new_screen
        return new_screen

    #Renders map to screen and if a tower is being selected draws transparent screen
    def draw(self,x=0,y=0):
        Settings.screen.blit(self.new_screen,(x,y))
        #Draws grid view of map
        if Settings.selected_Tower:
            Settings.screen.blit(self.map_grid_screen,(x,y))



#rgb(133, 79, 43) brown
#rgb(112, 178, 55) green

map_1 = 'game_files\map_files\map_1.csv'
map_2 = 'game_files\map_files\map_2.csv'
map_3 = 'game_files\map_files\map_3.csv'
map_4 = 'game_files\map_files\map_4.csv'
map_5 = 'game_files\map_files\map_5.csv'
#map_file, cost,  start position, end round
new_map = Maps(map_1,0,(5,1),10)
new_map = Maps(map_2,300,(1,1),50)
new_map = Maps(map_3,1000,(12,2),60)
new_map = Maps(map_4,2000,(1,6),100)
new_map = Maps(map_5,50,(1,1),50)
Settings.current_Map = Maps.maps[0]
