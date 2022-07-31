# C:\Users\Root\0\python

import os

from time import sleep

def run_replace():
    print('''
    RRRRRRRRRRRRRR  EEEEEEEEEEEEEEEEE  PPPPPPPPPPPPP  LLLLLLLL      AAAAAAAAAAAAAAAA  CCCCCCCCCCCC   EEEEEEEEEEEEEEEEE
    RRRRRo      RR  EEEEEEEo           PPPP     oooo  LLLLLLLo      AAAAAo    oooooo  CCCo       oo  EEEEEEEo
    RRRRRo      RR  EEEEEEEooooooooo   PPPP     oooo  LLLLLLLo      AAAAAo    oooooo  CCCo           EEEEEEEooooooooo
    RRRRRooooooooo  EEEEEEEooooooooo   PPPPooooooooo  LLLLLLLo      AAAAAooooooooooo  CCCo           EEEEEEEooooooooo
    RRRRRooooooo    EEEEEEEooooooooo   PPPPPP         LLLLLLLo      AAAAAooooooooooo  CCCo           EEEEEEEooooooooo
    RRRRRo   oooo   EEEEEEEo           PPPPPP         LLLLLLLooooo  AAAAAo    oooooo  CCCo       oo  EEEEEEEo
    RRRRRoo  ooooo  EEEEEEEoooooooooo  PPPPPP         LLLLLLLooooo  AAAAAo    oooooo  CCCooooooooo   EEEEEEEoooooooooo

        ''')

    give_me_path = input("[+]Please Give me Files path:\n")

    try:
        os.chdir(give_me_path)
    
    except:
        print("[-]Path Not Found!\nTry Again ..")

    len_files = len(os.listdir())

    len_name = 0

    file_names = input("[+]Please Give me Name for files:\n")

    format = input("[+]Please Give me Some Format:\n")

    print("[%s]Lenght files"%(len_files))

    sleep(2)

    print("[*]Getting Files Name ..")
    
    sleep(2)
    
    for some_ls in os.listdir():
        
        print(some_ls)


    while len_name <= len_files :
        
        for ls in os.listdir() :

            full_names = f"{file_names}_{len_name}.{format}"
            os.replace(ls, full_names)
            len_name += 1
        
            if len_name == len_files:
                
                print("[\]Job Finished \nGood Bye!")
                sleep(4)
                break
while True:
    help = input("[+]Can I Help You?\n*n/Y\n")
    if help == str('n'):
        print("[-]Good Luck\nBye bye!")
        sleep(4)
        break
    elif help == str('y'):
        print("[*]Very Good\nGo!")
        sleep(2)
        run_replace()



