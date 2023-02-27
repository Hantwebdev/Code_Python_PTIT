def check(n):
    sum4, sum7 = 0, 0
    for i in range(len(n)):
        if(int(n[i]) == 4): sum4 += 1
        elif (int(n[i]) == 7): sum7 += 1
    return sum4 + sum7 == 4 or sum4 + sum7 == 7
if __name__ == '__main__':
    n = input()
    print("YES", end='\n') if check(n) else print("NO", end='\n')