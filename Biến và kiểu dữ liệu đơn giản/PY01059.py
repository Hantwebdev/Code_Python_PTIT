for case in range(int(input())) :
    n = input()
    sum, mul = 0, 1
    ok = 0
    for i in range(len(n)) :
        if i % 2 == 0 : sum += int(n[i])
        else :
            if n[i] != '0' :
                ok = 1
                mul *= int(n[i])
    if ok == 0 : mul = 0
    print(sum, mul)