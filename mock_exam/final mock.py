def lists_to_dict(keys, values):
    dict_1 = dict.fromkeys(keys)
    for idx,i in enumerate(keys):
        if keys.count(i) != 1:
            raise ValueError
        else:

            for idxx,x in enumerate(values):
                dict_1[i] = x
                if idx+1 >= len(keys) :
                    break
                else:
                    i = keys[idx+1]

        return dict_1
print(lists_to_dict([2, 1], ["b", "a"]))
print(lists_to_dict(["z", "y"], [10, 20]))

import random
class Temperature:
    def __init__(self,tem):
        self.__tem = tem
    def get_celsius(self):
        return self.__tem
    def get_fahrenheit(self):
        return '{:.2f}'.format(self.__tem*(9/5)+32)


class Series:
    def __init__(self, list):
        self.list = list
        self.sum = 0

    def get_average_celsius(self):
        for i in self.list:
            self.sum += i.get_celsius()
        return round(self.sum/len(self.list),2)

    def mockMeasurements(self):

        x = 0
        li = []
        while x < self:
            li.append(Temperature(random.randint(36,42)))
            x += 1
        return li



t = Temperature(39)
print(t.get_celsius())
print(t.get_fahrenheit())
ms = Series.mockMeasurements(3)
print(ms)
print(len(ms))
ms.append(t)
s = Series(ms)
print(ms)
print(s.get_average_celsius())
import unittest

class Account:
    def __init__(self,name):
        self.name = name
        self.__balance = 0

    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount1):
        self.__balance -= amount1
        if amount1 > self.available():
            raise ValueError
    def balance(self):
        return self.__balance
    def available(self):
        return self.__balance


class OverdrawAccount(Account):
    def __init__(self, name,amount):
        super().__init__(name)
        self.__amount = amount
        self.__balance = 0
        self.name = name
    def withdraw(self, money):
        self.__balance -= money
        if money > self.available():
            raise ValueError
        return self.__balance
    def balance(self):
        return self.__balance
    def available(self):
        return self.__amount + self.__balance


class Bank(Account):
    def __init__(self,name):
        super().__init__(name)
        self.__list = []
        self.__psum = 0
        self.__nsum = 0

    def add_account(self,account):
        self.__list.append(account)


    def get_balances(self):
        for i in self.__list:
            if i.balance() >= 0:
                self.__psum += i.balance()
            elif i.balance() < 0:
                self.__nsum += i.balance()
        return (self.__psum,self.__nsum)




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
        ao = OverdrawAccount('John',50)
        self.assertEqual(ao.available(), 50)

    def test_fail_overdraw(self):
        w = Account('John Doe')
        w.deposit(20)
        self.assertEqual(w.withdraw(30),ValueError)



a1 = Account("Gordon Freeman")
a1.deposit(30)
assert(a1.balance() == 30)
assert(a1.available() == 30)
a2 = OverdrawAccount("John Freeman", 500)
a2.withdraw(50)
assert(a2.balance() == -50)
assert(a2.available() == 450)
a3 = Account("Barney Calhoun")
a3.deposit(200)
b = Bank("Black Mesa")
b.add_account(a1)
b.add_account(a2)
b.add_account(a3)
assert(b.get_balances() == (230, -50))

unittest.main()


