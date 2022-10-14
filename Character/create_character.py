import yaml


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


def load_player():
    p = Player()
    with open(r'test.yml') as file:
        load = yaml.load(file, Loader=yaml.FullLoader)
    Player_Factory(p, load)
    return p


my_player = load_player()

print(my_player.name + my_player.profession + str(my_player.ability))
