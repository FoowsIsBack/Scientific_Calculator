#dave.py

import os
import time

def clear():
    if os.system == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def add():
    global num1, num2, result
    print(f""" 
    ╔═════════════════════════╗
    ║        ADDITION         ║
    ╚═════════════════════════╝""")
    num1 = int(input("     Num1: "))
    num2 = int(input("     Num2: "))
    result = num1 + num2
    time.sleep(1)
    clear()
    add_result()

def add_result():
    print(f""" 
    ╔═════════════════════════╗
    ║     ADDITION RESULT     ║
    ╠═════════════════════════╣
    ║       Num1 = {num1:<10} ║
    ║       Num2 = {num2:<10} ║
    ║       Total = {result:<10}║
    ╚═════════════════════════╝""")
    choice = input("     Choice: ")
    time.sleep(1)
    main()


def sub():
    global num1, num2, result
    print(f""" 
    ╔═════════════════════════╗
    ║        ADDITION         ║
    ╚═════════════════════════╝""")
    num1 = int(input("     Num1: "))
    num2 = int(input("     Num2: "))
    result = num1 - num2
    time.sleep(1)
    clear()
    sub_result()


def sub_result():
    print(f""" 
    ╔═════════════════════════╗
    ║    SUBTRACTION RESULT   ║
    ╠═════════════════════════╣
    ║       Num1 = {num1:<10} ║
    ║       Num2 = {num2:<10} ║
    ║       Total = {result:<10}║
    ╚═════════════════════════╝""")
    choice = input("     Choice: ")
    time.sleep(1)
    main()

def mult():
    global num1, num2, result
    print(f""" 
    ╔═════════════════════════╗
    ║      MULTIPLICATION     ║
    ╚═════════════════════════╝""")
    num1 = int(input("     Num1: "))
    num2 = int(input("     Num2: "))
    result = num1 * num2
    time.sleep(1)
    clear()
    mult_result()

def mult_result():
    print(f""" 
    ╔═════════════════════════╗
    ║  MULTIPLICATION RESULT  ║
    ╠═════════════════════════╣
    ║       Num1 = {num1:<10} ║
    ║       Num2 = {num2:<10} ║
    ║       Total = {result:<10}║
    ╚═════════════════════════╝""")
    choice = input("     Choice: ")
    time.sleep(1)
    main()       

def div():
    global num1, num2, result
    print(f""" 
    ╔═════════════════════════╗
    ║        DIVISION         ║
    ╚═════════════════════════╝""")
    num1 = int(input("     Num1: "))
    num2 = int(input("     Num2: "))
    result = num1 / num2
    time.sleep(1)
    clear()
    div_result()

def div_result():
    print(f""" 
    ╔═════════════════════════╗
    ║     DIVISION RESULT     ║
    ╠═════════════════════════╣
    ║       Num1 = {num1:<10} ║
    ║       Num2 = {num2:<10} ║
    ║       Total = {result:<10.5f}║
    ╚═════════════════════════╝""")
    choice = input("     Choice: ")
    time.sleep(1)
    main()  


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
        print("       Invalid input!")
        time.sleep(1.5)
        main()

main()