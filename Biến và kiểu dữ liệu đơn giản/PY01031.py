if __name__ == '__main__':
    for case in range(int(input())):
        n, m = list(map(int, input().split()))
        res = ''
        tmp = n
        while tmp > 0:
            du = tmp % m
            if du >= 10: res += str(chr(du + 55))
            else: res += str(du)
            tmp = int(tmp / m)
        print(''.join(reversed(res)))
