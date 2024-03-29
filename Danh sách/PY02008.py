import mat
def isprime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return n > 1

prm = [2]
i = 3
while len(prm) <= 1001:
    if isprime(i):
        prm += [i]
    i += 2

n, x = [int(i) for i in input().split()]
index = 0
for i in range(n+1):
    print(x, end = ' ')
    x += prm[i]
print()