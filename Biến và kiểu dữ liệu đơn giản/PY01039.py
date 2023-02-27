def check(s) :
    for i in range(2, len(s)) :
        if s[i] != s[i - 2] : return False
    return True
for i in range() :
    s = input()
    print("YES") if check(s) else print("NO")