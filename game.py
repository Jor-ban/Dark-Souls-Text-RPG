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
main_menu_options = [
    'continue',
    'new game',
    'creators' 
    ]
hero = {}
current_map = 'prison'
location_name = ''
# functions part
def load_game(): ###TODO
    if current_map and location_name:
        pass
    else:
        alert("N O   G A M E S   F O U N D")
        main_menu()

def new_game():
    location_name = ''
    situation("you wake up in an unknown prison surrounded by cold dark walls sitting somewhere in the corner you do not need to lick terrible sounds coming from outside your room. And deadly, a dead body falls on top of your room, coming to you, you look up and you see a leaving knight. А body key is hanging on the belt, very similar to the one that locked you here")
    chose = output(none,['take the key', 'open locked door'], 'extended', 'menu')

def creator_info():
    pass

def main_menu():
    clear()
    menu_choice = output(logo, main_menu_options, 'short', 'EXIT')
    if menu_choice == 1:
        load_game()
    elif menu_choice == 2:
        new_game()
    elif menu_choice == 3:
        creator_info()
    elif menu_choice == 0:
        exit()
    else:
        alert('U N K N O W N   E R R O R')
main_menu()  # displaying main menu 