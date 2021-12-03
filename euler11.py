# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
#
# 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
#
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20×20 grid?
#
import sys

file = "assets/euler11.txt"


def extract_line(line: str) -> list[int]:
    modline = line.split(' ')
    rlist = []
    for i in modline:
        num = int(i)
        rlist.append(num)

    return rlist


def load_grid(filename=file) -> list[[]]:
    flist = []
    with open(filename, 'r') as f:
        lines = f.readlines()

    for i in lines:
        flist.append(extract_line(i))
    return flist


def print_grid(grid):
    for i in range(len(grid)):
        sys.stdout.write(f"{i}:\t")
        for k in range(len(grid[i])):
            sys.stdout.write(f"{grid[i][k]}\t")
        sys.stdout.write('\n')


def grab_adj(grid, rows=False, mutate=4) -> list[[]]:
    """

    :param grid: input grid to be evaluated
    :param mutate: number by which the selector will be mutated
    :param rows: True for selecting rows. False for selecting columns
    :return: 2 dimensional list of adjacent variables
    """
    lgrid = len(grid)
    rlist = []
    tlist = []

    for i in range(lgrid):
        for j in range(lgrid):
            if rows:
                if i + mutate <= lgrid:
                    for t in range(mutate):
                        tlist.append(grid[i + t][j])
                    rlist.append(tlist)
                    tlist = []
            else:
                if j + mutate <= lgrid:
                    for t in range(mutate):
                        tlist.append(grid[i][j + t])
                    rlist.append(tlist)
                    tlist = []
    return rlist


def grab_diag_adj(grid, right=False, mutate=4) -> list[[]]:
    """

    :param grid: input grid to be evaluated
    :param right: True for selecting Right adjacent False for selecting Left adjacent
    :param mutate: number by which the selector will be mutated
    :return: 2 dimensional list of adjacent variables
    """
    lgrid = len(grid)
    rlist = []
    tlist = []

    for i in range(lgrid):
        for j in range(lgrid):
            if right:
                if i + mutate <= lgrid and j + mutate <= lgrid:
                    for t in range(mutate):
                        tlist.append(grid[i + t][j + t])
                    rlist.append(tlist)
                    tlist = []
            else:
                if i + mutate <= lgrid and j - mutate >= 0:
                    for t in range(mutate):
                        tlist.append(grid[i + t][j - t])
                    rlist.append(tlist)
                    tlist = []
    return rlist


def calculate_possible(possible) -> int:
    ans = 1
    for i in range(len(possible)):
        ans *= possible[i]
    return ans


def calculate_greatest(possibles) -> int:
    greatest = 0
    for i in range(len(possibles)):
        t = calculate_possible(possibles[i])
        if greatest < t:
            print(greatest := t)
            print(f"{i}: {possibles[i]}")

    return greatest


def main():
    l = load_grid()

    ms = 40
    print(f"DOWN{'=' * ms}")
    print_grid(dug := grab_adj(l, rows=True))  # DOWN ADJACENT
    calculate_greatest(dug)

    print(f"LEFT{'=' * ms}")
    print_grid(lrg := grab_adj(l, rows=False))  # LEFT ADJACENT
    calculate_greatest(lrg)

    print(f"RIGHT DIAG{'=' * ms}")
    print_grid(drg := grab_diag_adj(l, right=True))
    calculate_greatest(drg)

    print(f"LEFT DIAG{'=' * ms}")
    print_grid(drg := grab_diag_adj(l, right=False))
    calculate_greatest(drg)

    print('\n')

    print_grid(l)


if __name__ == '__main__':
    main()
