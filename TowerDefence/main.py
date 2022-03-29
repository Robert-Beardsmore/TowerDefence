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


'''
Issue Tracker
- setting a map to active and then looking at another map not changing button fixed by changing reference in button class for which button is the curren map
- selected map not being map used in game
- buy maps and towers page need to be linked now with player account
- buying a map changes text to prurchased but then the text does not change - needed .text in the is_Bought function
- account system not saving towers purchases - hvn't added additional code to save and quit button yet
- cannot picke pygame objects - added convert_Tower and convert_Maps function to Player_Accounts to store index of tower and maps bought
- an unconvert maps and towers function is now needed
- inital opening of buy towers page not displaying the bought tower as purchased - called is_Bought function when button pressed to open page
- level and money display on the main menu not updating - changed buttons to update display also going to change the level and money display to be on the main menu and not the individual page
    - changed that by adding the level and money display on the main menu page and then creating a bool in settings that when changed would cause a change to happen - this solution works
- added display message to buying towers
- sound effects don't save as off - fixed
- fix setting the active map - done
- just fix the saving system again and it should work - fixed, problem in set_data
- is active for select map page not being called when page first opened - mixing up select map and buy map and not calling set_data function
- towers not appearing on tower select  -because __init__ function called when game first started so no values for the towers
- made call to game class in settings so new game can be made when the play button is pressed each time game doesn't reset when finished
- game still there when returnning to main menu - not reseting data also need to reset map grid
- added the make reward function to the rounds class to add exp and money to the player
- need to fix sell and upgrade button the cost isn't appearing on the butotn when tower first pressed
- issue with new maps bought not appearing in select tower menu and issue with the ordering used to buy a tower
- enemies spawn in wrong place - fixed with active map
- can start game with no active map selected - added condition in open game button
- issue with order of buying maps when going to and from the screen - fixed by setting the current buy map in the player accounts class
- issue with trying to close window when in the game - fixed by changing the game state to main menu
- issue with map prices appearing as 0 - button not updating - problem caused by tempory changes to update function is pages, this change has been reversed problem solved
- current select map being used for the active map - changed this to current map this also solved enemy spawning position
- added another variable to the map that will store what round the game ends on
- red square not appearing on enemies - they are now but look out for this problem
- upgrade and sell button not updating - fixed by changing update button
- in game show message at the end of each round saying 'press space to start round'
- wierd index out of range error when spawning enemies run and hide enemies - no run and hide enemies so index error occured
- issue creating a new account very big issue - issue cause by in create account it immediatly saves and then loads the account even though no data has been set so it doesn't work
- red square not appearing over enemies all the time
-changed times that the enemies spawned and the health to make the game more balanced
-enemy spawn rate does not go back to normal after each round - look in game_init()

'''