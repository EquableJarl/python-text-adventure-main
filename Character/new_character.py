import yaml
import datetime

with open(r'Character/character_config.yml') as file:
    creation_stats = yaml.load(file, Loader=yaml.FullLoader)


class New_Character:
    def __init__(self, config):
        self.file = file
        self.config = config
        self.name = self.get_name()
        self.profession = ""
        self.do_professions()
        self.abilities = []
        self.set_abilities()
        self.save_file = ""

    def get_name(self):
        name = input("What is your name?")
        return name

    def describe_professions(self):
        for count, p in enumerate(self.config["professions"]):
            print(p)
            print("_______________")
            print("***************")
            for count, value in enumerate(self.config["professions"][p]):
                print(self.config["professions_key"]
                      [count] + " = " + str(value))
            print("")

    def get_profession_selection(self):
        choice = input("What profession would you like to chose? : ")
        professions = []
        for p in self.config["professions"]:
            professions.append(p.upper())
        if choice.upper() in professions:
            self.profession = choice
        else:
            print("Thats not a valid choice, please try again.")

    def do_professions(self):
        self.describe_professions()
        while self.profession == "":
            self.get_profession_selection()

    def set_abilities(self):
        for a in self.config["professions"][self.profession]:
            self.abilities.append(a)

    def save_file_name(self):
        dt = datetime.datetime.now()
        suffix = dt.strftime("%d%m%y%H%M%S")
        return self.name + "-" + suffix + ".yml"

    def export_to_ymal(self):
        data = {"Name": self.name,
                "Profession": self.profession,
                "Abilities": self.abilities}
        file_name = self.save_file_name()
        self.save_file = file_name
        with open("Save/" + file_name, 'w') as file:
            yaml.dump(data, file)


# test = New_Character(creation_stats)
# print(test.name)
# print(test.profession)
# print(test.abilities)
# test.export_to_ymal()
