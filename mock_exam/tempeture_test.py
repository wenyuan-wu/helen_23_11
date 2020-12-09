import random


class Temperature:
    def __init__(self, temp):
        self.__temp = temp

    def get_celsius(self):
        return self.__temp

    def get_fahrenheit(self):
        return '{:.2f}'.format(self.__temp * (9/5) + 32)


class Series:
    def __init__(self, list_len):
        self.list_len = list_len
        self.sum = 0

    def get_average_celsius(self):
        for i in self.list:
            self.sum += i
        return round(self.sum/len(self.list),2)

    def mockMeasurements(self):

        x = 0
        li = []
        while x < self:
            li.append(random.randint(36,42))
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