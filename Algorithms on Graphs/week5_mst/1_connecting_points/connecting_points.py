#Uses python3
import sys
import math
import heapq 

def minimum_distance(x, y):
    result = 0.
    #write your code here
    n_nodes = len(x)
    cost = [float('inf')] * n_nodes
    cost[0] = 0
    H = []
    for i in range(n_nodes):
        H.append((cost[i], i, x[i], y[i]))
    heapq.heapify(H)
    processed = [0] * n_nodes

    while len(H) > 0:
        u = heapq.heappop(H)[1]
        if processed[u] == 1:
            continue
        for tup in H:
            v = tup[1]            
            if not processed[v] == 1 and not u == v:
                dist = math.sqrt((x[u] - x[v])**2 + (y[u] - y[v])**2)
                if cost[v] > dist:
                    cost[v] = dist
                    heapq.heappush(H, (dist, v, x[v], y[v]))
        processed[u] = 1

    result = sum(cost)
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
