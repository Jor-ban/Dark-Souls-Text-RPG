from os import system, name 
from random import randint
from pics import victory

global_loot = {
    #all possible inventory objects dict
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
    'asylum arena key': {
        'name': 'asylum arena key',
        'class': 'key',
        'info': 'key which can be taken from asylum demon',
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
        'power': 30,
        'prot': 13,
        'distance': 2,
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
    # used to create a hero in newgame start
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

hero = {
    'name'      : 'Jordan',
    'class'     : 'knight',
    'info'      : 'very powerfull',
    'start-inv' : 'knight sword and armor',
    'health'    : 100,
    'init_heal' : 100,
    'estus'     : None,
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
}

enemies = {
    'room corridor': {}, 
    'asylum demon': { 
        'name': 'asylum demon',
        'health': 1,
        'init_heal' : 425,
    },
    'corridor archer': {
        'name': 'corridor archer',
        'health': 30,
        'init_heal' : 30,
    },
    'steel ball undead': {
        'name': 'corridor archer',
        'health': 50,
        'init_heal' : 50,
    }
}
opened_doors = []
alive_enemies = [el for el in enemies.keys()]
current_map = 'prison'
curr_location = None
prev_location = None
last_fire = 'prison room'

def enemy_rebirth():
    global hero, alive_enemies, enemies, last_fire
    clear()
    last_fire = curr_location
    if hero['estus']:
        hero['estus'] = 1
    hero['health'] = hero['init_heal']
    alive_enemies = [el for el in enemies.keys()]
    line = "Y O U   H A V E   T A K E N   A   R E S T"
    print('\n' * 10)
    print('__' * 87 + '\n')
    print(' ' * (87 - len(line) // 2) + line + '\n')
    line = 'ENEMIES RESURRECT AFTER TAKING REST'
    print(' ' * (87 - len(line) // 2) + line )
    print('__' * 87 + '\n')
    enter_to_continue()

def enemy_stat(enemy):
    name_low = enemy['name']
    name = ''
    for char in name_low:
        name += char + ' '

    print('\n' + " " * 68 + " " * (19 - len(name)//2) + name.upper())
    health_bar = '■' * int(42 * enemy['health'] / enemy['init_heal']) + ' ' * int(42 - 42 * enemy['health'] / enemy['init_heal'])
    print('\n' + " "*58 + "-------|" + health_bar.upper() + "|------- \n")

def boss_defeat():
    clear()
    print('\n' * 7)
    print(victory)
    enter_to_continue()

def drop(*items):
    """random drop after killing an enemy

    hero dict and items dicts which can be dropped

    {'name': 'broken sword', 'poss': 25}

    the less possibility the more chance to get the object
    """
    global hero
    for item in items:
        name = item['name']
        obj = global_loot[name]
        if obj in hero['inventory']:    # in case if the drop object is already in inventory
            continue
        possibility = item['poss']
        luck = hero['luck']
        if randint(0,100) * luck >= possibility:
            hero['inventory'].append(obj)
            message('you`ve got ' + name + '!')
    return hero

def move(enemy, poss, type):
    """enemy_obj, possibility, type(attack or dodge).

    possibility is here for poss. of taking damage.

    the less possib. the more chance to succeed."""
    global hero
    sword = hero['sword']
    num = randint(1,100) * hero['luck']
    if type == 'attack' or type == 'Attack':
        num = num * sword['distance']
        if num >= poss:
            num = int(num)
            enemy['health'] -= num
            return f"This attack was successfull, you have taken {num} from enemy's health"
        else:
            armor = hero['armor']
            damage = (100 - armor['prot']) / 100
            num = int(damage * num)
            hero['health'] -= num
            return f"That wasn't a successfull move, you are taking {num} amounts of dammage"
    else:
        shield = hero['shield']
        if shield == global_loot['fist']:
            # hero can protect itself with weapon instad of fist
            shield = sword
            
        num = num * shield['prot'] / 50
        if num >= poss:
            num = num * sword['distance']
            num = int(num)
            enemy['health'] -= num
            return f"your dodge was successfull, you have taken {num} from enemy's health"
        else:
            num = num * (100 - shield['prot']) / 100
            num = int(num)
            hero['health'] -= num
            return f"You couldn't successfully dodge, you are taking {num} amounts of dammage"

def hero_creator():
    global hero
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
    hero = hero_obj

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

def show_status():
    global hero
    # one line display of hero status
    health_bar = '■ ' * int(hero['health'] // 10) + '□ ' * int((hero['init_heal'] - hero['health']) // 10)
    if hero['health'] % 10 >= 5:
        health_bar = '■ ' + health_bar
    elif hero['health'] % 10 >=1:
        health_bar = health_bar + '□ '

    health_bar =  '÷ ' + health_bar
    #sword and armor
    shield = hero['shield']
    if hero['shield'] == global_loot['fist']:
        shield = hero['sword']
    tools = ' ⚔ ' + str(hero['sword']['power']) + ' ※ ' + str(hero['armor']['prot']) + ' 𝌆 ' + str(shield['prot'])
    if hero['estus'] != None:
        tools += ' ✱ ' + str(hero['estus'])
    print(' ' * 47 + '♝ ' + hero['name'] + '  ' + health_bar + ' ' * (76 - len(hero['name'] + health_bar + tools)) + tools)

def situation(text):
    print(' ' * 47 + '-' * 80 + '\n') # newline
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

def table(params, percentage, arr):  
    """ params = ['name', 'info'], 
    
    params length percentage = [25, 40], 
    
    actual array = [{'name': 'prison room key', 'info': 'opens your prison room'}] """
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
