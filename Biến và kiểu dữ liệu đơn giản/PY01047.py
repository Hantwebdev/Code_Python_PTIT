import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 : return False
    return n > 1
for case in range(int(input())):
    n = input()
    print("YES") if isPrime(int(n[-4::])) else print("NO")