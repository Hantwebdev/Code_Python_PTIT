for case in range(int(input())) :
    n = input()
    mul, sum = 1, 0
    ok = 0
    for i in range(len(n)) :
        if i % 2 == 0 :
            if n[i] != '0' :
                ok = 1
                mul *= int(n[i])
        else : sum += int(n[i])
    if ok == 0 : mul = 0
    print(mul, sum)