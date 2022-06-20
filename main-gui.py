from classes.account import *
from classes.days import *
from classes.log import *

from tkinter import *

import os

users = []
class admin:
    root = Tk()
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.title("personalAccountPython")
    root.geometry("600x300")
    frm = Frame(root)
    frm.grid()
    def __init__(self):
        self.days = days()
        while True:
            self.clear()
            Label(self.frm, text="Control Panel").grid(column=1, row=0)
            Button(self.frm, text="Admin", command=self.admin).grid(column=1, row=1)
            Button(self.frm, text="Get users", command=self.get_users).grid(column=1, row=2)
            Button(self.frm, text="Add user", command=self.add_user).grid(column=1, row=3)
            Button(self.frm, text="Exit", command=self.safe_exit).grid(column=1, row=4)
            self.root.mainloop()
    def safe_exit(self):
        log()
        self.root.destroy()
    def admin(self):
        self.clear()
        Label(self.frm, text="Admin Control Panel").grid(column=1, row=0)
        Button(self.frm, text="Delete logs", command=self.delete_logs).grid(column=1, row=1)
        Button(self.frm, text="Delete accounts", command=self.delete_accounts).grid(column=1, row=2)
        Button(self.frm, text="Pass day", command=self.pass_day).grid(column=1, row=3)
        Button(self.frm, text="Exit", command=self.__init__).grid(column=1, row=4)
    def delete_logs(self):
        self.clear()
        os.remove('personal_account_python_log.txt')
        os.remove('personal_account_python_log_backup.txt')
        Label(self.frm, text="Success! all logs have been deleted").grid(column=1, row=0)
        Button(self.frm, text="Exit", command=self.admin).grid(column=1, row=1)
    def delete_accounts(self):
        self.clear()
        self.users = []
        Label(self.frm, text="Success! all accounts have been deleted").grid(column=1, row=0)
        Button(self.frm, text="Exit", command=self.admin).grid(column=1, row=1)
    def pass_day(self):
        self.clear()
        self.days.pass_day(users)
        Label(self.frm, text="Success! day passed, and user yields updated").grid(column=1, row=0)
        Button(self.frm, text="Exit", command=self.admin).grid(column=1, row=1)
    def get_users(self):
        self.clear()
        for i, user in enumerate(users):
            Label(self.frm, text="ID: ").grid(column=0, row=i)
            Label(self.frm, text=user.get_id()).grid(column=1, row=i)
            Label(self.frm, text="Name: ").grid(column=2, row=i)
            Label(self.frm, text=user.get_name()).grid(column=3, row=i)
            Label(self.frm, text="Age: ").grid(column=4, row=i)
            Label(self.frm, text=user.get_age()).grid(column=5, row=i)
            Label(self.frm, text="Balance: ").grid(column=6, row=i)
            Label(self.frm, text=user.get_balance()).grid(column=7, row=i)
            Label(self.frm, text="Savings: ").grid(column=8, row=i)
            Label(self.frm, text=user.get_savings()).grid(column=9, row=i)
            Label(self.frm, text="Interest: ").grid(column=10, row=i)
            Label(self.frm, text=user.get_interest()).grid(column=11, row=i)
            self.id = user.get_id()
            Button(self.frm, text="Edit", command=self.edit_user).grid(column=12, row=i)
            Button(self.frm, text="Remove", command=self.remove_user).grid(column=13, row=i)
        Button(self.frm, text="Exit", command=self.__init__).grid(column=6)
    def add_user(self):
        self.clear()
        Label(self.frm, text="What is your name").grid(column=1, row=0)
        self.name = Entry(self.frm)
        self.name.grid(column=1, row=1)
        Label(self.frm, text="What is your age").grid(column=1, row=2)
        self.age = Entry(self.frm)
        self.age.grid(column=1, row=3)
        Button(self.frm, text="Add", command=self.add_user_tk).grid(column=1, row=5)
    def add_user_tk(self):
        id = len(users)
        users.append(account(id, self.name.get(), self.age.get()))
        self.__init__()
    def remove_user(self):
        users.pop(self.id)
        self.get_users()
    def edit_user(self):
        self.clear()
        Label(self.frm, text="User panel").grid(column=1, row=0)
        Button(self.frm, text="Add balance", command=self.edit_user_add_balance).grid(column=1, row=1)
        Button(self.frm, text="Remove balance", command=self.edit_user_remove_balance).grid(column=1, row=2)
        Button(self.frm, text="Add savings", command=self.edit_user_transfer_in_savings).grid(column=1, row=3)
        Button(self.frm, text="Remove savings", command=self.edit_user_transfer_out_savings).grid(column=1, row=4)
        Button(self.frm, text="Set interest", command=self.edit_user_set_interest).grid(column=1, row=5)
        Button(self.frm, text="Exit", command=self.__init__).grid(column=1, row=6)
    def edit_user_add_balance(self):
        self.clear()
        self.amount = Entry(self.frm)
        self.amount.grid(column=0, row=0)
        Button(self.frm, text="Add", command=self.edit_user_add_balance_tk).grid(column=0, row=1)
    def edit_user_add_balance_tk(self):
        users[self.id].add_balance(int(self.amount.get()))
        self.edit_user()
    def edit_user_remove_balance(self):
        self.clear()
        self.amount = Entry(self.frm)
        self.amount.grid(column=0, row=0)
        Button(self.frm, text="Remove", command=self.edit_user_remove_balance_tk).grid(column=0, row=1)
    def edit_user_remove_balance_tk(self):
        users[self.id].remove_balance(int(self.amount.get()))
        self.edit_user()
    def edit_user_transfer_in_savings(self):
        self.clear()
        self.amount = Entry(self.frm)
        self.amount.grid(column=0, row=0)
        Button(self.frm, text="Add", command=self.edit_user_transfer_in_savings_tk).grid(column=0, row=1)
    def edit_user_transfer_in_savings_tk(self):
        response = users[self.id].transfer_in_savings(int(self.amount.get()))
        self.clear()   
        if response == 1:
            Label(self.frm, text="You do not hold this amount in your balance").grid(column=1, row=0)
            Button(self.frm, text="Exit", command=self.edit_user).grid(column=1, row=1)
        else:
            Label(self.frm, text="Success! value transfered").grid(column=1, row=0)
            Button(self.frm, text="Exit", command=self.edit_user).grid(column=1, row=1)
    def edit_user_transfer_out_savings(self):
        self.clear()
        self.amount = Entry(self.frm)
        self.amount.grid(column=0, row=0)
        Button(self.frm, text="Remove", command=self.edit_user_transfer_out_savings_tk).grid(column=0, row=1)
    def edit_user_transfer_out_savings_tk(self):
        response = users[self.id].transfer_out_savings(int(self.amount.get()))
        self.clear()
        if response == 1:
            Label(self.frm, text="You do not hold this amount in your savings").grid(column=1, row=0)
            Button(self.frm, text="Exit", command=self.edit_user).grid(column=1, row=1)
        else:
            Label(self.frm, text="Success! value transfered").grid(column=1, row=0)
            Button(self.frm, text="Exit", command=self.edit_user).grid(column=1, row=1)
    def edit_user_set_interest(self):
        self.clear()
        self.amount = Entry(self.frm)
        self.amount.grid(column=0, row=0)
        Button(self.frm, text="Set", command=self.edit_user_set_interest_tk).grid(column=0, row=1)
    def edit_user_set_interest_tk(self):
        response = users[self.id].set_interest(int(self.amount.get()))
        self.clear()
        if response == 1:
            Label(self.frm, text="Are you sure that this is correct? > 1000% seems a lot").grid(column=1, row=0)
            Button(self.frm, text="Exit", command=self.edit_user).grid(column=1, row=1)
        else:
            Label(self.frm, text="Success! interest set").grid(column=1, row=0)
            Button(self.frm, text="Exit", command=self.edit_user).grid(column=1, row=1)
    def clear(self):
        self.frm.destroy()
        self.frm = Frame(self.root)
        self.frm.grid()
admin()