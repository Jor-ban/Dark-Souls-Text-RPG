from engine import *

# pictures part
logo = """                                         `                                                                                                                             ``           
               ./:------...`           `-/      ..........`       .......   `.....           `-:::-.`      `.----.`     .......     ......`.......           .----.`   ..           
               `+yNNNdyssyhddy/.     `/hNN-     /yNNNdyydmdo.     :yNNNy-  `ommhs/`        .ymmyssdmy`  `/sdho++oydy+.  :smmmo:     :smmo-`/ymmmo/        `/hds+oymh-               
                 .MMM:    `:hMMms`   `hMMMd`     .NMMo``.yMMm.     :MMM-  .yNd/.          `hMM+`  .sy` /dMm/`    `/mMmo` .NMM.       `dh`   /MMd`         +MMo`` `/d:               
                 `MMN.      `yMMMs   :NhNMMs`    `NMMo   +MMM-     :MMM.`+mm+`    ```     `dMMd/`  `` :NMM/        -dMMy``NMM.       `hy    :MMd`         +MMm/.   `                
        `````````.MMM. ``.```:NMMN-.-dh:sMMN/```.-NMMy//omMms.``   :MMMhdMd:```  ``` `     -dNMMmy+-.`yMMN-````````.oMMM:-NMM-```.```.dy.```/MMd.````  ```.smMMmho:...``````        
         ````````.NMM- ```` `.mMMN..hMhyyNMMm-``..NMMdsmMMm:```    :MMMsdMNy:``.          ` `:ohNMMNo.sMMN-`````````+MMM/.NMM-`````` .my`  `/MMd`` `    ````.+ymMMNy.````           
                 `mMM.       -NMN+`sN+:::/NMMy`  `NMMs`-hMMh-      :MMM-`+mMNs..          ./   `-sMMN--mMMo`       `hMMh``mMM:       .No    /MMd`      `  :`   `/mMM/               
                 `mMM:    `./mMd/`+Ms     /MMM+  .NMMs  `sNMm/`    :MMM-  .sNMmo.        `yNo.   `mMN- :mMMo.     .sMNy.  oNMd-     .ym-    /MMm`     -h:+Ns.    +MM+               
               `+sNMMmsooshdds/./sNN/`    -mNNmo/sNNNd:   :ymmy:` -sNNNo`  `oNNNdo-`     `/mNms//smy-   .+dmho++oshds:`    /hNmhoooyhs-   ./hNNNs+//+odN/-yNds//odmo`               
               `:::::::::--.`  `--:--`    .------------     `.--` .-----`   .------.       .:////:.       `.-:///:.`         .:///:-`     .-------------`  -:///:-`               
\n""" + ' '* 80 + 'T E X T   R P G \n\n'
bonfire = """                                                                                O          
                                                                                '       
                                                                                [         
                                                                                }         
                                                                                |         
                                                                            =========    (                     
                                                                               |#|      (                    
                                                                               |#|     ((/                   
                                                                               |#|((((((                   
                                                                               |((/((//(((                   
                                                                            ,(((((((*((((                   
                                                                            ((((/((((**(((                   
                                                                        .   ((((((/(****((((((                
                                                                        ((  (((((*******(((((((  /            
                                                                        (((((((*****.*****((((((((/           
                                                                        /(((*((*****....****(((((((           
                                                                        (((**/*****......*****(((            
                                                                        (((***.*........,.***((             
                                                                            ((**............**(.              
                                                                            /**........*(      """

# variables part
hero = {
    'name'      : 'Jordan',
    'class'     : 'knight',
    'info'      : 'very powerfull',
    'start-inv' : 'knight sword and armor',
    'health'    : 100,
    #
    'init_heal' : 100,
    'estus'     : None,
    #
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

enemies = ['room corridor', ]
alive_enemies = enemies
current_map = 'prison'
curr_location = None
prev_location = None

#locations functions

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
    else:
        alert("no games found")
        return main_menu()


def central_fire():
    clear()
    set_location('central fire')
    print(bonfire)

def room_corridor():
    clear()
    set_location('room corridor')
    show_status(hero)
    options = []
    if curr_location in alive_enemies:
        situation(" You see 3 undeads staying at wall, they don't attack you")
        options = [
            'Pass them silently',
            'Get back to prison room',
            'Attack them',
        ]
    else:
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
        pass
    else:
        alert('unknown error')
        return main_menu()

def prison_room():
    clear()
    set_location('prison room')
    options = ['Go to corridor']
    if not prev_location:
        options = ['Open prison room door']

    if global_loot['prison key'] not in hero['inventory']: # if user haven't taken room key
        options.append('Take the key')

    chose = output(options)
    if chose == 1 and global_loot['prison key'] not in hero['inventory']:  # if he tries to open without key
        message('door is locked')
        show_status(hero)
        return prison_room()
    elif chose == 1:    # if key is taken
        if not prev_location:
            message('door opens')
        clear()
        return room_corridor()
    elif chose == 2:    # to take the key
        message("you've got the key")
        hero['inventory'].append(global_loot['prison key'])
        show_status(hero)
        return prison_room()
    else:
        alert("unknown error")
        return main_menu()

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
        show_status(hero)
        return output(arr)
     

def new_game():
    global hero
    hero = hero_creator()
    clear()
    show_status(hero)
    situation("You wake up in an unknown prison surrounded by cold dark walls sitting somewhere at the corner not to hear terrible sounds coming from outside your room. Suddenly, a dead body falls from top of your room where is a big hole to outside, slowly awaking you look up and you see a leaving knight. А body has a key hanging on the belt, very similar to the one that locked you here")
    return prison_room()

def creator_info():
    pass

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
    temp_list = [str(i + 1) for i in range(len(main_menu_options))]

    if user_choice not in temp_list and user_choice != '0':
        alert('wrong input')
        return main_menu()
    
    user_choice = int(user_choice)

    if user_choice == 1:
        return load_location()
    elif user_choice == 2:
        return new_game()
    elif user_choice == 3:
        return creator_info()
    elif user_choice == 0:
        exit()
    else:
        alert('unknown error')
        exit()
room_corridor()  # displaying main menu 