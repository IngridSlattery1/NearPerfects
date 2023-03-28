from math import sqrt
from sympy import divisors

def ispoweroftwo(n):  # Checks to see whether number is power of two
    if n == 0 or n == 1:
        return False
    while n != 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True


def checkprime(n):  # Checks to see whether number is prime
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n > 2:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True


def checkotherdivsior(d2new):  # Checking the other divisor (not a power of two) to see if its prime
    while d2new % 2 == 0 and d2new > 2:
        d2new = d2new / 2
    if checkprime(d2new):
        return True
    return False


def checkoriginalnumber(original):   # Checking original number to see whether it is  product of power of two and prime
    while original % 2 == 0:
        original = original / 2
    if checkprime(original):
        return True
    return False

def nearperfect2finder(w, x):
    for n in range(w, x + 1):
        if n != 1 and n % 10000 == 1:
            print("Just completed " + str(n-1))
        sig = sum(divisors(n))
        maxcheck = sig - 2 * n
        if maxcheck > 1:
            for d in divisors(n):
                    if d < int(maxcheck / 2) and maxcheck - d > 0 and n % (maxcheck - d) == 0 and (maxcheck - d) != d:
                        d2 = maxcheck - d
                        if ispoweroftwo(d) and ispoweroftwo(d2):   # Breaks code if both divisors are powers of 2
                            break
                        if ispoweroftwo(d):
                            if checkotherdivsior(d2):
                                if checkoriginalnumber(n):  # Checking all three requirements
                                    print(n, sig, d, d2)
                        elif ispoweroftwo(d2):
                            if checkotherdivsior(d):
                                if checkoriginalnumber(n):  # Checking all three requirements
                                    print(n, sig, d, d2)
    print("all done")

nearperfect2finder(0, 1000000)
