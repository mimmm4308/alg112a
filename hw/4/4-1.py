from numpy import arange

def ans(a):
    return a**2 - 3*a + 1
    

for i in arange(-100, 100, 0.001):
    if abs(ans(i)) < 0.001:
        print("x =", i, " f(x) =", ans(i))