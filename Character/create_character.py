import yaml
import os


class Player:
    def __init__(self):
        self.name = ""
        self.profession = ""
        self.checklist = []
        # self.god = ""
        # self.rank = ""
        # self.defence = ""
        self.ability = []
        # self.stamina = {}
        self.possessions = []
        # self.money = ""


class Player_Factory:
    def __init__(self, player, load):
        self.player = player
        self.load = load
        self.load_player()

    def load_player(self):
        self.player.name = self.load["Name"]
        self.player.profession = self.load["Profession"]
        for a in self.load["Abilities"]:
            self.player.ability.append(a)


def load_player(save):
    print("from the load_player function - Loading player " + save)
    p = Player()
    os.chdir("Save")
    with open(save, "r") as file:
        load = yaml.load(file, Loader=yaml.FullLoader)
    Player_Factory(p, load)
    return p

