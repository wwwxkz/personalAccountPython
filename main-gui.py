from classes.account import *
from classes.days import *
from classes.log import *

from tkinter import *

import os

users = []
class admin:
    def __init__(self):
        self.days = days()
        self.color_scheme('dark')
        self.main()
    def main(self):
        self.root = Tk()
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.title("personalAccountPython")
        self.root.geometry("600x300")
        self.root.configure(bg=self.bg)
        self.frm = Frame(self.root)
        self.frm.grid()
        self.control_panel()
    def control_panel(self):
        while True:
            self.clear()
            e1 = Label(self.frm, text="Control Panel")
            e2 = Button(self.frm, text="Admin", command=self.admin_panel)
            e3 = Button(self.frm, text="Get users", command=self.get_users)
            e4 = Button(self.frm, text="Add user", command=self.add_user)
            e5 = Button(self.frm, text="Dark/Light mode", command=self.theme_switch)
            e6 = Button(self.frm, text="Exit", command=self.safe_exit)
            el = [e1, e2, e3, e4, e5, e6]
            for i, widget in enumerate(el):
                widget.grid(column=1, row=i)
                widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
            self.root.mainloop()
    def color_scheme(self, mode):
        if mode == 'dark':
            self.bg, self.fg, self.ac = ('#2b2b2b', 'white', '#69cfe0')
        if mode == 'light':
            self.bg, self.fg, self.ac = ('#ededed', 'black', '#72c491')
    def restart_tk(self):
        self.root.destroy()
        self.main()
    def theme_switch(self):
        if self.bg == '#2b2b2b':
            self.color_scheme('light')
            self.theme_btn_text = 'Dark Theme'
        elif self.bg == '#ededed':
            self.color_scheme('dark')
            self.theme_btn_text = 'Light Theme'
        self.restart_tk()
    def safe_exit(self):
        log()
        self.root.destroy()
    def admin_panel(self):
        self.clear()
        e1 = Label(self.frm, text="Admin Control Panel")
        e2 = Button(self.frm, text="Delete logs", command=self.delete_logs)
        e3 = Button(self.frm, text="Delete accounts", command=self.delete_accounts)
        e4 = Button(self.frm, text="Pass day", command=self.pass_day)
        e5 = Button(self.frm, text="Exit", command=self.control_panel)
        el = [e1, e2, e3, e4, e5]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def delete_logs(self):
        self.clear()
        try:
            os.remove('personal_account_python_log.txt')
            os.remove('personal_account_python_log_backup.txt')
            e1 = Label(self.frm, text="Error! no logs found")
        except:
            e1 = Label(self.frm, text="Success! all logs have been deleted")
        e2 = Button(self.frm, text="Exit", command=self.admin_panel)
        el = [e1, e2]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def delete_accounts(self):
        self.clear()
        self.users = []
        e1 = Label(self.frm, text="Success! all accounts have been deleted")
        e2 = Button(self.frm, text="Exit", command=self.admin_panel)
        el = [e1, e2]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def pass_day(self):
        self.clear()
        self.days.pass_day(users)
        e1 = Label(self.frm, text="Success! day passed, and user yields updated")
        e2 = Button(self.frm, text="Exit", command=self.admin_panel)
        el = [e1, e2]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def get_users(self):
        self.clear()
        for i, user in enumerate(users):
            e1 = Label(self.frm, text="ID: ")
            e2 = Label(self.frm, text=user.get_id())
            e3 = Label(self.frm, text="Name: ")
            e4 = Label(self.frm, text=user.get_name())
            e5 = Label(self.frm, text="Age: ")
            e6 = Label(self.frm, text=user.get_age())
            e7 = Label(self.frm, text="Balance: ")
            e8 = Label(self.frm, text=user.get_balance())
            e9 = Label(self.frm, text="Savings: ")
            e10 = Label(self.frm, text=user.get_savings())
            e11 = Label(self.frm, text="Interest: ")
            e12 = Label(self.frm, text=user.get_interest())
            self.id = user.get_id()
            e13 = Button(self.frm, text="Edit", command=self.edit_user)
            e14 = Button(self.frm, text="Remove", command=self.remove_user)
            el = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14]
            for i, widget in enumerate(el):
                widget.grid(column=i, row=1)
                widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
        e1 = Button(self.frm, text="Exit", command=self.control_panel)
        e1.grid(column=7)
        e1.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def add_user(self):
        self.clear()
        e1 = Label(self.frm, text="What is your name")
        self.name = Entry(self.frm)
        e2 = Label(self.frm, text="What is your age")
        self.age = Entry(self.frm)
        e3 = Button(self.frm, text="Add", command=self.add_user_tk)
        el = [e1, self.name, e2, self.age, e3]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def add_user_tk(self):
        id = len(users)
        users.append(account(id, self.name.get(), self.age.get()))
        self.control_panel()
    def remove_user(self):
        users.pop(self.id)
        self.get_users()
    def edit_user(self):
        self.clear()
        e1 = Label(self.frm, text="User panel")
        e2 = Button(self.frm, text="Add balance", command=self.edit_user_add_balance)
        e3 = Button(self.frm, text="Remove balance", command=self.edit_user_remove_balance)
        e4 = Button(self.frm, text="Add savings", command=self.edit_user_transfer_in_savings)
        e5 = Button(self.frm, text="Remove savings", command=self.edit_user_transfer_out_savings)
        e6 = Button(self.frm, text="Set interest", command=self.edit_user_set_interest)
        e7 = Button(self.frm, text="Exit", command=self.control_panel)
        el = [e1, e2, e3, e4, e5, e6, e7]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def edit_user_add_balance(self):
        self.clear()
        self.amount = Entry(self.frm)
        self.amount.grid(column=0, row=0)
        e1 = Button(self.frm, text="Add", command=self.edit_user_add_balance_tk)
        el = [self.amount, e1]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def edit_user_add_balance_tk(self):
        users[self.id].add_balance(int(self.amount.get()))
        self.edit_user()
    def edit_user_remove_balance(self):
        self.clear()
        self.amount = Entry(self.frm)
        self.amount.grid(column=0, row=0)
        e1 = Button(self.frm, text="Remove", command=self.edit_user_remove_balance_tk)
        el = [self.amount, e1]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def edit_user_remove_balance_tk(self):
        users[self.id].remove_balance(int(self.amount.get()))
        self.edit_user()
    def edit_user_transfer_in_savings(self):
        self.clear()
        self.amount = Entry(self.frm)
        self.amount.grid(column=0, row=0)
        e1 = Button(self.frm, text="Add", command=self.edit_user_transfer_in_savings_tk)
        el = [self.amount, e1]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def edit_user_transfer_in_savings_tk(self):
        response = users[self.id].transfer_in_savings(int(self.amount.get()))
        self.clear()   
        if response == 1:
            e1 = Label(self.frm, text="You do not hold this amount in your balance")
            e2 = Button(self.frm, text="Exit", command=self.edit_user)
        else:
            e1 = Label(self.frm, text="Success! value transfered")
            e2 = Button(self.frm, text="Exit", command=self.edit_user)
        el = [e1, e2]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def edit_user_transfer_out_savings(self):
        self.clear()
        self.amount = Entry(self.frm)
        self.amount.grid(column=0, row=0)
        e1 = Button(self.frm, text="Remove", command=self.edit_user_transfer_out_savings_tk)
        el = [self.amount, e1]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def edit_user_transfer_out_savings_tk(self):
        response = users[self.id].transfer_out_savings(int(self.amount.get()))
        self.clear()
        if response == 1:
            e1 = Label(self.frm, text="You do not hold this amount in your savings")
            e2 = Button(self.frm, text="Exit", command=self.edit_user)
        else:
            e1 = Label(self.frm, text="Success! value transfered")
            e2 = Button(self.frm, text="Exit", command=self.edit_user)
        el = [e1, e2]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def edit_user_set_interest(self):
        self.clear()
        self.amount = Entry(self.frm)
        self.amount.grid(column=0, row=0)
        e1 = Button(self.frm, text="Set", command=self.edit_user_set_interest_tk)
        el = [self.amount, e1]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def edit_user_set_interest_tk(self):
        response = users[self.id].set_interest(int(self.amount.get()))
        self.clear()
        if response == 1:
            e1 = Label(self.frm, text="Are you sure that this is correct? > 1000% seems a lot")
            e2 = Button(self.frm, text="Exit", command=self.edit_user)
        else:
            e1 = Label(self.frm, text="Success! interest set")
            e2 = Button(self.frm, text="Exit", command=self.edit_user)
        el = [e1, e2]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def clear(self):
        self.frm.destroy()
        self.frm = Frame(self.root)
        self.frm.grid()
admin()