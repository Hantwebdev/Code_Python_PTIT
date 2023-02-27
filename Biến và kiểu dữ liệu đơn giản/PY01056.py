import math
def isprime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return n > 2
def deff(n):
    if not isprime(sum(int(i) for i in n)):
        return 'NO'
    for i in range(len(n)):
        if int(i) % 2 != int(n[i]) % 2:
            return 'NO'
    return 'YES'
for case in range(int(input())):
    n = input()
    print(deff(n))