from engine import *
from pics import *

#locations functions
def death():
    global curr_location, hero, last_fire
    clear()
    print('\n' * 7)
    print(you_died)
    enter_to_continue()
    curr_location = last_fire
    return load_location()

def set_location(loc):
    global curr_location, prev_location
    if loc != curr_location:
        prev_location = curr_location
        curr_location = loc
    location_print(loc)   

def load_location():
    clear()
    if curr_location == 'prison room':
        return prison_room()
    elif curr_location == 'room corridor':
        return room_corridor()
    elif curr_location == 'central fire':
        return central_fire()
    elif curr_location == 'central arena':
        return central_arena()
    elif curr_location == 'side corridor':
        return side_corridor()
    elif curr_location == 'second floor':
        return second_floor()
    elif curr_location == 'third floor':
        return third_floor()
    else:
        alert("no games found")

def take_rest():
    global alive_enemies, enemies, curr_location, last_fire
    alive_enemies = [el for el in enemies.keys()]
    curr_location = last_fire
    enemy_rebirth()

def drink_estus():
    global hero
    if not hero['estus']:
        message('You have no estus left')
        return 0
    init = hero['init_heal']
    if hero['health'] + 40 < init:
        hero['health'] += 40
    else:
        hero['health'] = init

    hero['estus'] -= 1

def undead_archer_fight(location, next_location):
    global enemies, hero, curr_location
    archer = enemies[location]
    text = ''
    while archer['health'] > 0:
        if hero['health'] <= 0:
            return death()
        clear()
        show_status()
        enemy_stat(archer)

        if text:
            situation(text)
        options = [
            'Rush the enemy',
            'Try to dodge',
            'Get back',
            'Escape',
            'Open inventory'
        ]

        if global_loot['astorian knights shield'] not in hero['inventory'] and curr_location == 'side corridor':
            # if hero haven't taken shield
            options.append('Look to side prison-room')
        if hero['estus']:
            #if hero returned after taking estus
            options.append('Drink estus')

        chs = output(options)
        if chs == 1:
            text = move(archer, 15, 'attack')
        elif chs == 2:
            text = move(archer, 20, 'dodge')
        elif chs == 3:
            return load_location()
        elif chs == 4:
            curr_location = next_location
            return load_location()
        elif chs == 5:
            alert('TODO')
        elif chs == 6 and global_loot['astorian knights shield'] not in hero['inventory']:
            hero = drop({'name': 'astorian knights shield', 'poss': 0})
        elif (chs == 6 and hero['estus']) or (chs == 7 and hero['estus']):
            drink_estus()

    alive_enemies.remove(location)
    hero = drop(
        {'name': 'broken sword', 'poss': 15}, 
        {'name': 'undead soldiers armor', 'poss': 20}, 
        #{'name': 'tower shield', 'poss': 12}
    )
    archer['health'] = archer['init_heal']
    message('You have eliminated enemy')

def undead_swordsman_fight(location, next_location):
    global enemies, hero, curr_location
    swordsman = enemies[location]
    text = ''
    while swordsman['health'] > 0:
        if hero['health'] <= 0:
            return death()
        clear()
        show_status()
        enemy_stat(swordsman)

        if text:
            situation(text)
        options = [
            'Rush the enemy',
            'Try to dodge',
            'Get back',
            'Escape',
            'Open inventory'
        ]

        if hero['estus']:
            #if hero returned after taking estus
            options.append('Drink estus')

        chs = output(options)
        if chs == 1:
            text = move(swordsman, 15, 'attack')
        elif chs == 2:
            text = move(swordsman, 20, 'dodge')
        elif chs == 3:
            return load_location()
        elif chs == 4:
            curr_location = next_location
            return load_location()
        elif chs == 5:
            alert('TODO')
        elif chs == 6 and hero['estus']:
            drink_estus()
        else:
            alert('wrong input')
            return undead_swordsman_fight()

    alive_enemies.remove(location)
    hero = drop(
        {'name': 'broken sword', 'poss': 15}, 
        {'name': 'undead soldiers armor', 'poss': 20}, 
        {'name': 'tower shield', 'poss': 12}
    )
    swordsman['health'] = swordsman['init_heal']
    message('You have eliminated enemy')   

