import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return n > 1
if __name__ == '__main__':
    for case in range(int(input())):
        a, b = [int(i) for i in input().split()]
        print("YES") if isPrime(sum(int(i) for i in str(math.gcd(a, b)))) else print("NO", end='\n')