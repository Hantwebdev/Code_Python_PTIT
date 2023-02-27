for case in range(int(input())):
    n = input() + '/'
    cnt, res = 0, n[0]
    for i in n:
        if i == res:
            cnt += 1
        else:
            print(str(cnt) + res, end='')
            cnt, res = 1, i
    print()