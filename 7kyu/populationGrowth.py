import math

def nb_year(p0, percent, aug, p):
    n = 0
    while p0 < p:
        p0 = p0 + p0 * (percent * 0.01) + aug
        p0 = math.floor(p0)
        n += 1
    return n

print(nb_year(1500, 5, 100, 5000))