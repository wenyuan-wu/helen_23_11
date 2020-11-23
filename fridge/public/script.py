#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.
class Fridge:

    def store(self, item):
        pass

    def take(self, item):
        pass

    def find(self, name):
        pass

    def take_before(self, date):
        pass

    # To implement the required functionality, you will also have to implement several
    # of the special functions that typically include a double underscore.


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    l = ["a", "b", "c"]
    for i in l:
        l.remove(i)

    f = Fridge()
    f.store((191127, "Butter"))
    f.store((191117, "Milk"))

    print("Items in the fridge:")
    for i in f:
        print("- {} ({})".format(i[1], i[0]))

    i = f.take((191127, "Butter"))
    print("Removed {}, {} items left".format(i, len(f)))
