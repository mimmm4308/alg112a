import random

def neighbor(f, p, h=0.01):
    dimensions = len(p)
    index = random.randint(0, dimensions - 1)
    direction = random.choice([-1, 1])
    p1 = p.copy()
    p1[index] += direction * h

    return p1, f(*p1)

def hillClimbing(f, p, h=0.01):
    failCount = 0
    while (failCount < 10000):
        fnow = f(*p)
        p1, f1 = neighbor(f, p, h)
        if f1 >= fnow:
            fnow = f1
            p = p1
            print('p=', p, 'f(p)=', fnow)
            failCount = 0
        else:
            failCount = failCount + 1
    return p, fnow

def f(x, y, z):
    return -1*(x**2 + y**2 + z**2)

result = hillClimbing(f, [2, 1, 3])
