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
