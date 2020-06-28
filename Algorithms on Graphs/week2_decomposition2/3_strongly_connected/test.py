#Uses python3
#Kosararu's algorithm

import sys

sys.setrecursionlimit(200000)
clock = 0

def reverse_graph(adj):
    reversed_adj = [[] for _ in range(len(adj))]
    for i, edges in enumerate(adj):
        for edge in edges:
            reversed_adj[edge].append(i)
    return reversed_adj


def explore(x, adj, used, post_num):
    global clock
    used[x] = 1
    clock += 1
    for y in adj[x]:
        if used[y] == 0:
            explore(y, adj, used, post_num)
    clock += 1
    post_num[x] = clock

def Explore(x, adj, used):
    used[x] = 1
    for y in adj[x]:
        if used[y] == 0:
            Explore(y, adj, used)

def number_of_strongly_connected_components(adj):
    result = 0
    adj_re = reverse_graph(adj)
    used = [0] * len(adj)
    post_num = [0] * len(adj)
    for x in range(len(adj)):
        if used[x] == 0:
            explore(x, adj_re, used, post_num)

    dfs_sequence = []
    for i in range(len(post_num)):
        dfs_sequence.append(post_num.index(max(post_num)))
        post_num[post_num.index(max(post_num))] = -1

    used = [0] * len(adj)

    for x in dfs_sequence:
        if used[x] == 0:
            Explore(x, adj, used)
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
    print(number_of_strongly_connected_components(adj))
