#Uses python3
import sys
import math

class Union(object):
    def __init__(self, n):
        self.count = n
        self.id = list(range(n))
        self.num_group = n

    def find(self, p):
        if p >= 0 and p < self.count:
            return self.id[p]

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union_elements(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)
        if p_id == q_id:
            return None
        i = 0
        while i < self.count:
            if self.id[i] == p_id:
                self.id[i] = q_id
            i += 1
        self.num_group -= 1

def clustering(x, y, k):
    #write your code here
    n_nodes = len(x)
    d_set = Union(n_nodes)
    dist = []
    for i in range(n_nodes):
        for j in range(i + 1, n_nodes):
            dist.append((math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2), i, j))
    dist = sorted(dist)
    for i in range(len(dist)):
        tup = dist[i]
        if not d_set.is_connected(tup[1], tup[2]):
            d_set.union_elements(tup[1], tup[2])
            if d_set.num_group == k - 1:
                return tup[0]


if __name__ == '__main__':
    #f = open('input.txt', 'rb')
    #input = f.read()
    #f.close()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
