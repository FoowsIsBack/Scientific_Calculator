#dave.py

import os
import time
import math

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
    choice = input("     Press Enter to Go Back: ")
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
    choice = input("     Press Enter to Go Back: ")
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
    choice = input("     Press Enter to Go Back: ")
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
    choice = input("     Press Enter to Go Back: ")
    time.sleep(1)
    main()  

def qroot():
    global num1, result
    print(f""" 
    ╔═════════════════════════╗
    ║       SQUARE ROOT       ║
    ╚═════════════════════════╝""")
    num1 = int(input("     Num1: "))
    result = math.sqrt(num1)
    time.sleep(1)
    clear()
    qroot_result()

def qroot_result():
    print(f""" 
    ╔═════════════════════════╗
    ║    SQUARE ROOT RESULT   ║
    ╠═════════════════════════╣
    ║       Num1 = {num1:<10} ║
    ║       Qroot = {result:<10.4f}║
    ╚═════════════════════════╝""")
    choice = input("     Press Enter to Go Back: ")
    time.sleep(1)
    clear()
    shift_mode()  

def asmd():
    global num1, num2, result, result1, result2, result3
    print(f""" 
    ╔═════════════════════════╗
    ║  ALL IN ONE CALCULATOR  ║
    ╚═════════════════════════╝""")
    num1 = int(input("     Num1: "))
    num2 = int(input("     Num2: "))
    result = num1 + num2
    result1 = num1 - num2
    result2 = num1 * num2
    result3 = num1 / num2
    time.sleep(1)
    clear()
    asmd_result()

def asmd_result():
    print(f""" 
    ╔═════════════════════════╗
    ║    ALL IN ONE RESULT    ║
    ╠═════════════════════════╣
    ║       Num1 = {num1:<10} ║
    ║       Num2 = {num2:<10} ║
    ╠═════════════════════════╣
    ║       Add = {result:<10}  ║
    ║       Sub = {result1:<10}  ║
    ║       Mult = {result2:<10} ║
    ║       Div = {result3:<10}  ║
    ╚═════════════════════════╝""")
    choice = input("     Press Enter to Go Back: ")
    time.sleep(1)
    main()

def exponent():
    global num1, num2, result
    print(f""" 
    ╔═════════════════════════╗
    ║     RAISED TO POWER     ║
    ╚═════════════════════════╝""")
    num1 = int(input("     Base: "))
    num2 = int(input("     Exponent: "))
    result = math.pow(num1, num2)
    time.sleep(1)
    clear()
    exponent_result()

def exponent_result():
    print(f""" 
    ╔═════════════════════════╗
    ║ {num1} RAISED TO POWER OF {num2} ║
    ╠═════════════════════════╣
    ║      Num1 = {num1:<10}  ║
    ║      Num2 = {num2:<10}  ║
    ║      Result = {result:<10.0f}║
    ╚═════════════════════════╝""")
    choice = input("     Press Enter to Go Back: ")
    time.sleep(1)
    clear()
    shift_mode()  

def factorial():
    global num1, result
    print(f""" 
    ╔═════════════════════════╗
    ║        FACTORIAL        ║
    ╚═════════════════════════╝""")
    num1 = int(input("     Num1: "))
    result = math.factorial(num1)
    time.sleep(1)
    clear()
    factorial_result()

def factorial_result():
    print(f""" 
    ╔═════════════════════════╗
    ║     FACTORIAL RESULT    ║
    ╠═════════════════════════╣
    ║      Num1 = {num1:<10}  ║
    ║      Result = {result:<10}║    
    ╚═════════════════════════╝""")
    choice = input("     Press Enter to Go Back: ")
    time.sleep(1)
    clear()
    shift_mode()

def ncr():
    global num1, num2, result
    print(f""" 
    ╔═════════════════════════╗
    ║        nCr METHODS      ║
    ╚═════════════════════════╝""")
    num1 = int(input("     Num1: "))
    num2 = int(input("     Num2: "))
    result = math.comb(num1, num2)
    time.sleep(1)
    clear()
    ncr_result()    

def ncr_result():
    print(f""" 
    ╔═════════════════════════╗
    ║        nCr RESULT       ║
    ╠═════════════════════════╣
    ║      Num1 = {num1:<10}  ║
    ║      Num2 = {num2:<10}  ║
    ║      Result = {result:<10}║    
    ╚═════════════════════════╝""")
    choice = input("     Press Enter to Go Back: ")
    time.sleep(1)
    clear()
    shift_mode()

def modulus():
    global num1, num2, result
    print(f""" 
    ╔═════════════════════════╗
    ║         MODULUS         ║
    ╚═════════════════════════╝""")
    num1 = int(input("     Num1: "))
    num2 = int(input("     Num2: "))
    result = num1 % num2
    time.sleep(1)
    clear()
    modulus_result()
 
def modulus_result():
    print(f""" 
    ╔═════════════════════════╗
    ║      MODULUS RESULT     ║
    ╠═════════════════════════╣
    ║      Num1 = {num1:<10}  ║
    ║      Num2 = {num2:<10}  ║
    ║      Result = {result:<10}║    
    ╚═════════════════════════╝""")
    choice = input("     Press Enter to Go Back: ")
    time.sleep(1)
    clear()
    shift_mode()

def shift_mode():
    print(f""" 
    ╔═════════════════════════╗
    ║       SHIFT MODE        ║
    ╠═════════════════════════╣
    ║  1.   Square root       ║
    ║  2.   Exponent          ║  
    ║  3.   Factorial         ║   
    ║  4.   nCr               ║
    ║  5.   Modulus           ║
    ║  0.   Back              ║
    ╚═════════════════════════╝""")
    choice = int(input("     Choice: "))
    time.sleep(1)
    clear()

    if choice == 1:
        qroot()
    elif choice == 2:
        exponent()
    elif choice == 3:
        factorial()
    elif choice == 4:
        ncr()
    elif choice == 5:
        modulus()
    elif choice == 0:
        main()

def main():
    clear()
    print(f""" 
    ╔═════════════════════════╗
    ║  SCIENTIFIC CALCULATOR  ║
    ╠═════════════════════════╣
    ║  1.   Addition          ║
    ║  2.   Subtraction       ║
    ║  3.   Multiplication    ║
    ║  4.   Division          ║
    ║  5.   All in One        ║
    ║  6.   Shift-Mode        ║    
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
    elif choice == 6:
        shift_mode()
    elif choice == 0:
        clear()
        print("Goodbye & Thank You!")
    else:
        print(f""" 
        ╔═════════════════════════╗
        ║      Invalid Input!     ║
        ╚═════════════════════════╝""")
        time.sleep(1.5)
        main()

main()