#!/usr/bin/python3

import sys
#import queue
import heapq

class BiDij:
    def __init__(self, n):
        self.n = n;                             # Number of nodes
        self.inf = n*10**6                      # All distances in the graph are smaller
        self.d = [[self.inf]*n, [self.inf]*n]   # Initialize distances for forward and backward searches
        self.visited = [False]*n                  # visited[v] == True iff v was visited by forward or backward search
        self.workset = []                       # All the nodes visited by forward or backward search

    def clear(self):  
        self.d = [[self.inf]*n, [self.inf]*n]
        self.visited = [False]*n
        self.workset = []

    def visit(self, q, side, v, dist):
        if self.d[side][v] > dist:
            self.d[side][v] = dist
            heapq.heappush(q[side], (self.d[side][v], v))
            self.workset.append(v)

    def process(self, q, side, v, adj, cost):
        for u, w in zip(adj[v], cost[v]):
            self.visit(q, side, u, self.d[side][v] + w)
    '''
        if self.visited[side][u] is True:
            return
        for i, v in enumerate(adj[u]):
            if self.d[side][v] > self.d[side][u] + cost[u][i]:
                self.d[side][v] = self.d[side][u] + cost[u][i]
                heapq.heappush(q[side], (self.d[side][v], v))
        self.visited[side][u] = True
        self.workset.append(u)
    '''

    def shortestpath(self):
        distance = self.inf
        for u in self.workset:
            if self.d[0][u] + self.d[1][u] < distance:
                distance = self.d[0][u] + self.d[1][u]
        return distance if not distance == self.inf else -1

    def query(self, adj, cost, s, t):
        self.clear()
        #self.d[0][s] = 0
        #self.d[1][t] = 0
        q = [[], []]
        '''
        for i in range(self.n):
            heapq.heappush(q[0], (self.d[0][i], i))    
            heapq.heappush(q[1], (self.d[1][i], i))
        '''
        self.visit(q, 0, s, 0)
        self.visit(q, 1, t, 0)
        while not len(q[0]) == 0 and not len(q[1]) == 0:
            for side in [0, 1]:
                v = heapq.heappop(q[side])[1]
                self.process(q, side, v, adj[side], cost[side])
                if self.visited[v]:
                    return self.shortestpath()
                self.visited[v] = True
        return -1
        '''
        while(True):
            if len(q[0]) == 0 or len(q[1]) == 0:
                return -1
            u = heapq.heappop(q[0])[1]
            self.process(u, q, 0, adj[0], cost[0])
            if self.visited[1][u] is True:
                return self.shortestpath()
            v = heapq.heappop(q[1])[1]
            self.process(v, q, 1, adj[1], cost[1])
            if self.visited[0][v] is True:
                return self.shortestpath()
        '''

def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n,m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u,v,c = readl()
        adj[0][u-1].append(v-1)
        cost[0][u-1].append(c)
        adj[1][v-1].append(u-1)
        cost[1][v-1].append(c)
    t, = readl()
    bidij = BiDij(n)
    for i in range(t):
        s, t = readl()
        print(bidij.query(adj, cost, s-1, t-1))
