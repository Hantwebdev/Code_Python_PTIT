import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 : return False
    return n > 1
def check(n):
    nt, nnt = 0, 0
    for i in n:
        if i in ['2', '3', '5', '7']: 
            nt += 1
        else: nnt += 1
    return nt > nnt and isPrime(len(n))
for case in range(int(input())):
    n = input()
    print("YES") if check(n) else print("NO")