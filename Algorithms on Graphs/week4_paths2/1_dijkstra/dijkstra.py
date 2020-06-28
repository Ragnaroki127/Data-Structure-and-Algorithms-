#Uses python3

import sys
import heapq

def distance(adj, cost, s, t):
    #write your code here
    dist = [float('inf')] * (len(adj))
    prev = [None] * len(adj)
    dist[s] = 0
    H = []
    for v, dis in enumerate(dist):
        H.append((dis, v))
    heapq.heapify(H)
    processed = [0] * len(adj)
    while len(H) > 0:
        u = heapq.heappop(H)[1]
        if processed[u] == 1:
            continue
        for i in range(len(adj[u])):
            if dist[adj[u][i]] > dist[u] + cost[u][i]:
                dist[adj[u][i]] = dist[u] + cost[u][i]
                prev[adj[u][i]] = u
                heapq.heappush(H, (dist[adj[u][i]], adj[u][i]))
        processed[u] = 1
    return dist[t] if not dist[t] == float('inf') else -1 


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
