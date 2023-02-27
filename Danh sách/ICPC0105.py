for case in range(int(input())):
    n = input()
    s = ''
    for i in n:
        if i.isalpha(): s += ' '
        else: s += i
    a = list(map(int, s.split()))
    a.sort(reverse= True)
    print(a[0])