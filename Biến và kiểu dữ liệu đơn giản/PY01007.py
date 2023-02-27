import math
if __name__ == '__main__':
    for i in range(int(input())):
        N, X, M = [float(i) for i in input().split()]
        years = (math.log(M / N, 1 + X/100))
        print(years) if years == int(years) else print(int(years)+1)