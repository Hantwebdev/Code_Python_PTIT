import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 : return False
    return n > 1
def check(n):
    return isPrime(sum(int(i) for i in n))
if __name__ == '__main__':
    for case in range(int(input())):
        n = input()
        print("YES") if check(n) else print("NO")