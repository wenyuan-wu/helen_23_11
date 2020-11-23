#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.
class MagicDrawingBoard:
    def __init__(self, x, y):
        pass

    def reset(self):
        pass

    def pixel(self, xy):
        pass

    def rect(self, start_xy, end_xy):
        pass

    def img(self):
        pass


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    db = MagicDrawingBoard(6, 4)
    db.pixel((1, 1))
    db.rect((2, 2), (5, 4))
    print("After drawing:")
    print(db.img())
    db.reset()
    print("After resetting:")
    print(db.img())
