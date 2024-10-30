#dave.py

import os
import time

def clear():
    if os.system == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def add():
    pass

def sub():
    pass

def mult():
    pass

def div():
    pass

def asmd():
    pass

def main():
    clear()
    print(f""" 
    ╔═════════════════════════╗
    ║       CALCULATOR        ║
    ╠═════════════════════════╣
    ║  1.   Addition          ║
    ║  2.   Subtraction       ║
    ║  3.   Multiplication    ║
    ║  4.   Division          ║
    ║  5.   All in One        ║
    ║  0.   Exit              ║
    ╚═════════════════════════╝""")
    choice = int(input("     Choice: "))
    time.sleep(1)
    clear()

    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mult()
    elif choice == 4:
        div()
    elif choice == 5:
        asmd()
    elif choice == 0:
        clear()
        print("Goobye & Thank You!")
    else:
        print("     Invalid input!")

main()