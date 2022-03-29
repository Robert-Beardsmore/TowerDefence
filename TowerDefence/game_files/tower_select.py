import pygame
pygame.font.init()

from .colours import Colours

from .settings import Settings

from .towers import *

from .active_towers import Active_Tower

#Tower select
class Tower_Select:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x,y,width,height)
        self.surface = self.new_surface()
        self.towers = Settings.towers #change this to player account towers - change made
        self.squares = self.make_Squares()
        self.movementY = 0
        self.scroll_speed = 10

    #Returns the image of the tower select
    def new_surface(self):
        surface = pygame.Surface((self.width,self.height))
        surface.fill(Colours.brown)
        return surface

    #Makes a sqaure for each tower
    def make_Squares(self):
        squares = []
        i=0
        for tower in self.towers:
            #Position of each square on tower select made
            squares.append(Square(800,(170*i),tower))
            i+=1
        return squares

    #Renders all squares to the screen
    def draw_Sqaures(self):
        for square in self.squares:
            square.draw(self.movementY)

    #Called when left mouse button is lifted and there was a tower selected
    def place_Tower(self):
        x,y= pygame.mouse.get_pos()
        if not 180<=y<=900 or not 0<=x<=720: #Condition to keep mouse within map
            return
        x //=(Settings.width) #Used to gain positon of mouse in map array
        y = (y-180)//Settings.height #Used ot gain posiotn of mouse in map array, takes away distance of the map from the 0 y coord
        if Settings.active_Map.map_grid[y][x] == '2': #Two being a path tile
            #Insert If statement checking playing money
            if Settings.selected_Tower.deploy_cost <=Settings.money: #Condition statement used to determine if player has enough money to place tower
                Settings.money -= Settings.selected_Tower.deploy_cost #Removes cost of tower from player money
                Settings.active_Map.map_grid[y][x] = '1' #Prevents new towers from being placed onto of each other, 1 is the value of a path tile
                new_tower = Active_Tower(x,y,Settings.selected_Tower)
                #Add new tower to list of active towers, tower now spawned
                Settings.active_Towers.append(new_tower)
                Settings.active_Tower = new_tower #Sets tower just placed down to active tower
                Settings.selected_Tower = True





    def events(self,event):
        #Left click checks for tower collision
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = pygame.mouse.get_pos()
            for square in self.squares: square.collision(x,y-self.movementY)

        #Left mouse button let go causes selected tower to be None
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            #If statement used so value only changed if not None already
            if Settings.selected_Tower:
                self.place_Tower()
                Settings.selected_Tower = None
                #Place Tower

        #Right click returns tower position to normal
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            self.movementY = 0

        #Mousewheel scrolls towers
        if event.type == pygame.MOUSEWHEEL:
                    self.movementY += int(event.y*self.scroll_speed)

    def update(self):
        pass

    def draw_tower(self):
        pos = pygame.mouse.get_pos()
        surface = pygame.Surface(Settings.screen.get_size(), pygame.SRCALPHA)#Makes transparent surface
        pygame.draw.circle(surface,Colours.grey,(pos[0],pos[1]),Settings.selected_Tower.radius) #Draws circle to new surface
        surface.set_alpha(128) #Makes ircle transparent
        Settings.screen.blit(surface,(0,0)) #Draws surface to screen
        Settings.screen.blit(Settings.selected_Tower.img,(pos[0]-30,pos[1]-30)) #Draws tower to screen centred on mouse


    def draw(self):
        Settings.screen.blit(self.surface,self.rect)
        self.draw_Sqaures()
        #Add checking player money when game linked
        #Draws tower on player mouse position
        if Settings.selected_Tower:
            self.draw_tower()



#Makes a single square representing a tower
class Square:
    #Font is the same across all class instances
    font = pygame.font.Font(None,64)
    def __init__(self,x,y,tower):
        self.x = x
        self.y = y
        self.tower = tower
        #Tower img size changed to make it easier to see
        self.tower.new_img = pygame.transform.scale2x(self.tower.img)
        self.rect = pygame.Rect(self.x,self.y,self.tower.new_img.get_width(),self.tower.new_img.get_height())
        self.text_sur,self.text_rec = self.make_text()

    #Returns cost of tower as text rendered underneath tower img
    def make_text(self):
        surface= self.font.render(str(self.tower.deploy_cost),True,Colours.black)
        rect = surface.get_rect()
        #centres the text to the image
        rect.midtop= self.rect.midbottom
        return surface,rect

    def collision(self,x ,y):
        #Place can only drag tower if they have enough money
        if self.rect.collidepoint((x,y)) and Settings.money >= self.tower.deploy_cost:
            Settings.selected_Tower = self.tower

    #Draws tower img and tower text
    def draw(self,Y):
        Settings.screen.blit(self.tower.new_img,(self.x,self.y+Y))
        Settings.screen.blit(self.text_sur,(self.text_rec.x,self.text_rec.y+Y))

