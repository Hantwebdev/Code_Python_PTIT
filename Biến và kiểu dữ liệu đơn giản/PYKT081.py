def solve(list):
    if len(list) != 4: return 'NO'
    for i in list:
        if not i.isnumeric() or int(i) > 255 or int(i) < 0:
            return 'NO'
    return 'YES'

for case in range(int(input())):
    print(solve(input().split('.')))