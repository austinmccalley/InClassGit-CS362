def calcDivisors(n):
    divisiors = []
    for i in range(1, n):
        if n % i == 0:
            divisiors.append(i)
    return divisiors


userNumber = input('Please enter a number: ')
d = calcDivisors(int(userNumber))


for i in range(len(d)):
    print(d[i])
