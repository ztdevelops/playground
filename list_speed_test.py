import time

MIN_NUM = 1
MAX_NUM = 10000000

mylist3 = []

def give_exponent(n):
    return n**2

start = time.time()
mylist = [n**2 for n in range(MIN_NUM, MAX_NUM)]
end = time.time()
print("list comprehension:", end - start, "seconds")

start = time.time()
mylist2 = list(n**2 for n in range(MIN_NUM, MAX_NUM))
end = time.time()
print("array computation:", end - start, "seconds")

start = time.time()
for n in range(MIN_NUM, MAX_NUM):
    mylist3.append(n**2)
end = time.time()
print("for loop:", end - start, "seconds")

start = time.time()
mylist4 = list(map(give_exponent, range(MIN_NUM, MAX_NUM)))
end = time.time()
print("map:", end - start, "seconds")
