def check(n):
    for i in range(len(n)):
        if(n[i] not in ['4', '7']): return False
    return True
if __name__ == '__main__':
    for i in range(int(input())):
        n = input()
        print("YES", end='\n') if check(n) else print("NO", end='\n')