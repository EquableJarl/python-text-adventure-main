import yaml
from main_classes import Chapter as Chapter
from main_classes import Gameloop as Gameloop
from main_classes import intro as intro

chapter = "1"
game_on = True

yml_file_path = "Data/data.yml"
with open(yml_file_path, 'r') as y:
    data = yaml.load(y.read(), Loader=yaml.FullLoader)


def getChapter(chap):
    t = data[chap]["text"]
    o = data[chap]["options"]
    return Chapter(t, o)

# TODO fix main remove gameloop and chapter class
# TODO add start screen, create character, load character
# TODO create a function for the main class loop


def main():
    global chapter
    current_chap = getChapter(chapter)
    game = Gameloop(current_chap)
    game.game_main()
    chapter = game.direction


save = intro()
print(save.save_file)
