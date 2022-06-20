from classes.account import *
from classes.days import *
from classes.log import *

import os

users = []

class admin:
    def __init__(self):
        self.days = days()
        while True:
            os.system('cls||clear')
            option = int(input(' 0: Admin \n 1: Get users \n 2: Remove user \n 3: Add user \n 4: Edit user \n 5: Exit \n '))
            if option == 0:
                self.admin()
            elif option == 1:
                self.get_users()
            elif option == 2:
                os.system('cls||clear')
                id = int(input(' What is the user ID: '))
                self.remove_user(id)
            elif option == 3:
                self.add_user()
            elif option == 4:
                os.system('cls||clear')
                id = int(input(' What is the user ID: '))
                self.edit_user(id)
            elif option == 5:
                log()
                break
            else:
                self.status_log(' Something went wrong, please try again (Just numbers from 0-5) ')
    def status_log(self, text):
        print(text)
        input(' Press any key to continue ')
    def admin(self):
        os.system('cls||clear')
        option = int(input(' 1: Delete logs \n 2: Delete accounts \n 3: Pass day \n'))
        if option == 1:
            os.remove('personal_account_python_log.txt')
            os.remove('personal_account_python_log_backup.txt')
            self.status_log(' Success! all logs have been deleted ')
        elif option == 2:
            self.users = []
            self.status_log(' Success! all accounts have been deleted ')
        elif option == 3:
            self.days.pass_day(users)
            self.status_log(' Success! day passed, and user yields updated ')
        else:
            self.status_log(' Something went wrong, please try again (Just numbers from 1-3) ')
    def get_users(self):
        os.system('cls||clear')
        for user in users:
            print(' ID: ', user.get_id())
            print(' User: ', user.get_name())
            print(' Age: ', user.get_age())
            print(' Balance: ', user.get_balance())
            print(' Savings: ', user.get_savings())
            print(' Interest: ', user.get_interest(), '%')
            print('\n')
        input(' Press any key to continue ')
    def add_user(self):
        os.system('cls||clear')
        name = input(' What is your name: ')
        age = input(' What is your age: ')
        id = len(users)
        users.append(account(id, name, age))
        self.status_log(' Success! user added ')
    def remove_user(self, id):
        users.pop(id)
    def edit_user(self, id):
        while 1:
            os.system('cls||clear')
            option = int(input(' 1: Exit \n 2: Add balance \n 3: Remove balance \n 4: Add savings \n 5: Remove savings \n 6: Set interest \n '))
            if option == 1:
                break
            elif option == 2:
                amount = int(input(' How much to add: '))
                users[id].add_balance(amount)
            elif option == 3:
                amount = int(input(' How much to remove: '))
                users[id].remove_balance(amount)
            elif option == 4:
                amount = int(input(' How much to transfer in savings: '))
                response = users[id].transfer_in_savings(amount)
                if response == 1:
                    self.status_log(' You do not hold this amount in your balance ')
                else:
                    self.status_log(' Success! value transfered ')
            elif option == 5:
                amount = int(input(' How much to transfer out savings: '))
                response = users[id].transfer_out_savings(amount)
                if response == 1:
                    self.status_log(' You do not hold this amount in your savings ')
                else:
                    self.status_log(' Success! value transfered ')
            elif option == 6:
                amount = int(input(' Set an interest rate for your savings account: '))    
                response = users[id].set_interest(amount)
                if response == 1:
                    self.status_log(' Are you sure that this is correct? > 1000% seems a lot ')
                else:
                    self.status_log(' Success! interest set ')

admin()
