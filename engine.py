from os import system, name 
from random import randint

global_loot = {
    'fist' : {
        'name': 'fist',
        'class': 'weapon',
        'power': 24,
        'prot': 17,
        'distance': 0.5,
        'info': 'convenient to use when you have no weapons',
    },
    'prison key' : {
        'name': 'prison room key',
        'class': 'key',
        'info': 'key that opens your prison room you have been locked in',
    },
    'balders knight sword' : {
        'class': 'weapon',
        'name': 'balders knight weapon',
        'power': 75,
        'prot': 23,
        'distance': 0.8,
        'info': 'sword taken from balder undead knight'
    },
    'balders knight armor' : {
        'class': 'armor',
        'name': 'balders knight armor',
        'prot': 45,
        'info': 'armor taken from balder undead knight',
    },
    'wooden magic stick' : {
        'class': 'weapon',
        'name': 'wooden magic stick',
        'power': 100,
        'prot': 13,
        'distance': 3,
        'info': 'wooden stick which mostly use roving magicians'
    },
    "poor magician's dress" : {
        'class': 'armor',
        'name': "poor magician's dress",
        'prot': 21,
        'info': 'dress with sewn holes'
    },
    'underpants' : {
        'class': 'armor',
        'name': "underpants",
        'prot': 12,
        'info': "doesn't protect anything but the most important"
    },
    'broken sword':{
        'class' : 'weapon',
        'name'  : 'broken rusty sword',
        'prot'  : 9,
        'power' : 45,
        'distance' : 0.65,
        'info'  : 'broken undeads sword rusted by time'
    },
    'tower shield':{
        'class' : 'weapon',
        'name'  : 'tower shield',
        'prot'  : 43,
        'power' : 23,
        'distance' : 0.5,
        'info'  : 'black tower shield mostly used by undead soldiers'
    },
    'undead soldiers armor':{
        'class' : 'armor',
        'name'  : 'undead soldier`s armor',
        'prot'  : 40,
        'info'  : 'armor set taken from neutralized undead'
    },
    'astorian knights shield': {
        'class' : 'weapon',
        'name'  : 'tower shield',
        'prot'  : 43,
        'power' : 23,
        'distance' : 0.5,
        'info'  : 'black tower shield mostly used by undead soldiers'
    }
}
classes = [
    {
        'name'      : '',
        'class'     : 'knight',
        'info'      : 'very powerfull',
        'start-inv' : 'knight sword and armor',
        'health'    : 100,
        'power'     : 100,
        'luck'      : 0.8,
        'sword'     : global_loot['balders knight sword'],
        'armor'     : global_loot['balders knight armor'],
        'shield'    : global_loot['fist'],
        'inventory' : [
            global_loot['underpants'],
            global_loot['balders knight sword'],
            global_loot['balders knight armor'],
        ],  
    }, {
        'name'      : '',
        'class'     : 'magician',
        'info'      : 'long distance fight',
        'start-inv' : 'magic stick and dress',
        'health'    : 50,
        'power'     : 100,
        'luck'      : 1,
        'sword'     : global_loot['wooden magic stick'],
        'armor'     : global_loot["poor magician's dress"],
        'shield'    : global_loot['fist'],
        'inventory' : [
            global_loot['underpants'],
            global_loot['wooden magic stick'],
            global_loot["poor magician's dress"],
        ],  
    }, {
        'name'      : '',
        'class'     : 'poor',
        'info'      : 'ultra lucky',
        'start-inv' : 'nothing',
        'health'    : 120,
        'power'     : 100,
        'luck'      : 1.6,
        'sword'     : global_loot['fist'],
        'armor'     : global_loot['underpants'],
        'shield'    : global_loot['fist'],
        'inventory' : [
            global_loot['underpants'],
        ],  
    }
]

def hero_creator():
    clear()
    hero_obj = {}
    location_print('select your class')
    params = ['class', 'health', 'luck', 'info']
    length = [15, 10, 10, 35]
    table(params, length, classes)
    user_choice = input("\n" + " " * 83 + ">| ")
    if user_choice not in [str(index + 1) for index in range(len(classes))]:
        alert('wrong input')
        return hero_creator()

    hero_obj = classes[int(user_choice) - 1]
    hero_obj['init_heal'] = hero_obj['health']
    hero_obj['estus'] = None
    location_print('enter your name')
    hero_name = input("\n" + " " * 67 + ">| ")
    if len(hero_name) > 15:
        new_name = ''
        for i in range(13):
            new_name += hero_name[i]
        hero_name = new_name + '...'
    hero_obj['name'] = hero_name
    return hero_obj

