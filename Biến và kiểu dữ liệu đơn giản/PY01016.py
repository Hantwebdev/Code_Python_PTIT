for case in range(int(input())):
    n = input()
    res = ''
    for i in range(0, len(n), 2):
        res += n[i] * int(n[i + 1])
    print(res, end='\n')