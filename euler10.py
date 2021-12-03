# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
# ANS
# 142913828922

def is_prime(num: int) -> bool:
    for i in range(num):
        # Divide the number by 1 through the number
        # if the number is not itself or one then it is not a prime
        if num % (i+1) == 0 and (i+1) != num and (i+1) != 1:
            return False
    return True

def find_primes(_max: int) -> list[int]:
    t = []  # temporary list
    for i in range(_max):
        if is_prime(i):
            print(i)
            t.append(i)
    return t[2:]  # remove the first two elements (0,1)

def main():
    print(is_prime(8))
    # f = find_primes(2_000_000)
    # printx


if __name__ == '__main__':
    main()
