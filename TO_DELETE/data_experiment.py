import json

json_file_path = "data.json"

game_on = True
current_chapter = "1"
inventory = []
checks = {"draw" : "False"}

with open(json_file_path, 'r') as j:
     data = json.loads(j.read())

def choice_and_check(chapter):
    choice = input("Please make your selection : ")
    if choice in data[chapter]["options"]:
        return choice
    else :
        print("That wasn't a valid choice...")
        return

#This function pick the correct code for the extra option 
def extra_ops(funk, value):
    if funk == "inventory_add":
        inventory.append(value)
    elif funk == "check_list":
        x = value.split("-")
        checks[x[0]] = x[1]


def change_chapter(chapter, choice):
    if data[chapter]["options"][choice]["direction"] == "check":
        print(data[chapter]["options"][choice]["check"]["value"])
        current_value = checks[data[chapter]["options"][choice]["check"]["value"]]
        direction = data[chapter]["options"][choice]["check"][current_value]
        return direction
    else : 
        return data[chapter]["options"][choice]["direction"]



def print_text(chapter):
    global current_chapter
    print(data[chapter]["text"])
    for ops in data[chapter]["options"]:
        if ops != "extra_option":
            print(ops + ") " + data[chapter]["options"][ops]["text"]) 
    choice = choice_and_check(chapter)
    if choice != None:
        if "extra_option" in data[chapter]["options"]:
            key_list = list(data[chapter]["options"]["extra_option"])
            for index, value in enumerate(data[chapter]["options"]["extra_option"]):
                extra_ops(key_list[index], data[chapter]["options"]["extra_option"][value])
            print(inventory)
        current_chapter = change_chapter(chapter, choice)


while game_on == True:
    print_text(current_chapter)





