# Very rudimentary hex file tool

import os
import sys

buffer = [] # Buffer used for in memory data
file = "None" # File name only, used in prompt
file_path = "None" # Full file path
mode = "None" # Mode

def new_file():
    print("----[ Create new file ]----\n")
    f_name = input("Name : ")
    f_path = input("Path : ")
    f_size = input("Size : ")
    f_fill = input("Fill : ")
    confirm = input("Create this project? (Y/n) : ")
    if confirm == "n":
        print("Cancelled.\n")
        return
    else:
        global buffer
        global file
        global file_path
        buffer = bytearray([int(f_fill, 16)] * int(f_size))
        file = f_name
        file_path = f_path
        print("New buffer instantiated.\n\n")
        return
    
def list_buffer():
    print("----[ Current buffer contents ]----\n")
    index = int("0")
    line = int("0",16)
    print('0x{:04X}'.format(line) + " : ", end ="")
    for b in buffer:
        if index < 15:
            print('0x{:02X}'.format(b), end =" ")
            index = index + 1
        else:
            print("")
            index = 0
            line = line + 16
            print('0x{:04X}'.format(line) + " : ", end ="")
    print("\n")
    return

while 1: # Main loop
    cmd = input(file + " [" + mode + "] : ")
    if cmd == "clear":
        os.system('cls')
        continue
    if cmd == "exit":
        print("Very well then, goodbye.\n")
        sys.exit()
        continue
    if cmd == "help":
        print("----[ Help Prinout ]----\n")
        print("\n")
        print("clear     - Clear the console window\n")
        print("exit      - Exit this software\n")
        print("help      - You're looking at it!\n")
        print("list      - List current buffer contents\n")
        print("new       - Create a new file\n")
        continue
    if cmd == "list":
        list_buffer()
        continue
    if cmd == "new":
        new_file()
        continue
    else:
        print("Invalid command " + cmd + "\n")