# define console clear function 
def clear(): 

    # for windows 
    if name == 'nt': 
        system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        system('clear') 

def enter_to_continue():
    print(' ' * 66 + '-' * 42 + '\n' + " " * 76 + "press Enter to continue")
    input()
    clear() # clearing the console

def status(hero):
    health_bar = '÷ ' + '■ ' * (hero['health'] // 10) + '□ ' * ((hero['init_heal'] - hero['health']) // 10)
    if hero['health'] % 10 >= 5:
        health_bar = '■ ' + health_bar
    elif hero['health'] % 10 >= 1:
        health_bar = health_bar + '□ '
    #sword and armor
    shield = hero['shield']
    if hero['shield'] == global_loot['fist']:
        shield = hero['sword']
    tools = ' ⚔ ' + str(hero['sword']['power']) + ' ※ ' + str(hero['armor']['prot']) + ' 𝌆 ' + str(shield['prot'])
    if hero['estus'] != None:
        tools += ' ✱ ' + str(hero['estus'])
    print(' ' * 47 + '♝ ' + hero['name'] + '  ' + health_bar + ' ' * (76 - len(hero['name'] + health_bar + tools)) + tools)

def situation(text):
    print(' ' * 47 + '-' * 80 + '\n') #newline
    arr = text.split()
    line = ''
    for word in arr:
        if len(line + word) <= 76:
            line += word + " "
        else:
            print(" " * 45 + '|   ' + line + ' ' * (77 - len(line)) +'  |')
            line = word + " "
    print(" "*45 + '|   ' + line + ' ' * (77 - len(line)) +'  |')
    print('\n' + ' ' * 47 + '-' * 80)

def message(msg):
    clear()
    text = ''
    for char in msg:
        text += char + ' '
    print('\n' * 10)
    print(' ' * 47 + '-' * 80 + '\n') 
    line = " "*(38 - len(text) // 2) + text.upper() + " "*(38 - len(text) // 2 + len(text) % 2)
    print(" "*45 + '|   ' + line + ' ' * (77 - len(line)) +'  |')
    print('\n' + ' ' * 47 + '-' * 80)     
    enter_to_continue()

def location_print(name):
    long_name = ''
    for char in name:
        long_name += char + ' '
    print('\n' + " "*58 + "-------|  " + " "*(19 - len(long_name)//2) + long_name.upper() + " "*(19 - len(long_name)//2) + "  |------- \n")

def alert(message):
    clear()
    text = ''
    for char in message:   #making spaces between characters in sentence
        text += char + ' '
    print('\n' * 10)
    print(" "*58 + ">> !! >> " + "█" + " "*(19 - len(text)//2) + text.upper() + " "*(19 - len(text)//2) + "█" + " << !! << ")
    print(" "*68 + "_"*39)
    enter_to_continue()

def table(params, percentage, arr):  # ['name', 'info'], [25, 40], [{'name': 'prison room key', 'info': 'opens your prison room'}]
    line = ''
    left_space_amount = 62
    underline = "_"
    for i in range(len(percentage)):    # printing header line
        space = round(75 * percentage[i]/100)
        left_space_amount -= (space - len(params[i]))//2
        line += params[i].upper() + " " * (space - len(params[i])) + " | "
        underline += '_' * (space + 3)
    line = ' ' * (left_space_amount + 8) + "| " + line
    underline = ' ' * (left_space_amount + 8) + underline
    print(line + "\n" + underline + "\n")
    for index in range(len(arr)):     #printing body
        obj = arr[index]
        line = ' ' * left_space_amount + f"<| {index + 1} |> " + '| '
        for i in range(len(percentage)):
            param = params[i]
            space = round(75 * percentage[i]/100)
            line += str(obj[param]) + " " * (space - len(str(obj[param]))) + " | "
        print(line + f"<| { index + 1 } |>" +"\n" + underline + "\n")
