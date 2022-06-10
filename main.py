from tkinter import *
from tkinter import ttk

users = []
class admin:
    root = Tk()
    frm = ttk.Frame(root, padding=40)
    frm.grid()
    def __init__(self):
        while True:
            self.clear()
            ttk.Label(self.frm, text="Admin Control Panel").grid(column=1, row=0)
            ttk.Button(self.frm, text="Get users", command=self.get_users).grid(column=1, row=1)
            ttk.Button(self.frm, text="Add user", command=self.add_user).grid(column=1, row=3)
            ttk.Button(self.frm, text="Exit", command=self.root.destroy).grid(column=1, row=5)
            self.root.mainloop()
    def get_users(self):
        self.clear()
        for i, user in enumerate(users):
            ttk.Label(self.frm, text="ID: ").grid(column=0, row=i)
            ttk.Label(self.frm, text=user.get_id()).grid(column=1, row=i)
            ttk.Label(self.frm, text="Name: ").grid(column=2, row=i)
            ttk.Label(self.frm, text=user.get_name()).grid(column=3, row=i)
            ttk.Label(self.frm, text="Age: ").grid(column=4, row=i)
            ttk.Label(self.frm, text=user.get_age()).grid(column=5, row=i)
            ttk.Label(self.frm, text="Balance: ").grid(column=6, row=i)
            ttk.Label(self.frm, text=user.get_balance()).grid(column=7, row=i)
            self.id = user.get_id()
            ttk.Button(self.frm, text="Edit", command=self.edit_user).grid(column=8, row=i)
            ttk.Button(self.frm, text="Remove", command=self.remove_user).grid(column=9, row=i)
        ttk.Button(self.frm, text="Exit", command=self.__init__).grid(column=5)
    def add_user(self):
        self.clear()
        ttk.Label(self.frm, text="What is your name").grid(column=1, row=0)
        self.name = ttk.Entry(self.frm)
        self.name.grid(column=1, row=1)
        ttk.Label(self.frm, text="What is your age").grid(column=1, row=2)
        self.age = ttk.Entry(self.frm)
        self.age.grid(column=1, row=3)
        ttk.Button(self.frm, text="Add", command=self.add_user_tk).grid(column=1, row=5)
    def add_user_tk(self):
        id = len(users)
        users.append(account(id, self.name.get(), self.age.get()))
        self.__init__()
    def remove_user(self):
        users.pop(self.id)
        self.get_users()
    def edit_user(self):
        self.clear()
        ttk.Label(self.frm, text="User panel").grid(column=1, row=0)
        ttk.Button(self.frm, text="Add balance", command=self.edit_user_add_balance).grid(column=1, row=1)
        ttk.Button(self.frm, text="Remove balance", command=self.edit_user_remove_balance).grid(column=1, row=2)
        ttk.Button(self.frm, text="Exit", command=self.__init__).grid(column=1, row=3)
    def edit_user_add_balance(self):
        self.clear()
        self.amount = ttk.Entry(self.frm)
        self.amount.grid(column=0, row=0)
        ttk.Button(self.frm, text="Add", command=self.edit_user_add_balance_tk).grid(column=0, row=1)
    def edit_user_add_balance_tk(self):
        users[self.id].add_balance(int(self.amount.get()))
        self.edit_user()
    def edit_user_remove_balance(self):
        self.clear()
        self.amount = ttk.Entry(self.frm)
        self.amount.grid(column=0, row=0)
        ttk.Button(self.frm, text="Remove", command=self.edit_user_remove_balance_tk).grid(column=0, row=1)
    def edit_user_remove_balance_tk(self):
        users[self.id].remove_balance(int(self.amount.get()))
        self.edit_user()
    def clear(self):
        self.frm.destroy()
        self.frm = ttk.Frame(self.root, padding=40)
        self.frm.grid()

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

admin()
