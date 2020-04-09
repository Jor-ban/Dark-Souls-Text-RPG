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

def situation(text):
    clear()
    print() #newline
    arr = text.split()
    arr[0].upper()
    stopped_index = 0
    line = ''
    for word in arr:
        if len(line) < 75:
            line += word + " "
        else:
            print(" "*48 + line)
            line = ''

def achieve(name):
    clear()
    print('\n' * 10)
    print(' ' * 67 + '-' * 42 + '\n' + " "*58 + "~~~~~~~~!  " + " "*(19 - len(name)//2) + name.upper() + " "*(19 - len(name)//2) + "  !~~~~~~~~ \n" + ' ' * 67 + '-' * 42)
    print(" " * 75 + "press Enter to continue")
    input()
    clear() # clearing the console

def location(name):
    print('\n' + " "*58 + "-------|  " + " "*(19 - len(name)//2) + name.upper() + " "*(19 - len(name)//2) + "  |------- \n")

def alert(message):
    clear()
    print('\n' * 10)
    print(" "*58 + ">> !! >> " + "█" + " "*(19 - len(message)//2) + message + " "*(19 - len(message)//2) + "█" + " << !! << ")
    print(" "*68 + "_"*39)
    print(" " * 75 + "press Enter to continue")
    input()
    clear() # clearing the console

def output(picture, arr, style, last_option):  # output(None, ['hello', 'its me'], 'extended', 'back')
    # text pictire part
    if picture:
        print(picture)
    # outputing options
    chose = ''
    if style == 'small' or style == 'short':  # small space with capital letters (main menu mostly)
        print(" "*67 + "_"*40)
        for index in range(len(arr)):
            chose = arr[index].upper()
            print()
            print(" "*58 + f"<| {index + 1} |> " + "█" + " "*(20 - len(chose)//2) + chose + " "*(20 - len(chose)//2 - len(chose) % 2) + "█" + f" <| {index + 1} |> ")
            print(" "*67 + "_"*40)
    else:
        print(" "*47 + "_"*80)
        for index in range(len(arr)): # for long space
            chose = arr[index]
            print()
            print(" "*38 + f"<| {index + 1} |> " + "█" + " "*(40 - len(chose)//2) + chose + " "*(40 - len(chose)//2 - len(chose) % 2) + "█" + f" <| {index + 1} |> ")
            print(" "*47 + "_"*80)
    # 0 for back or exit
    print("\n\n" + " "*58 + "<| 0 |> " + "█" + " "*(20 - len(last_option)//2) + last_option + " "*(20 - len(last_option)//2) + "█" + " <| 0 |> ")
    print(" "*67 + "_"*40)
    # input part
    user_choice = input("\n" + " " * 84 + ">| ")
    temp_list = [f'{i + 1}' for i in range(len(arr))]
    if user_choice in temp_list or user_choice == '0': # if this choose exists in list
        return int(user_choice)
    else:
        alert('W R O N G  I N P U T')
        return output(picture, arr, style, last_option)


classes = {
    'knight': {
        'name'      : '',
        'class'     : 'knight',
        'info'      : 'very powerfull',
        'start-inv' : 'knight sword and armor',
        'health'    : 100,
        'power'     : 100,
        'luck'      : 0.8,
        'inventory' : [
            {
                'class': 'sword',
                'name': 'balders knight sword',
                'power': 75,
                'prot': 23,
                'distance': 0.8
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
        'info'      : 'long distance fight',
        'start-inv' : 'magic stick and dress',
        'health'    : 50,
        'power'     : 100,
        'luck'      : 1,
        'fight-dist': 1.5,
        'inventory' : [
            {
                'class': 'sword',
                'name': 'wooden magic stick',
                'power': 100,
                'prot': 13,
                'distance': 3,
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
        'info'      : 'ultra lucky',
        'start-inv' : 'nothing',
        'health'    : 120,
        'power'     : 100,
        'luck'      : 1.6,
        'inventory' : [
        ],  
    }
}
