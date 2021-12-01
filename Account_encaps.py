class Account:
    def __init__(self, id, balance, pin):
        self.id = id
        self.balance = balance
        self.pin = pin

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        self.__pin = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def get_id(self, new_pin):
        if new_pin == self.pin:
            return self.id
        return "Wrong pin"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            return 'Pin changed'
        return 'Wrong pin'


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))