#Uses python3

import sys

def acyclic(adj):
    flag = 0
    for i, out_edge in enumerate(adj):
        if out_edge == []:
            for j, edge in enumerate(adj):
                if i in edge:
                    flag = 1
                    del adj[j][edge.index(i)]
    if flag == 0 and any(adj):
        return 1
    elif flag == 0 and not any(adj):
        return 0
    else:
        return acyclic(adj)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
