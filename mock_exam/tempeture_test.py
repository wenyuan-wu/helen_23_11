import random


class Temperature:
    def __init__(self, degree: float):
        self.__degree = degree

    def get_celsius(self):
        return self.__degree

    def get_fahrenheit(self):
        return round((self.__degree * (9/5) + 32), 2)


class Series:
    def __init__(self, temp_list: [Temperature]):
        self.temp_list = temp_list

    def get_average_celsius(self):
        degree_sum = 0
        for i in self.temp_list:
            degree_sum += i.get_celsius()
        return round(degree_sum/len(self.temp_list), 2)

    @staticmethod
    def mockMeasurements(n):
        temp_list = []
        for i in range(0, n):
            temp_list.append(Temperature(random.randint(36, 42)))
            i += 1
        return temp_list


t = Temperature(39)
assert(t.get_celsius() == 39)
assert(t.get_fahrenheit() == 102.20)
ms = Series.mockMeasurements(3)
assert(len(ms) == 3)
ms.append(t)
s = Series(ms)
assert(36 <= s.get_average_celsius() <= 42)
