res = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
arr = [0]
for i in range(1, 26):
    arr.append((arr[i-1]*2+1))

def Try(n, k):
    if k-1 == arr[n-1]:
        return res[n-1]
    return Try(n-1, k if k <= arr[n-1] else k-arr[n-1]-1)

for _ in range(int(input())):
    n, k = [int(i) for i in input().split()]
    print(Try(n, k))