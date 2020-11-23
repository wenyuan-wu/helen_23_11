#!/usr/bin/env python3

import warnings

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.

class Fridge:
    def __init__(self):
        self.__storage = []

    def store(self, item):
        self.__storage.append(item)
        # print(f'{item} was added into fridge.')
        # print(f'The current storage: {self.__storage}')

    def take(self, item):
        try:
            self.__storage.remove(item)
            return item
        except ValueError:
            warnings.warn(f'{item} was not found in the fridge!')
        pass

    def find(self, name):
        for item in self.__storage:
            if name == item[1]:
                return item
        return None

    def take_before(self, date):
        take_list = []
        for item in self.__storage:
            if item[0] < date:
                take_list.append(item)
                self.__storage.remove(item)
        return take_list


    def __iter__(self):
        return iter(self.__storage)

    def __len__(self):
        return len(self.__storage)

    # To implement the required functionality, you will also have to implement several
    # of the special functions that typically include a double underscore.


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    l = ["a", "b", "c"]
    for i in l:
        l.remove(i)
        # print(l)

    f = Fridge()
    f.store((191127, "Butter"))
    f.store((191117, "Milk"))

    print("Items in the fridge:")
    for i in f:
        print("- {} ({})".format(i[1], i[0]))
    butter = f.find("Butter")
    print(butter)
    i = f.take((191127, "Butter"))
    f.take((201123, "Egg"))
    print("Removed {}, {} items left".format(i, len(f)))
    f.store((191128, "Egg"))
    f.store((191128, "Milk"))
    date = 191127
    print(f'thing taken out before {date}: {f.take_before(date)}')