for case in range(int(input())) :
    n = input()
    sum = 0
    s = ""
    for i in n :
        if i.isdigit() : sum += int(i)
        else : s += i
    print(''.join(sorted(s)), sum, sep = "")