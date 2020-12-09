import unittest


class Account:
    def __init__(self, name):
        self.name = name
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount
        if amount > self.__balance:
            raise ValueError
        return self.__balance

    def balance(self):
        return self.__balance

    def available(self):
        return self.__balance


class OverdrawAccount(Account):
    def __init__(self, name, amount):
        super().__init__(name)
        self.__amount = amount
        self.__balance = 0

    def withdraw(self, money):
        self.__balance -= money
        if money > self.available():
            raise ValueError
        return self.__balance

    def available(self):
        return self.__amount + self.__balance


class Bank(Account):
    def __init__(self, name):
        super().__init__(name)
        self.__list = []
        self.__psum = 0
        self.__nsum = 0

    def add_account(self, account):
        self.__list.append(account)

    def get_balances(self):
        for i in self.__list:
            if i.balance() >= 0:
                self.__psum += i.balance()
            elif i.balance() < 0:
                self.__nsum += i.balance()
        return self.__psum, self.__nsum


class AccountTest(unittest.TestCase):
    def test_deposit(self):
        acc = Account("John Doe")
        acc.deposit(30)
        self.assertEqual(acc.available(), 30)

    def test_withdraw(self):
        w = Account('John Doe')
        w.deposit(20)
        w.withdraw(10)
        self.assertEqual(w.available(), 10)

    def test_available_overdraw(self):
        ao = OverdrawAccount('John', 50)
        self.assertEqual(ao.available(), 50)

    def test_fail_overdraw(self):
        w = Account('John Doe')
        w.deposit(20)
        self.assertEqual(w.withdraw(30), ValueError)


unittest.main()