def asydemon_fight():
    global enemies
    boss = enemies['asylum demon']
    text = ''
    while boss['health'] > 0:
        if hero['health'] <= 0:
            return death()
        clear()
        show_status()
        enemy_stat(boss)  #show status

        if text:
            situation(text)

        options = [
            'Attack the demon',
            'Try to dodge',
            'Escape to side door',
            'Open backside of central doors'
        ]
        if hero['estus']:
            options.append('Drink estus')

        chs = output(options)
        if chs == 1:
            text = move(boss, 40, 'attack')
        elif chs == 2:
            text = move(boss, 25, 'dodge')
        elif chs == 3:
            return side_corridor()
        elif chs == 4:
            message('door is closed')
        elif hero['estus'] and chs == 5:
            alert('TODO')

    boss_defeat()
    key = global_loot['asylum arena key']
    hero['inventory'].append(key)
    message('you`ve got ' + key['name'] + '!')
    enemies['asylum demon'] = None
    alive_enemies.remove('asylum demon')
    return central_arena()

def third_floor():
    pass

def second_floor():
    global curr_location, hero
    text = ''
    while True:
        clear()
        show_status()
        set_location('second floor')
        if text:
            situation(text)
        options = [
            'Go upper',
            'Go down by stairs',
            'Back to side fire',
        ]
        if curr_location in opened_doors:
            options.append('Look through giant hole')
        if hero['estus']:
            options.append('Drink estus')
        chs = output(options)
        if chs == 1:
            if curr_location not in opened_doors:
                clear()
                show_status()
                situation('You hear strange voices coming upper')
                options = [
                    'Rush',
                    'Get back',
                    'Jump to side',
                ]
                chs = output(options)
                if chs == 1 or chs == 2:
                    text = "That was a giant steel ball, You couldn't dodge it but it has left a big hole on wall"
                    hero['health'] -= 50
                else:
                    text = "That was a giant steel ball, You could dodge it and it has left a big hole on wall"
                opened_doors.append(curr_location)
            else:
                if 'steel ball undead' in alive_enemies:
                    return undead_swordsman_fight(curr_location, 'third floor')
                else:
                    return third_floor()
        elif chs == 2:
            if 'central fire' not in opened_doors:
                message('You have opened door to central fire')
                opened_doors.append('central fire')
            return central_fire()
        elif chs == 3:
            if 'corridor archer' in alive_enemies:
                undead_archer_fight('corridor archer', 'second floor')
                return side_corridor()
            else:
                return side_corridor()
        elif curr_location in opened_doors and chs == 4 and not hero['estus']:
            clear()
            show_status()
            situation("You see a wounded knight")
            options = [
                "Attack him",
                'Talk to knight',
                'Leave',
            ]
            chs = output(options)
            if chs == 1:
                hero['estus'] = 2
                text = 'You have killed the knight and got estus, estus restores your health'
            elif chs == 2:
                hero['estus'] = 2
                text = ' - I am an astorian knight im damaged so I cant move, take this estus, estus restores your health'
            elif chs == 3:
                continue
        elif curr_location in opened_doors and chs == 4:
            text = 'The knight lies wounding on ground'
        elif chs == 5:
            drink_estus()
                
def side_corridor():
    clear()
    show_status()
    set_location('side corridor')
    print(bonfire)
    options = [
        'Take a rest',
        'Go further by corridor',
        'Return to central arena',
        'Open inventory',
    ]
    chs = output(options)
    if chs == 1:
        take_rest()
        return side_corridor()
    elif chs == 2:
        if 'corridor archer' in alive_enemies:
            undead_archer_fight('corridor archer', 'second floor')
            return second_floor()
        else:
            return second_floor()
    elif chs == 3:
        return central_arena()
    elif chs == 4:
        alert('TODO')
    
def central_arena():
    clear()
    set_location('central arena')
    if enemies['asylum demon']:
        message("here it come flying from the sky")
        print(asylum_demon)
        enter_to_continue()
        return asydemon_fight()
    else:
        clear()
        show_status()
        situation('Empty arena')
        options = [
            'Go to side door',
            'Open backside of central doors'
        ]
        chs = output(options)
        if chs == 1:
            return side_corridor()
        elif chs == 2:
            alert('TODO')

def central_fire():
    clear()
    show_status()
    set_location('central fire')
    print(bonfire)
    options = [
        'take a rest',
        'go to side door',
        'go through central gates',
        'go to prison corridor',
        'open inventory'
    ]
    user_chose = output(options)
    if user_chose == 1:
        take_rest()
        return central_fire()
    elif user_chose == 2:
        if curr_location in opened_doors:
            return second_floor()
        else:
            message('door cant be opened from this side')
            return central_fire()
    elif user_chose == 3:
        central_arena()
    elif user_chose == 4:
        return room_corridor()
    elif user_chose == 5:
        return alert('TODO')

