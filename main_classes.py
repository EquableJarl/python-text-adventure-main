from Character.new_character import New_Character as New_Character
import yaml

with open(r'Character/character_config.yml') as file:
    creation_stats = yaml.load(file, Loader=yaml.FullLoader)


class Chapter:
    def __init__(self, text, options, player):
        self.text = text
        self.option = options
        self.op_text = self.get_options("text")
        self.op_dest = self.get_options("direction")

    def get_options(self, value):
        options = []
        for ops in self.option:
            options.append(self.option[ops][value])
        return options


class Gameloop:
    def __init__(self, chapter):
        self.chapter = chapter
        self.choice = ""
        self.direction = ""

    def game_main(self):
        print(self.chapter.text)
        for count, opt in enumerate(self.chapter.op_text):
            print(str(count + 1) + ") " + opt)
        while self.choice == "":
            self.choice_and_check()
        self.get_direction()

    def choice_and_check(self):
        choice = input("What would you like to do now ? : ")
        try:
            if int(choice) in range(1, len(self.chapter.op_text) + 1):
                self.choice = choice
            else:
                print("That wasn't an option, please try again! ")
        except:
            print("Thats not even a number!, please try again")

    def get_direction(self):
        self.direction = self.chapter.op_dest[int(self.choice) - 1]


class intro():
    def __init__(self):
        self.choice = ""
        self.print_intro()
        # self.run_selection()

    def print_intro(self):
        print("""
        Welcome to the game!
    
        1) New Game
        2) Load Game
    
        """)
        while self.choice == "":
            self.check_and_choice()

    def check_and_choice(self):
        choice = input("Please make your selection : ")
        if choice == "1" or choice == "2":
            self.choice = choice
        else:
            print("That was not a valid selection!")

    def run_selection(self):
        if self.choice == "1":
            player = New_Character(creation_stats)
            player.export_to_ymal
        else:
            pass


# intro()
