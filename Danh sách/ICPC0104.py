for case in range(int(input())):
    s = input()
    t = ''
    for x in s:
        if x.isalpha():
            t += ' '
        else:
            t += x
    a = list(map(int, t.split()))
    a.sort()
    print(a[0])
