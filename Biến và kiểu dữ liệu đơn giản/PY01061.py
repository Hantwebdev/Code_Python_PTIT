import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1
if __name__ == '__main__':
    for case in range(int(input())):
        n = input()
        print("YES") if (len(n) > 3 and isPrime(int(n[:3])) and isPrime(int(n[len(n)-3 :]))) else print("NO")