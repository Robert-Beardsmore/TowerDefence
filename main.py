import pygame

from game_files.settings import Settings

from game_files.account_system import Account_System

from game_files.main_menu import Main_Menu


account_System = Account_System()
main_menu = Main_Menu()
pygame.display.set_caption('MyTowerDefenceGame')

while True:
    Settings.clock.tick(Settings.Framerate)
    if Settings.Game_state:
        Settings.game.run()

    elif Settings.Main_Menu_state:
        main_menu.run()

    elif Settings.Account_System_state:
        account_System.run()
