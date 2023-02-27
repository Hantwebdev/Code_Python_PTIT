def check(n):
    s = str(sum(int(i) for i in n))
    return s == s[::-1] and int(s) >= 10
if __name__ == '__main__':
    for case in range(int(input())):
        n = input()
        print("YES") if check(n) else print("NO")