def gensquares(N):

    for n in range(N):
        yield n**2

for x in gensquares(10):
    print(x)


import random

def rand_num(low,high,n):

    for num in range(n):
        yield random.randint(low, high)

for num in rand_num(1,10,12):
    print(num)

s = "hello"

iterable = iter(s)

for char in iterable:
  print(char)
