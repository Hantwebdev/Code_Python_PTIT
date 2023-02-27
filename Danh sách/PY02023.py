for case in range(int(input())):
    n = int(input())
    print(*sorted([i for i in input().split()], key=lambda x: (sum(int(i) for i in x), int(x))))