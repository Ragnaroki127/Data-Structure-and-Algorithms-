#Uses python3

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


def dfs(adj, num):
    global clock
    #write your code here
    if not any(adj): 
        num += len(adj)
        return num
    post_num = [0] * len(adj)
    clock = 0
    used = [0] * len(adj)
    for x in range(len(adj)):
        if used[x] == 0:
            explore(x, adj, used, post_num)
    v = post_num.index(max(post_num))
    used = [0] * len(adj)
    explore(v, reverse_graph(adj), used, post_num)
    num_of_nodes_removed = 0
    for i in range(len(used)):
        if used[i]:
            remove_node(adj, i - num_of_nodes_removed)
            num_of_nodes_removed += 1
    num += 1
    return dfs(adj, num)

    
def remove_node(adj, x):
    del adj[x]
    for edges in adj:
        for i, edge in enumerate(edges):
            if edge > x:
                edges[i] -= 1
            elif edge == x:
                del edges[i]


def number_of_strongly_connected_components(adj):
    result = 0
    #write your code here
    result = dfs(reverse_graph(adj), result)
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
