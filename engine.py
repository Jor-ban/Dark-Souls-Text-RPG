from os import system, name 
from random import randint

# define console clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        system('clear') 


def output(picture, arr, style, last_option):  # output(None, ['hello', 'its me'], 'extended', 'back')
    # text pictire part
    if picture:
        print(picture)
    # outputing options
    chose = ''
    if style == 'small' or style == 'short':  # small space with capital letters (main menu mostly)
        for index in range(len(arr)):
            chose = arr[index].upper()
            print()
            print(" "*58 + f"<| {index + 1} |> " + "█" + " "*(20 - len(chose)//2) + chose + " "*(20 - len(chose)//2 - len(chose) % 2) + "█" + f" <| {index + 1} |> ")
            print(" "*67 + "_"*40)
    else:
        for index in range(len(arr)): # for long space
            chose = arr[index]
            print()
            print(" "*38 + f"<| {index + 1} |> " + "█" + " "*(40 - len(chose)//2) + chose + " "*(40 - len(chose)//2 - len(chose) % 2) + "█" + f" <| {index + 1} |> ")
            print(" "*47 + "_"*80)
    # 0 for back or exit
    print("\n\n" + " "*58 + "<| 0 |> " + "█" + " "*(20 - len(last_option)//2) + last_option + " "*(20 - len(last_option)//2) + "█" + " <| 0 |> ")
    print(" "*67 + "_"*40)
    # input part
    user_choice = input("\n                                                               >> ")
    temp_list = [f'{i + 1}' for i in range(len(arr))]
    if user_choice in temp_list or user_choice == '0': # if this choose exists in list
        return (int(user_choice) - 1)
    else:
        wrong_option = 'W R O N G  I N P U T'
        print("\n\n" + " "*58 + ">> !! >> " + "█" + " "*(20 - len(wrong_option)//2) + wrong_option + " "*(20 - len(wrong_option)//2) + "█" + f" << !! << ")
        print(" "*67 + "_"*40)
        print(" " * 75 + "press Enter to continue")
        input()
        clear() # clearing the console
        return output(picture, arr, style, last_option)


classes = {
    'knight': {
        'name'      : '',
        'class'     : 'knight',
        'health'    : 100,
        'power'     : 100,
        'luck'      : 0.8,
        'inventory' : [
            {
                'class': 'sword',
                'name': 'balders knight sword',
                'power': 75,
                'prot': 23
            },
            {
                'class': 'armor',
                'name': 'balder knight armor',
                'prot': 45,
            }
        ],  
    },
    'magician': {
        'name'      : '',
        'class'     : 'magician',
        'health'    : 50,
        'power'     : 100,
        'luck'      : 1,
        'inventory' : [
            {
                'class': 'sword',
                'name': 'wooden magic stick',
                'power': 100,
                'prot': 13
            },
            {
                'class': 'armor',
                'name': 'poor magician\'s dress',
                'prot': 25,
            }
        ],  
    },
    'poor': {
        'name'      : '',
        'class'     : 'poor',
        'health'    : 120,
        'power'     : 100,
        'luck'      : 1.6,
        'inventory' : [
        ],  
    }
}
hero = {}

clear()
#print(output(['hello', 'its me'], 'extended', 'back'))