import account

import os

users = []
class admin:
    def __init__(self):
        while True:
            os.system('cls||clear')
            option = int(input(' 1: Get users \n 2: Remove user \n 3: Add user \n 4: Edit user \n 5: Exit \n '))
            if option == 1:
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
                break
            else:
                print(' Something went wrong, please try again (Just numbers from 1-3) ')
    def get_users(self):
        os.system('cls||clear')
        for user in users:
            print(' ID: ', user.get_id())
            print(' User: ', user.get_name())
            print(' Age: ', user.get_age())
            print(' Balance: ', user.get_balance())
            print(' Savings: ', user.get_savings())
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
                    print(' You do not hold this amount in your balance ')
                    input(' Press any key to continue ')
                else:
                    print(' Success, value transfered ')
                    print(' Press any key to continue ')
            elif option == 5:
                amount = int(input(' How much to transfer out savings: '))
                response = users[id].transfer_out_savings(amount)
                if response == 1:
                    print(' You do not hold this amount in your savings ')
                    input(' Press any key to continue ')
                else:
                    print(' Success, value transfered')
                    input(' Press any key to continue ')
            elif option == 6:
                amount = int(input(' Set an interest rate for your savings account: '))    
                users[id].set_interest(amount)

admin()
