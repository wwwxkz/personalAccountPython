from classes.account import *
from classes.days import *
from classes.log import *

from tkinter import *

import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

users = []
class admin:
    widget_width = 30
    widget_height = 3
    def __init__(self):
        self.days = days()
        self.color_scheme('light')
        self.main()
    def main(self):
        self.root = Tk()
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.title("personalAccountPython")
        self.root.configure(bg=self.bg)
        self.root.state('zoomed')
        self.frm = Frame(self.root)
        self.frm.grid()
        self.control_panel()
    def control_panel(self):
        self.clear()
        e1 = Label(self.frm, text="Control Panel", width=self.widget_width, height=self.widget_height)
        e2 = Button(self.frm, text="Admin", command=self.admin_panel, width=self.widget_width, height=self.widget_height)
        e3 = Button(self.frm, text="Get Users", command=self.get_users, width=self.widget_width, height=self.widget_height)
        e4 = Button(self.frm, text="Add User", command=self.add_user, width=self.widget_width, height=self.widget_height)
        e5 = Button(self.frm, text="Increase Font", command=self.increase_font_size, width=self.widget_width, height=self.widget_height)
        e6 = Button(self.frm, text="Decrease Font", command=self.decrease_font_size, width=self.widget_width, height=self.widget_height)
        e7 = Button(self.frm, text="Dark Mode", command=self.theme_switch, width=self.widget_width, height=self.widget_height)
        e8 = Button(self.frm, text="Exit", command=self.safe_exit, width=self.widget_width, height=self.widget_height)
        el = [e1, e2, e3, e4, e5, e6, e7, e8]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
        self.root.mainloop()
    def increase_font_size(self):
        self.widget_width += 10
        self.widget_height += 1
        self.restart_tk()
    def decrease_font_size(self):
        self.widget_width -= 10
        self.widget_height -= 1
        self.restart_tk()
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
        e1 = Label(self.frm, text="Admin Control Panel", width=self.widget_width, height=self.widget_height)
        e2 = Button(self.frm, text="Delete logs", command=self.delete_logs, width=self.widget_width, height=self.widget_height)
        e3 = Button(self.frm, text="Delete accounts", command=self.delete_accounts, width=self.widget_width, height=self.widget_height)
        e4 = Button(self.frm, text="Pass day", command=self.pass_day, width=self.widget_width, height=self.widget_height)
        e5 = Button(self.frm, text="Log Analyzer", command=self.log_analyzer, width=self.widget_width, height=self.widget_height)
        e6 = Button(self.frm, text="Exit", command=self.control_panel, width=self.widget_width, height=self.widget_height)
        el = [e1, e2, e3, e4, e5, e6]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def delete_logs(self):
        self.clear()
        try:
            os.remove('personal_account_python_log.txt')
            os.remove('personal_account_python_log_backup.txt')
            e1 = Label(self.frm, text="Error! no logs found", width=self.widget_width, height=self.widget_height)
        except:
            e1 = Label(self.frm, text="Success! all logs have been deleted", width=self.widget_width, height=self.widget_height)
        e2 = Button(self.frm, text="Exit", command=self.admin_panel, width=self.widget_width, height=self.widget_height)
        el = [e1, e2]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def delete_accounts(self):
        self.clear()
        self.users = []
        e1 = Label(self.frm, text="Success! all accounts have been deleted", width=self.widget_width, height=self.widget_height)
        e2 = Button(self.frm, text="Exit", command=self.admin_panel, width=self.widget_width, height=self.widget_height)
        el = [e1, e2]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def pass_day(self):
        self.clear()
        self.days.pass_day(users)
        e1 = Label(self.frm, text="Success! day passed, and user yields updated", width=self.widget_width, height=self.widget_height)
        e2 = Button(self.frm, text="Exit", command=self.admin_panel, width=self.widget_width, height=self.widget_height)
        el = [e1, e2]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def get_users(self):
        self.clear()
        e1 = Label(self.frm, text="ID", width=self.widget_width, height=self.widget_height)
        e2 = Label(self.frm, text="Name", width=self.widget_width, height=self.widget_height)
        e3 = Label(self.frm, text="Age", width=self.widget_width, height=self.widget_height)
        e4 = Label(self.frm, text="Balance", width=self.widget_width, height=self.widget_height)
        e5 = Label(self.frm, text="Savings", width=self.widget_width, height=self.widget_height)
        e6 = Label(self.frm, text="Interest", width=self.widget_width, height=self.widget_height)
        e7 = Label(self.frm, text="", width=self.widget_width, height=self.widget_height)
        e8 = Label(self.frm, text="", width=self.widget_width, height=self.widget_height)
        el = [e1, e2, e3, e4, e5, e6, e7, e8]
        for i, widget in enumerate(el):
            widget.grid(column=i, row=0)
            widget.configure(bg=self.ac, fg=self.fg, borderwidth=1)
        for i, user in enumerate(users):
            e1 = Label(self.frm, text=user.get_id(), width=self.widget_width, height=self.widget_height)
            e2 = Label(self.frm, text=user.get_name(), width=self.widget_width, height=self.widget_height)
            e3 = Label(self.frm, text=user.get_age(), width=self.widget_width, height=self.widget_height)
            e4 = Label(self.frm, text=user.get_balance(), width=self.widget_width, height=self.widget_height)
            e5 = Label(self.frm, text=user.get_savings(), width=self.widget_width, height=self.widget_height)
            e6 = Label(self.frm, text=user.get_interest(), width=self.widget_width, height=self.widget_height)
            self.id = user.get_id()
            e7 = Button(self.frm, text="Edit", command=self.edit_user, width=self.widget_width, height=self.widget_height)
            e8 = Button(self.frm, text="Remove", command=self.remove_user, width=self.widget_width, height=self.widget_height)
            el = [e1, e2, e3, e4, e5, e6, e7, e8]
            for c, widget in enumerate(el):
                widget.grid(column=c, row=i+1)
                widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
        e1 = Button(self.frm, text="Exit", command=self.control_panel, width=self.widget_width, height=self.widget_height)
        e1.grid(column=4)
        e1.configure(bg=self.ac, fg=self.fg, borderwidth=1)
    def add_user(self):
        self.clear()
        e1 = Label(self.frm, text="What is your name", width=self.widget_width, height=self.widget_height)
        self.name = Entry(self.frm, width=self.widget_width)
        e2 = Label(self.frm, text="What is your age", width=self.widget_width, height=self.widget_height)
        self.age = Entry(self.frm, width=self.widget_width)
        e3 = Button(self.frm, text="Add", command=self.add_user_tk, width=self.widget_width, height=self.widget_height)
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
        e1 = Label(self.frm, text="User panel", width=self.widget_width, height=self.widget_height)
        e2 = Button(self.frm, text="Add balance", command=self.edit_user_add_balance, width=self.widget_width, height=self.widget_height)
        e3 = Button(self.frm, text="Remove balance", command=self.edit_user_remove_balance, width=self.widget_width, height=self.widget_height)
        e4 = Button(self.frm, text="Add savings", command=self.edit_user_transfer_in_savings, width=self.widget_width, height=self.widget_height)
        e5 = Button(self.frm, text="Remove savings", command=self.edit_user_transfer_out_savings, width=self.widget_width, height=self.widget_height)
        e6 = Button(self.frm, text="Set interest", command=self.edit_user_set_interest, width=self.widget_width, height=self.widget_height)
        e7 = Button(self.frm, text="Exit", command=self.control_panel, width=self.widget_width, height=self.widget_height)
        el = [e1, e2, e3, e4, e5, e6, e7]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def edit_user_add_balance(self):
        self.clear()
        self.amount = Entry(self.frm, width=self.widget_width)
        self.amount.grid(column=0, row=0)
        e1 = Button(self.frm, text="Add", command=self.edit_user_add_balance_tk, width=self.widget_width, height=self.widget_height)
        el = [self.amount, e1]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def edit_user_add_balance_tk(self):
        users[self.id].add_balance(int(self.amount.get()))
        self.edit_user()
    def edit_user_remove_balance(self):
        self.clear()
        self.amount = Entry(self.frm, width=self.widget_width)
        self.amount.grid(column=0, row=0)
        e1 = Button(self.frm, text="Remove", command=self.edit_user_remove_balance_tk, width=self.widget_width, height=self.widget_height)
        el = [self.amount, e1]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def edit_user_remove_balance_tk(self):
        users[self.id].remove_balance(int(self.amount.get()))
        self.edit_user()
    def edit_user_transfer_in_savings(self):
        self.clear()
        self.amount = Entry(self.frm, width=self.widget_width)
        self.amount.grid(column=0, row=0)
        e1 = Button(self.frm, text="Add", command=self.edit_user_transfer_in_savings_tk, width=self.widget_width, height=self.widget_height)
        el = [self.amount, e1]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def edit_user_transfer_in_savings_tk(self):
        response = users[self.id].transfer_in_savings(int(self.amount.get()))
        self.clear()   
        if response == 1:
            e1 = Label(self.frm, text="You do not hold this amount in your balance", width=self.widget_width, height=self.widget_height)
            e2 = Button(self.frm, text="Exit", command=self.edit_user, width=self.widget_width, height=self.widget_height)
        else:
            e1 = Label(self.frm, text="Success! value transfered", width=self.widget_width, height=self.widget_height)
            e2 = Button(self.frm, text="Exit", command=self.edit_user, width=self.widget_width, height=self.widget_height)
        el = [e1, e2]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def edit_user_transfer_out_savings(self):
        self.clear()
        self.amount = Entry(self.frm, width=self.widget_width)
        self.amount.grid(column=0, row=0)
        e1 = Button(self.frm, text="Remove", command=self.edit_user_transfer_out_savings_tk, width=self.widget_width, height=self.widget_height)
        el = [self.amount, e1]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def edit_user_transfer_out_savings_tk(self):
        response = users[self.id].transfer_out_savings(int(self.amount.get()))
        self.clear()
        if response == 1:
            e1 = Label(self.frm, text="You do not hold this amount in your savings", width=self.widget_width, height=self.widget_height)
            e2 = Button(self.frm, text="Exit", command=self.edit_user, width=self.widget_width, height=self.widget_height)
        else:
            e1 = Label(self.frm, text="Success! value transfered", width=self.widget_width, height=self.widget_height)
            e2 = Button(self.frm, text="Exit", command=self.edit_user, width=self.widget_width, height=self.widget_height)
        el = [e1, e2]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def edit_user_set_interest(self):
        self.clear()
        self.amount = Entry(self.frm, width=self.widget_width)
        self.amount.grid(column=0, row=0)
        e1 = Button(self.frm, text="Set", command=self.edit_user_set_interest_tk, width=self.widget_width, height=self.widget_height)
        el = [self.amount, e1]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def edit_user_set_interest_tk(self):
        response = users[self.id].set_interest(int(self.amount.get()))
        self.clear()
        if response == 1:
            e1 = Label(self.frm, text="Are you sure that this is correct? > 1000% seems a lot", width=self.widget_width, height=self.widget_height)
            e2 = Button(self.frm, text="Exit", command=self.edit_user, width=self.widget_width, height=self.widget_height)
        else:
            e1 = Label(self.frm, text="Success! interest set", width=self.widget_width, height=self.widget_height)
            e2 = Button(self.frm, text="Exit", command=self.edit_user, width=self.widget_width, height=self.widget_height)
        el = [e1, e2]
        for i, widget in enumerate(el):
            widget.grid(column=1, row=i)
            widget.configure(bg=self.bg, fg=self.fg, borderwidth=1)
    def log_analyzer(self):
        self.clear()
        logs = log.log_get()
        dates = []
        actions = []
        for log_line in logs:
            line = log_line.split(' - ')   
            dates.append(line[0])
            line.pop(0)
            actions.append(len(line))
        fig = Figure(figsize=(5, 4), dpi=100)
        fig.add_subplot(111).plot(dates, actions)
        canvas = FigureCanvasTkAgg(fig, master=self.frm)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(canvas, self.frm)
        toolbar.update()
        button = Button(master=self.frm, text="Exit", command=self.admin_panel, width=self.widget_width, height=self.widget_height)
        button.configure(bg=self.bg, fg=self.fg, borderwidth=1)
        button.pack(side=BOTTOM)
    def clear(self):
        self.frm.destroy()
        self.frm = Frame(self.root)
        self.frm.grid()
admin()