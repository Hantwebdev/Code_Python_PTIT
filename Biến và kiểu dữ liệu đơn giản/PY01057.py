import math
def isPrime(n) :
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return 0
    return n > 1
def check(s) :
	for i in range(len(s)) :
		if isPrime(i) != isPrime(int(s[i])) : return 0
	return 1
t = int(input())
for i in range(t) :
	s = input()
	print("YES") if check(s) else print("NO")