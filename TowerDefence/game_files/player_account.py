class Player_Account:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.Level = 0
        self.Money = 0
        self.towers = [0]
        self.maps =  [0]
        self.sound_effects = True

