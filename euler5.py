# EULER 5
# *******
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#

def generate_list(last: int) -> list[int]:
    lint = []
    for i in range(last):
        lint.append(i + 1)
    return lint

def main():
    ...


if __name__ == '__main__':
    main()
