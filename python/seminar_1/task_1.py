import random
def task (n):
    l = []
    for i in range (1,n):
        l.append(random.randint(10,30))
    return l

print (task (5))


