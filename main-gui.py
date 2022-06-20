from classes.account import *
from classes.days import *
from classes.log import *

from tkinter import *

import os

users = []
class admin:
    root = Tk()
    Grid.grid_columnconfigure(root, 0, weight=1)
    Grid.grid_rowconfigure(root, 0, weight=1)
    root.title("personalAccountPython")
    root.geometry("600x600")
    def __init__(self):
        self.days = days()
        while True:
            self.clear()
            e1 = Label(self.root, text="Control Panel")
            e2 = Button(self.root, text="Admin", command=self.admin)
            e3 = Button(self.root, text="Get users", command=self.get_users)
            e4 = Button(self.root, text="Add user", command=self.add_user)
            e5 = Button(self.root, text="Exit", command=self.safe_exit)
            el = [e1, e2, e3, e4, e5]
            i=0
            for element in el:
                Grid.rowconfigure(self.root, i, weight=1)
                element.grid(row=i, column=0, pady=5, padx=5, sticky= "nsew")
                i+=1
            self.root.mainloop()
    def safe_exit(self):
        self.root.destroy()
        log()
    def admin(self):
        self.clear()
        e1 = Label(self.root, text="Admin Control Panel")
        e2 = Button(self.root, text="Delete logs", command=self.delete_logs)
        e3 = Button(self.root, text="Delete accounts", command=self.delete_accounts)
        e4 = Button(self.root, text="Pass day", command=self.pass_day)
        e5 = Button(self.root, text="Exit", command=self.__init__)
        el = [e1, e2, e3, e4, e5]
        i=0
        for element in el:
            Grid.rowconfigure(self.root, i, weight=1)
            element.grid(row=i, column=0, pady=5, padx=5, sticky= "nsew")
            i+=1
    def delete_logs(self):
        self.clear()
        try:
            os.remove('personal_account_python_log.txt')
            os.remove('personal_account_python_log_backup.txt')
            e1 = Label(self.root, text="Success! all logs have been deleted")
        except:
            e1 = Label(self.root, text="Error! no logs found")
        e2 = Button(self.root, text="Exit", command=self.admin)
        el = [e1, e2]
        i=0
        for element in el:
            Grid.rowconfigure(self.root, i, weight=1)
            element.grid(row=i, column=0, pady=5, padx=5, sticky= "nsew")
            i+=1
    def delete_accounts(self):
        self.clear()
        self.users = []
        e1 = Label(self.root, text="Success! all accounts have been deleted")
        e2 = Button(self.root, text="Exit", command=self.admin)
        el = [e1, e2]
        i=0
        for element in el:
            Grid.rowconfigure(self.root, i, weight=1)
            element.grid(row=i, column=0, pady=5, padx=5, sticky= "nsew")
            i+=1
    def pass_day(self):
        self.clear()
        self.days.pass_day(users)
        e1 = Label(self.root, text="Success! day passed, and user yields updated")
        e2 = Button(self.root, text="Exit", command=self.admin)
        el = [e1, e2]
        i=0
        for element in el:
            Grid.rowconfigure(self.root, i, weight=1)
            element.grid(row=i, column=0, pady=5, padx=5, sticky= "nsew")
            i+=1
    def get_users(self):
        self.clear()
        for i, user in enumerate(users):
            e1 = Label(self.root, text="ID: ")
            e2 = Label(self.root, text=user.get_id())
            e3 = Label(self.root, text="Name: ")
            e4 = Label(self.root, text=user.get_name())
            e5 = Label(self.root, text="Age: ")
            e6 = Label(self.root, text=user.get_age())
            e7 = Label(self.root, text="Balance: ")
            e8 = Label(self.root, text=user.get_balance())
            e9 = Label(self.root, text="Savings: ")
            e10 = Label(self.root, text=user.get_savings())
            e11 = Label(self.root, text="Interest: ")
            e12 = Label(self.root, text=user.get_interest())
            self.id = user.get_id()
            e13 = Button(self.root, text="Edit", command=self.edit_user)
            e14 = Button(self.root, text="Remove", command=self.remove_user)
            el = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14]
            c=0
            for element in el:
                Grid.grid_columnconfigure(self.root, c, weight=1)
                element.grid(row=i, column=c, padx=5, sticky= "nsew")
                c+=1
        e15 = Button(self.root, text="Exit", command=self.__init__)
        Grid.grid_columnconfigure(self.root, 7, weight=1)
        e15.grid(column=7, sticky= "nsew")
    def add_user(self):
        self.clear()
        e1 = Label(self.root, text="What is your name")
        e1.grid(row=0, column=0, pady=5, padx=5, sticky= "nsew")
        self.name = Entry(self.root)
        self.name.grid(row=1, column=0, pady=5, padx=5, sticky= "nsew")
        e2 = Label(self.root, text="What is your age")
        e2.grid(row=2, column=0, pady=5, padx=5, sticky= "nsew")
        self.age = Entry(self.root)
        self.age.grid(row=3, column=0, pady=5, padx=5, sticky= "nsew")
        e3 = Button(self.root, text="Add", command=self.add_user_tk)
        e3.grid(row=5, column=0, pady=5, padx=5, sticky= "nsew")
    def add_user_tk(self):
        id = len(users)
        users.append(account(id, self.name.get(), self.age.get()))
        self.__init__()
    def remove_user(self):
        users.pop(self.id)
        self.get_users()
    def edit_user(self):
        self.clear()
        e1 = Label(self.root, text="User panel")
        e2 = Button(self.root, text="Add balance", command=self.edit_user_add_balance)
        e3 = Button(self.root, text="Remove balance", command=self.edit_user_remove_balance)
        e4 = Button(self.root, text="Add savings", command=self.edit_user_transfer_in_savings)
        e5 = Button(self.root, text="Remove savings", command=self.edit_user_transfer_out_savings)
        e6 = Button(self.root, text="Set interest", command=self.edit_user_set_interest)
        e7 = Button(self.root, text="Exit", command=self.__init__)
        el = [e1, e2, e3, e4, e5, e6, e7]
        i=0
        for element in el:
            Grid.rowconfigure(self.root, i, weight=1)
            element.grid(row=i, column=0, pady=5, padx=5, sticky= "nsew")
            i+=1
    def edit_user_add_balance(self):
        self.clear()
        self.amount = Entry(self.root)
        Grid.rowconfigure(self.root, 0, weight=1)
        self.amount.grid(row=0, column=0, pady=5, padx=5, sticky= "nsew")
        e1 = Button(self.root, text="Add", command=self.edit_user_add_balance_tk)
        Grid.rowconfigure(self.root, 1, weight=1)
        e1.grid(row=1, column=0, pady=5, padx=5, sticky= "nsew")
    def edit_user_add_balance_tk(self):
        users[self.id].add_balance(int(self.amount.get()))
        self.edit_user()
    def edit_user_remove_balance(self):
        self.clear()
        self.amount = Entry(self.root)
        Grid.rowconfigure(self.root, 0, weight=1)
        self.amount.grid(row=0, column=0, pady=5, padx=5, sticky= "nsew")
        e1 = Button(self.root, text="Remove", command=self.edit_user_remove_balance_tk)
        Grid.rowconfigure(self.root, 1, weight=1)
        e1.grid(row=1, column=0, pady=5, padx=5, sticky= "nsew")
    def edit_user_remove_balance_tk(self):
        users[self.id].remove_balance(int(self.amount.get()))
        self.edit_user()
    def edit_user_transfer_in_savings(self):
        self.clear()
        self.amount = Entry(self.root)
        Grid.rowconfigure(self.root, 0, weight=1)
        self.amount.grid(row=0, column=0, pady=5, padx=5, sticky= "nsew")
        e1 = Button(self.root, text="Add", command=self.edit_user_transfer_in_savings_tk)
        Grid.rowconfigure(self.root, 1, weight=1)
        e1.grid(row=1, column=0, pady=5, padx=5, sticky= "nsew")
    def edit_user_transfer_in_savings_tk(self):
        response = users[self.id].transfer_in_savings(int(self.amount.get()))
        self.clear()   
        if response == 1:
            e1 = Label(self.root, text="You do not hold this amount in your balance")
            e2 = Button(self.root, text="Exit", command=self.edit_user)
        else:
            e1 = Label(self.root, text="Success! value transfered")
            e2 = Button(self.root, text="Exit", command=self.edit_user)
        el = [e1, e2]
        i=0
        for element in el:
            Grid.rowconfigure(self.root, i, weight=1)
            element.grid(row=i, column=0, pady=5, padx=5, sticky= "nsew")
            i+=1
    def edit_user_transfer_out_savings(self):
        self.clear()
        self.amount = Entry(self.root)
        self.amount.grid(row=0, column=0, pady=5, padx=5, sticky= "nsew")
        e1 = Button(self.root, text="Remove", command=self.edit_user_transfer_out_savings_tk)
        Grid.rowconfigure(self.root, 1, weight=1)
        e1.grid(row=1, column=0, pady=5, padx=5, sticky= "nsew")
    def edit_user_transfer_out_savings_tk(self):
        response = users[self.id].transfer_out_savings(int(self.amount.get()))
        self.clear()
        if response == 1:
            e1 = Label(self.root, text="You do not hold this amount in your savings")
            e2 = Button(self.root, text="Exit", command=self.edit_user)
        else:
            e1 = Label(self.root, text="Success! value transfered")
            e2 = Button(self.root, text="Exit", command=self.edit_user)
        el = [e1, e2]
        i=0
        for element in el:
            Grid.rowconfigure(self.root, i, weight=1)
            element.grid(row=i, column=0, pady=5, padx=5, sticky= "nsew")
            i+=1
    def edit_user_set_interest(self):
        self.clear()
        self.amount = Entry(self.root)
        self.amount.grid(row=0, column=0, pady=5, padx=5, sticky= "nsew")
        e1 = Button(self.root, text="Set", command=self.edit_user_set_interest_tk)
        Grid.rowconfigure(self.root, 1, weight=1)
        e1.grid(row=1, column=0, pady=5, padx=5, sticky= "nsew")
    def edit_user_set_interest_tk(self):
        response = users[self.id].set_interest(int(self.amount.get()))
        self.clear()
        if response == 1:
            e1 = Label(self.root, text="Are you sure that this is correct? > 1000% seems a lot")
            e2 = Button(self.root, text="Exit", command=self.edit_user)
        else:
            e1 = Label(self.root, text="Success! interest set")
            e2 = Button(self.root, text="Exit", command=self.edit_user)
        el = [e1, e2]
        i=0
        for element in el:
            Grid.rowconfigure(self.root, i, weight=1)
            element.grid(row=i, column=0, pady=5, padx=5, sticky= "nsew")
            i+=1
    def clear(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()
admin()