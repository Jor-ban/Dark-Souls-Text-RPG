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
bonfire = """                                                                     ``-                                                               
                                                                    `.:                                                               
                                                                    `:                                                               
                                                                        .`                                                              
                                                                        `.  ``                                                          
                                                                        `                                                              
                                                                    `````                                                             
                                                                        ` ``                                                           
                                                                        `.`                                                            
                                                                        ``.                                                           
                                                                        ```                                                           
                                                                        `-.           `                                               
                                                                        .-`       ` `-`                                              
                                                                        ``.        .-:. `                                            
                                                                            ...    ``.::/:`.                                            
                                                                            ..:  `./-:+/o/::.                                           
                                                                            `::-`:+++++++++:-`                                          
                                                                            :+/:+ooo+oo+o+:-`                                          
                                                                            `o++ossoooooo++:.``                                        
                                                                        `..`-/o+osssososso/-----                                       
                                                                    ``.-:/:++++osssssso++//-..`                                      
                                                                    `````.-//-:/:+/o:o+o+++//:-::--```                                  
                                                                    ``-.`.-:/-...-.-.:/:////:/::--:----.`                               
                                                                    ``.`..--.--:-.--::-:/://--:--.....--.``                             
                                                            ``   ``...........--....-:.--::--.-:-:-.`...``                            
                                                                    ```````...-......``...--.....```        """

# variables part

hero = {}
current_map = 'prison'
location_name = ''

# functions part

def set_location(loc):
    global location_name
    location_name = loc
    location_print(loc)

def load_location(name):
    clear()
    location_print(name)
    if name == 'prison room':
        return prison_room()
    elif name == 'room corridor':
        return room_corridor()

def room_corridor():
    set_location('room corridor')
    situation(" You see 3 undeads staying at wall and crying, they don't attack you")

def prison_room():
    set_location('prison room')
    options = ['open prison room door']
    if global_loot['prison key'] not in hero['inventory']: # if user haven't taken room key
        options.append('take the key')
    chose = output(None, options, 'extended', 'menu')
    if chose == 1 and global_loot['prison key'] not in hero['inventory']:  # if he tries to open without key
        message('door is locked')
        status(hero)
        return prison_room()
    elif chose == 1:    # if key is taken
        message('door opens')
        return room_corridor()
    elif chose == 2:    # to take the key
        message("you've got the key")
        hero['inventory'].append(global_loot['prison key'])
        status(hero)
        return prison_room()
    else:
        return main_menu()

def load_game():
    if location_name:
        return load_location(location_name)    
    else:
        alert("N O   G A M E S   F O U N D")
        return main_menu()

def new_game():
    global hero
    hero = hero_creator()
    clear()
    status(hero)
    situation("You wake up in an unknown prison surrounded by cold dark walls sitting somewhere at the corner not to hear terrible sounds coming from outside your room. Suddenly, a dead body falls from top of your room where is a big hole to outside, slowly awaking you look up and you see a leaving knight. А body key is hanging on the belt, very similar to the one that locked you here")
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
    menu_choice = output(logo, main_menu_options, 'short', 'EXIT')
    if menu_choice == 1:
        return load_game()
    elif menu_choice == 2:
        return new_game()
    elif menu_choice == 3:
        return creator_info()
    elif menu_choice == 0:
        exit()
    else:
        alert('U N K N O W N   E R R O R')
        exit()
main_menu()  # displaying main menu 