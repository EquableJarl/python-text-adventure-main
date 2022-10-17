from Character.new_character import New_Character as New_Character
import yaml
import os

with open(r'Character/character_config.yml') as file:
    creation_stats = yaml.load(file, Loader=yaml.FullLoader)


class Chapter:
    def __init__(self, text, options):
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


class Get_Save():
    # TODO list the saves and have the user select, also have a call that passes direct to the factory for new charachers
    def __init__(self):
        self.save_list = os.listdir("Save")
        self.choice = ""
        self.numbers = []
        self.get_and_list_saves()
        self.choice_loop()

    def get_and_list_saves(self):
        for index, save in enumerate(self.save_list):
            print(str(index + 1) + ") " + save)
            self.numbers.append(str(index + 1))
    
    def choice_loop(self):
        while self.choice == "":
            self.choice_and_check()

    def choice_and_check(self):
        choice = input("Please make your selection : ")
        if choice in self.numbers:
            self.choice = self.save_list[int(choice) - 1]
        else :
            print("This is not a valid option")

class Intro():
    def __init__(self):
        self.choice = ""
        self.save_file = ""
        self.print_intro()
        self.run_selection()


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
            player.export_to_ymal()
            self.save_file = player.save_file
        elif self.choice == "2":
            get_save = Get_Save()
            self.save_file = get_save.choice
    

