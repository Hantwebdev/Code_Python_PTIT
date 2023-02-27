def check(s) :
    for i in s :
        if i not in ['0', '1', '2'] : return False
    return True
for case in range(int(input())) :
    s = input()
    print("YES") if check(s) else print("NO")