def room_corridor():
    global alive_enemies
    clear()
    set_location('room corridor')
    show_status()
    options = []
    if curr_location in alive_enemies:
        situation("You see 3 undeads staying at wall, they don't attack you")
        options = [
            'Pass them silently',
            'Get back to prison room',
            'Attack them',
        ]
    else:
        situation('you have defeated enemies in corridor')
        options = [
            'Leave corridor',
            'Go to prison room'
        ]
    user_choice = output(options)
    if user_choice == 1:
        return central_fire()
    elif user_choice == 2:
        clear()
        return prison_room()
    elif user_choice == 3 and curr_location in alive_enemies:
        alive_enemies.remove(curr_location)
        hero = drop({'name': 'broken sword', 'poss': 25}, {'name': 'undead soldiers armor', 'poss': 30})
        return room_corridor()

def prison_room():
    clear()
    set_location('prison room')
    options = []
    if not prev_location:
        show_status()
        situation("You wake up in an unknown prison surrounded by cold dark walls sitting somewhere at the corner not to hear terrible sounds coming from outside your room. Suddenly, a dead body falls from top of your room where is a big hole to outside, slowly awaking you look up and you see a leaving knight. А body has a key hanging on the belt, very similar to the one that locked you here")
        options = ['Open prison room door']
    options = ['Go to corridor']

    if global_loot['prison key'] not in hero['inventory']: # if user haven't taken room key
        options.append('Take the key')

    chose = output(options)
    if chose == 1 and global_loot['prison key'] not in hero['inventory']:  # if he tries to open without key
        message('door is locked')
        show_status()
        return prison_room()
    elif chose == 1:    # if key is taken
        if not prev_location:
            message('door opens')
        clear()
        return room_corridor()
    elif chose == 2:    # to take the key
        message("you've got the key")
        hero['inventory'].append(global_loot['prison key'])
        show_status()
        return prison_room()

# functions part

def output(arr):  # output(['hello', 'its me'])

    print(" "*47 + "_"*80)
    for index in range(len(arr)): # for long space
        option = arr[index]
        print()
        print(" "*38 + f"<| {index + 1} |> " + "◆" + " "*(40 - len(option)//2) + option + " "*(40 - len(option)//2 - len(option) % 2) + "◆" + f" <| {index + 1} |> ")
        print(" "*47 + "_"*80)
    # 0 for back or exit
    print("\n\n" + " "*58 + "<| 0 |> " + "◆" + " "*(20 - len('main menu')//2) + 'main menu' + " "*(20 - len('main menu')//2) + "◆" + " <| 0 |> ")
    print(" "*67 + "_"*40)
    # input part
    user_choice = input("\n" + " " * 84 + ">| ")
    temp_list = [str(i + 1) for i in range(len(arr))]

    if user_choice == '0':
        return main_menu()
    elif user_choice in temp_list or user_choice == '0': # if this choose exists in list
        return int(user_choice)
    else:
        alert('wrong input')
        show_status()
        return output(arr)

def new_game():
    hero_creator()
    clear()
    return prison_room()

def creator_info():
    clear()
    line = "R A N D O M - J O R D A N"
    print('\n' * 10)
    print('__' * 87 + '\n')
    print(' ' * (87 - len(line) // 2) + line + '\n')
    line = 'https://github.com/random-jordan'
    print(' ' * (87 - len(line) // 2) + line )
    print('__' * 87 + '\n')
    line = 'press enter to continue'
    print(' ' * (87 - len(line) // 2) + line )
    input()
    return main_menu()

def main_menu():
    clear()
    main_menu_options = [
        'continue',
        'new game',
        'credits' 
    ]
    print(logo)
    print(" "*67 + "_"*40)
    for index in range(len(main_menu_options)):
        chose = main_menu_options[index].upper()
        print()
        print(" "*58 + f"<| {index + 1} |> " + "◆" + " "*(20 - len(chose)//2) + chose + " "*(20 - len(chose)//2 - len(chose) % 2) + "◆" + f" <| {index + 1} |> ")
        print(" "*67 + "_"*40)
    
    print("\n\n" + " "*58 + "<| 0 |> " + "◆" + " "*(20 - len('EXIT')//2) + 'EXIT' + " "*(20 - len('EXIT')//2) + "◆" + " <| 0 |> ")
    print(" "*67 + "_"*40)
    # input part
    user_choice = input("\n" + " " * 84 + ">| ")
    user_choice = user_choice[0]
    temp_list = [str(i + 1) for i in range(len(main_menu_options))]

    if user_choice not in temp_list and user_choice != '0':
        alert('wrong input')
        return main_menu()
    
    user_choice = int(user_choice)

    if user_choice == 1:
        load_location()
        return main_menu()
    elif user_choice == 2:
        return new_game()
    elif user_choice == 3:
        return creator_info()
    elif user_choice == 0:
        exit()
    else:
        alert('unknown error')
        exit()


side_corridor()  # displaying main menu 