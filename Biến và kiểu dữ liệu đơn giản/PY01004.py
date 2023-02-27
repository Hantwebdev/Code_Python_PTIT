import math
def isprime(n):
    for i in range(2, (int) (math.isqrt(n) + 1)):
        if n % i == 0: return 0
    return n > 1
if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        cnt = 0
        for j in range(1, n):
            if(math.gcd(j, n) == 1):
                cnt += 1
        print("YES", end='\n') if isprime(cnt) else print("NO", end='\n')
    