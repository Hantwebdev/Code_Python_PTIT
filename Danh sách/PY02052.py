if __name__ == '__main__':
    n = int(input())
    matrix = []
    for i in range(n):
        arr = list(map(int, input().split()))
        matrix.append(arr)
    k = int(input())
    sum_above, sum_under = 0, 0
    for i in range(n):
        for j in range(i):
            sum_under += matrix[i][j]
    for i in range(n):
        for j in range(i + 1, n):
                sum_above += matrix[i][j]
    sub = abs(sum_above - sum_under)
    print('YES', end='\n') if sub <= k else print('NO', end= '\n')
    print(sub)