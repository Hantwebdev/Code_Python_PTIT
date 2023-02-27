def check(n):
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]: return False
    return True
if __name__  == '__main__':
    for case in range(int(input())):
        n = input()
        print("YES", end='\n') if check(n) else print("NO", end='\n')