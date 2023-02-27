def DFS(graph, cur, v, visit, seen):
    path.append(cur)
    if cur == v:
        for ele in path:
            visit[ele] += 1
        return
    for ele in graph[cur]:
        if ele in path:
            continue
        DFS(graph, ele, v, visit, seen)     
        path.pop()

for test in range(int(input())):
    n, m, u, v = [int(i) for i in input().split()]
    graph, visit = [], []
    for i in range(n+1):
        graph.append([])