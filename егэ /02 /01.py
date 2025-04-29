from itertools import *

def f(x, y, z, w): return x and (z <= w) and (not y)

for a in product([0, 1], repeat = 7):
    table = [(a[0], a[1], 1, a[2]), (a[3], 1, 0, a[4]), (1, 0, a[5], a[6])] 
    if len(table) == len(set(table)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]: # хДхДхД лол лол лол 
                print(p)

