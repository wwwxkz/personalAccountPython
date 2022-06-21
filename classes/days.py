from datetime import datetime
from classes.account import *

class days:
    def __init__(self):
        self.__day = 0
    def pass_day(self, users):
        self.__day += 1
        for user in users:
            savings_yield = user.get_savings() * (user.get_interest() / 100) + user.get_savings()
            user.set_savings(savings_yield)