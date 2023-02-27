for i in range(int(input())):
    n = input()
    print("YES", end='\n') if n[:2] == n[len(n) - 2:] else print("NO", end='\n')