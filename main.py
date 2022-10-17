import yaml
from main_classes import Chapter
from main_classes import Gameloop
from main_classes import Intro
from Character.create_character import load_player 

chapter = "1"
game_on = True

yml_file_path = "Data/data.yml"
with open(yml_file_path, 'r') as y:
    data = yaml.load(y.read(), Loader=yaml.FullLoader)

def getChapter(chap):
    t = data[chap]["text"]
    o = data[chap]["options"]
    return Chapter(t, o)

intro = Intro()
player = load_player(intro.save_file)
print(player.name)
print(player.ability)

def main():
    global chapter
    current_chap = getChapter(chapter)
    game = Gameloop(current_chap)
    game.game_main()
    chapter = game.direction

while game_on == True:
    main()
    



