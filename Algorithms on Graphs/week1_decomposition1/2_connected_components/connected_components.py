#Uses python3

import sys

def explore(x, adj, visited):
    visited[x] = 1
    for y in adj[x]:
        if visited[y] == 0:
            explore(y, adj, visited)

def number_of_components(adj):
    result = 0
    visited = [0] * len(adj)
    for x in range(len(adj)):
        if visited[x] == 0:
            explore(x, adj, visited)
            result += 1
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
