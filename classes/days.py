from datetime import datetime
from classes.account import *

class days:
    def __init__(self):
        self.__day = 0
        self.__day_start = datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
    def pass_day(self, users):
        self.__day += 1
        print('Day now is: ', self.__day)
        for user in users:
            savings_yield = user.get_savings() * (user.get_interest() / 100) + user.get_savings()
            user.set_savings(savings_yield)