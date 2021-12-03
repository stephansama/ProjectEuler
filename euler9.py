#
# EULER 9
# *******
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#
import math

class Pythagorean:
    def __init__(self, a: int = 0, b: int = 0, c: int = 0):
        self.a = a
        self.b = b
        self.c = c

    # square functions
    @staticmethod
    def squared(num: int):
        return num ** 2

    def a_squared(self): return self.squared(self.a)
    def b_squared(self): return self.squared(self.b)
    def c_squared(self): return self.squared(self.c)

    def sum(self): return self.a + self.b + self.c

    # representation of
    # a < b < c
    def rule_one(self):
        if self.a < self.b < self.c:
            return True
        return False

    # representation of:
    # a^2 + b^2 == c^2
    def rule_two(self):
        if (self.a_squared() + self.b_squared()) == self.c_squared():
            return True
        return False

    # combines both rules to determine if the object is valid
    def is_valid(self):
        if self.rule_one():
            if self.rule_two():
                return True
        return False

    def calc_c(self):
        if not self.a | self.b:
            return False

        t = self.a_squared() + self.b_squared()
        self.c = math.sqrt(t)
        if not self.c.is_integer():
            self.c = 0  # remove new value
            return False
        self.c = int(self.c)

        return self.c


def test(v):
    t = Pythagorean(1, 1, 1)
    for i in range(25000):
        t.b += 1
        if t.b - t.a > v:
            t.a += 1
        if t.calc_c():
            if t.sum() == 1000:
                print(f"A: {t.a} B: {t.b} C: {t.c} = {t.sum()}")
                print('***********FOUND THE OBJECT!!!!!!!!!!!!!!')
                print(t.a * t.b * t.c)

def main():
    for i in range(250):
        test(i)


# 180,625 = 425^2
# 40,000 = 200^2
# 140,625 = 375^2


if __name__ == '__main__':
    main()
