import random
a = random.randint(3,21)
print(a)
b = []
for i in range(1,a +1):
    for j in range(i+1,a+1):
        if i == j:
            continue  
        if a % (i + j) == 0:
            x = (f"{i}{j}")
            b.append(x)
print(*b)  