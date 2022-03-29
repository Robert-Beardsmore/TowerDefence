#Player Accounts moudle: Used to store the logic for making, saving, and loading player accounts
#pickel module imported: Used for storing dictionary in file
import pickle

from .player_account import Player_Account

from .settings import Settings

from .towers import Towers

from .maps import Maps


'''class Player_Accounts:
    Accounts = {"Username": Player_Account("Username","Password")}

    @staticmethod
    def Save_Accounts():
        Player_Accounts.save_data()
        with open('game_files\data.txt','wb') as data_file:
            pickle.dump(Player_Accounts.Accounts,data_file)

    @staticmethod
    def Load_Accounts():
        try'''


#Player_Account class made: Used for saving and loading player accounts.
class Player_Accounts:
    Accounts = {'Username':Player_Account('Username','Password')}

    #Static method of Save_Accounts is made: Uses pickle module to dump Accounts into file
    @staticmethod
    def Save_Accounts():
        Player_Accounts.save_data()
        with open('game_files\data.txt','wb') as data_file:
            pickle.dump(Player_Accounts.Accounts,data_file)

    #Static method of Load_Accounts is made: Uses pickle module to load Accounts from file
    @staticmethod
    def Load_Accounts():
        try:
            data_file = open('game_files\data.txt','rb')
            Player_Accounts.Accounts = pickle.load(data_file)
            data_file.close()
        except EOFError:
            with open('game_files\data.txt','wb') as data_file:
                pickle.dump(Player_Accounts.Accounts,data_file)

    #Add Accounts function is made: Adds new account to accounts dictionary with username as key
    def Add_Account(username,password):
        new_Player = Player_Account(username,password)
        Player_Accounts.Accounts[username] = new_Player

    #Load_Account_Data function is made: Used to return the account linked to the username
    def Load_Account_Data(self,username):
        return Player_Accounts.Accounts[username]

    #check_password function is made: Used to return True if password matches the password of the account linked to the username
    def check_password(username,password):
        Player_Accounts.Load_Accounts()
        if Player_Accounts.Accounts[username].password == password:
            return True
        else:
            return False

    #check_username function is made: Used to return True if username is linked to player account
    def check_username(username):
        Player_Accounts.Load_Accounts()
        if username in Player_Accounts.Accounts:
            return True
        else:
            return False

    #Username and password would be text typed in textbox, function used to set data
    @staticmethod
    def set_data():
        Settings.Account_System_state = False
        Settings.Main_Menu_state = True
        Player_Accounts.unconvert_Maps()
        Player_Accounts.unconvert_Towers()
        Player_Accounts.set_maps()
        Settings.Money = Settings.Game_Data.Money
        Settings.Level = Settings.Game_Data.Level
        Settings.Sound_Effect = Settings.Game_Data.sound_effects
        Settings.changed_display = True


    @staticmethod
    def set_maps():
        Settings.current_select_Map = Settings.maps[0]
        Settings.active_Map = Settings.current_select_Map
        Settings.select_map_total = len(Settings.maps)
        Settings.current_buy_Map = Maps.maps[0]

    @staticmethod
    def save_data():
        Player_Accounts.Accounts[Settings.username].maps = Player_Accounts.convert_Maps()
        Player_Accounts.Accounts[Settings.username].towers = Player_Accounts.convert_Towers()
        Player_Accounts.Accounts[Settings.username].Money = Settings.Money
        Player_Accounts.Accounts[Settings.username].Level = Settings.Level
        Player_Accounts.Accounts[Settings.username].sound_effects = Settings.Sound_Effect

    #function returns the indexes of the towers that the player has unlocked
    @staticmethod
    def convert_Towers():
        temp = []
        for tower in Settings.towers: temp.append(Towers.towers.index(tower))
        return temp

    #Fucntion returns the indexes of the tmaps that the player has unlocked
    @staticmethod
    def convert_Maps():
        temp = []
        for Map in Settings.maps: temp.append(Maps.maps.index(Map))
        return temp

    #Function takes the indexes in the player accounts towers and adds the actual towers to settings
    @staticmethod
    def unconvert_Towers():
        for index in Settings.Game_Data.towers: Settings.towers.append(Towers.towers[index])


    #Player convert indexes in the player accounts into maps
    @staticmethod
    def unconvert_Maps():
        for index in Settings.Game_Data.maps: Settings.maps.append(Maps.maps[index])




