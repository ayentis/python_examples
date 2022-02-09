class AccountException(Exception):
    pass

class Account:
    def __init__(self, number):
        self.__balance = 0
        self.__number = number
        pass

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise AccountException('Can not set negative value')

        if abs(self.__balance - value) > 100_000:
            print('This operation will be audited')

        self.__balance = value

    @balance.deleter
    def balance(self):
        if self.__balance > 0:
            raise AccountException('Can not delete account as long it is not empty')
        self.__balance = None

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        raise AccountException('Invalid operation')

    @number.deleter
    def number(self):
        raise AccountException('Invalid operation')

    def __str__(self):
        return 'Account #{} balance is {}'.format(self.__number, self.__balance)

account = Account('34-6514-7654-9999-0002')
account.balance += 1000
print(account)

try:
    account.balance = -200
except AccountException as e:
    print('Exception detected:', e)

try:
    account.number = 'a new one'
except AccountException as e:
    print('Exception detected:', e)

try:
    account.balance += 1_000_000
except AccountException as e:
    print('Exception detected:', e)

try:
    del account.balance
except AccountException as e:
    print('Exception detected:', e)
