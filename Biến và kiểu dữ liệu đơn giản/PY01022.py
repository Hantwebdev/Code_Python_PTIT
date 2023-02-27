n = input()
res = 1 if len(n) == 1 else 0
while(len(n) > 1):
    n = str(sum(ord(i)-ord('0') for i in n))
    res += 1
print(res)