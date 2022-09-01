'''
    This file was created with the intention of testing the speed
    differences of the different ways of adding values to a list.

    The methods tested in this scenario were done by having a range
    from MIN_NUM to MAX_NUM, then performing exponentiation on each
    value in the range. The timing will begin just before the start
    of each method, and stops when it ends.

    The methods tested here are list comprehensions, array computations,
    for loops, and maps.
'''

import time

MIN_NUM = 1
MAX_NUM = 10000000

mylist3 = []

def give_exponent(n):
    return n**2

# List comprehension [n for n in range(1, 10)]
start = time.time()
mylist = [n**2 for n in range(MIN_NUM, MAX_NUM)]
end = time.time()
print("list comprehension:", end - start, "seconds")

# Array computation [list()]
start = time.time()
mylist2 = list(n**2 for n in range(MIN_NUM, MAX_NUM))
end = time.time()
print("array computation:", end - start, "seconds")

# For loop [for i in range(1, 10)]
start = time.time()
for n in range(MIN_NUM, MAX_NUM):
    mylist3.append(n**2)
end = time.time()
print("for loop:", end - start, "seconds")

# Map [map(cb, range)]
start = time.time()
mylist4 = list(map(give_exponent, range(MIN_NUM, MAX_NUM)))
end = time.time()
print("map:", end - start, "seconds")
