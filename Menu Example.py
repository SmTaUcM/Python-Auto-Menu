from Auto_Menu import *
import os

def menu_opt_1():
    os.system("cls")
    print "\nOption 1 Now Entered."
    raw_input("\nPress 'Enter' to continue.")

def menu_opt_2():
    os.system("cls")
    print "\nOption 2 Now Entered."
    raw_input("\nPress 'Enter' to continue.")

def menu_opt_3():
    sub_menu = Menu(["Back", "Sub Option 1"])

    while sub_menu.active:
        os.system("cls")
        print ""
        sub_menu.draw()
        key = sub_menu.get_key()

        if key == "Up":
            sub_menu.option -= 1
        elif key == "Down":
            sub_menu.option += 1
        elif key == "Enter":
            if sub_menu.option == 0:
                sub_menu.active = False
                os.system("cls")
            elif sub_menu.option == 1:
                sub_menu_opt_1()

def sub_menu_opt_1():
    os.system("cls")
    print "\nSub Option 1 Now Entered."
    raw_input("\nPress 'Enter' to continue.")

menu = Menu(["Exit", "Option 1", "Option 2", "Another Menu"])

while menu.active:
    os.system("cls")
    print ""
    menu.draw()
    key = menu.get_key()

    if key == "Up":
        menu.option -= 1
    elif key == "Down":
        menu.option += 1

    elif key == "Enter":
        if menu.option == 0:
            menu.active = False
            os.system("cls")

        elif menu.option == 1:
            menu_opt_1()

        elif menu.option == 2:
            menu_opt_2()

        elif menu.option == 3:
            menu_opt_3()

print "\nGood-Bye."
raw_input("\nPress 'Enter' to exit.")