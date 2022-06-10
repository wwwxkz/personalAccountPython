# Note print('\x1b[2J') also works, but not in all terminals, that is why I am using OS.
# In a production enviroment I would try to use as few libs as possible, and the fastest
# solutions, like a simple print
import os
# Using Tkinter instead of QT or other faster framework because of the simplicity and
# development speed of Tkinter. For more personalization you can port the core code to
# QT, GTK, or any other framework, I will make "front and backend" separeted
from tkinter import *

# Ask user if he wants to run in fallback mode (console/terminal with core features)
while True:
    fallback = int(input(' Would you like to run in fallback mode 0/Yes 1/No: '))
    if fallback == 1 or fallback == 0:
        break

# Save users locally in a global var
users = []
# User admin class to control de banking solution
class admin:
    # Start control panel in while True, without break from root, just from childs
    # Actually there is a break, but in the Exit option
    def __init__(self):
        while True:
            if fallback = 0:
                os.system('cls||clear')
                option = int(input(' 1: Get users \n 2: Remove user \n 3: Add user \n 4: Edit user \n 5: Exit \n '))
                if option == 1:
                    self.get_users()
                elif option == 2:
                    self.remove_user()
                elif option == 3:
                    self.add_user()
                elif option == 4:
                    os.system('cls||clear')
                    id = int(input(' What is the user ID: '))
                    self.edit_user(id)
                elif option == 5:
                    break
                else:
                    print(' Something went wrong, please try again (Just numbers from 1-3) ')

    # Deal with user Account class throught functions, add, remove, and edit users
    def get_users(self):
        os.system('cls||clear')
        for user in users:
            print(' ID: ', user.get_id())
            print(' User: ', user.get_name())
            print(' Age: ', user.get_age())
            print(' Balance: ', user.get_balance())
            print('\n')
        input(' Press any key to continue ')
    def add_user(self):
        os.system('cls||clear')
        name = input(' What is your name: ')
        age = input(' What is your age: ')
        id = len(users)
        users.append(account(id, name, age))  
        print(' Success! user added ')
        input(' Press any key to continue ')
    def edit_user(self, id):
        while 1:
            os.system('cls||clear')
            option = int(input(' 1: Exit \n 2: Add balance \n 3: Remove balance \n '))
            if option == 1:
                break
            elif option == 2:
                amount = int(input(' How much to add: '))
                users[id].add_balance(amount)
            elif option == 3:
                amount = int(input(' How much to remove: '))
                users[id].remove_balance(amount)

# Structure to create new accounts, not acessed directly but throught admin control panel
class account:
    def __init__(self, id, name, age):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__balance = 0
    
    def add_balance(self, to_add):
        self.__balance += to_add
    def remove_balance(self, to_remove):
        self.__balance -= to_remove

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_balance(self):
        return self.__balance

# Create admin instance, and call __Init__ 
admin()
