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
bonfire = """                                  ``-                                                               
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

clear()
menu_choice = output(logo, main_menu_options, 'short', 'EXIT')
