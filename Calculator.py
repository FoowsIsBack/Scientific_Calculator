#dave.py

import os

def clear():
    if os.system == 'nt':
        os.system('cls')
    else:
        os.system('clear')


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

    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 0:
        pass
    else:
        print("     Invalid input!")

main()