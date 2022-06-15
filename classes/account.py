from classes.time import *

class account:
    def __init__(self, id, name, age):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__balance = 0
        self.__savings = 0
        self.__interest = 0
        log()
        log.log_new('Created user: ' +  self.__name + ' with ID: ' + str(self.__id))
    def add_balance(self, to_add):
        self.__balance += to_add
        log.log_new('Added balance to the user: ' +  self.__name + ' with ID: ' + str(self.__id))
    def remove_balance(self, to_remove):
        self.__balance -= to_remove
        log.log_new('Removed balance from the user: ' +  self.__name + ' with ID: ' + str(self.__id))
    def transfer_in_savings(self, to_add):
        if self.__balance >= to_add:
            self.__savings += to_add
            self.__balance -= to_add
            log.log_new('Transfered in savings user: ' +  self.__name + ' with ID: ' + str(self.__id))
        else:
            log.log_new('Tried to transfer in savings user: ' +  self.__name + ' with ID: ' + str(self.__id))
            return 1
    def transfer_out_savings(self, to_remove):
        if self.__savings >= to_remove:
            self.__savings -= to_remove
            self.__balance += to_remove
            log.log_new('Transfered out savings user: ' +  self.__name + ' with ID: ' + str(self.__id))
        else:
            log.log_new('Tried to transfer out savings user: ' +  self.__name + ' with ID: ' + str(self.__id))
            return 1
    def set_interest(self, to_set):
        if to_set <= 1000:
            self.__interest = to_set
            log.log_new('Set interest user: ' +  self.__name + ' with ID: ' + str(self.__id))
        else:
            log.log_new('Tried to set interest user: ' +  self.__name + ' with ID: ' + str(self.__id))
            return 1 
    def get_id(self):
        log.log_new('Get ID from user: ' +  self.__name + ' with ID: ' + str(self.__id))
        return self.__id
    def get_name(self):
        log.log_new('Get name user: ' +  self.__name + ' with ID: ' + str(self.__id))
        return self.__name
    def get_age(self):
        log.log_new('Get age user: ' +  self.__name + ' with ID: ' + str(self.__id))
        return self.__age
    def get_balance(self):
        log.log_new('Get balance user: ' +  self.__name + ' with ID: ' + str(self.__id))
        return self.__balance
    def get_savings(self):
        log.log_new('Get savings user: ' +  self.__name + ' with ID: ' + str(self.__id))
        return self.__savings
    def get_interest(self):
        log.log_new('Get interest user: ' +  self.__name + ' with ID: ' + str(self.__id))
        return self.__interest