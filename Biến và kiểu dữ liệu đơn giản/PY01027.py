def check(n):
    for i in range(len(n)):
        if n[i] not in ['6', '8']: return False
        if n[0] == '8': return False
        if n[i] == '8' and n[i - 1] not in ['6', '8']: return False
        if i >= 2 and n[i] == '8' and n[i-1] == '8' and n[i-2] != '6': return False
    return True
if __name__ == '__main__':
    n = input()
    print('YES') if check(n) else print('NO')