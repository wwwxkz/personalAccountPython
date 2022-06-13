class account:
    def __init__(self, id, name, age):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__balance = 0
        self.__savings = 0
        self.__interest = 0
    def add_balance(self, to_add):
        self.__balance += to_add
    def remove_balance(self, to_remove):
        self.__balance -= to_remove
    def transfer_in_savings(self, to_add):
        if self.__balance >= to_add:
            self.__savings += to_add
            self.__balance -= to_add
        else:
            return 1
    def transfer_out_savings(self, to_remove):
        if self.__savings >= to_remove:
            self.__savings -= to_remove
            self.__balance += to_remove
        else:
            return 1
    def set_interest(self, to_set):
        self.__interest = to_set 
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_balance(self):
        return self.__balance
    def get_savings(self):
        return self.__savings


