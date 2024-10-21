import random
from random import randint

first = randint(0, 5)
second = randint(0, 5)
third = randint(0, 5)

if first == second == third:
    print (3)
elif first == second or first == third or second == third:
    print (2)
else:
    print (0)