import math


def calcDivisors(n):
    divisiors = []
    for i in range(1, math.floor(n / 2)):
        if n % i == 0:
            divisiors.append(i)
    return divisiors


d = calcDivisors(20)


for i in range(len(d)):
    print(d[i])
