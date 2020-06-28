
import sys

sys.setrecursionlimit(200000)

def reverse_graph(adj):
    reversed_adj = [[] for _ in range(len(adj))]
    for i, edges in enumerate(adj):
        for edge in edges:
            reversed_adj[edge].append(i)
    return reversed_adj


def explore(x, adj, used, post_num, clock):
    used[x] = 1
    clock += 1
    for y in adj[x]:
        if used[y] == 0:
            explore(y, adj, used, post_num, clock)
    clock += 1
    post_num[x] = clock


def dfs(adj, num):
    #write your code here
    if not any(adj): return
    post_num = [0] * len(adj)
    clock = 0
    used = [0] * len(adj)
    for x in range(len(adj)):
        if used[x] == 0:
            explore(x, adj, used, post_num, clock)
    used = [0] * len(adj)
    explore(x, adj, used, post_num, clock)
    for i in range(used):
        if used[i]:
            remove_node(adj, i)
    num += 1
    dfs(adj, num)

    
def remove_node(adj, x):
    del adj[x]
    for edges in adj:
        for i, edge in enumerate(edges):
            if edge > x:
                edges[i] -= 1
            elif edge == x:
                del edges[i]


if __name__ == '__main__':
    adj = [[1], [2], [0], [0]]
    reversed_adj = reverse_graph(adj)
    remove_node(adj, 2)
    print(adj)