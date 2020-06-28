# python3
import queue

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


def max_flow(graph, from_, to):
    flow = 0
    # your code goes here
    while True:
        for i, edge in enumerate(graph.edges):
            edge.capacity -= edge.flow
            edge.flow = 0
        min_flow, path = bfs(graph, from_, to)
        if min_flow == -1:
            return flow
        else:
            for i in range(len(path) - 1):
                graph.add_flow(path[i][1], min_flow)
            flow += min_flow



def bfs(graph, from_, to):
    prev = [[graph.size(), -1]] * graph.size()
    prev[from_] = [-1, -1]
    Q = queue.Queue()
    Q.put(from_)
    flag = 1
    while not Q.empty() and flag:
        u = Q.get()
        for edge in graph.get_ids(u):
            if graph.get_edge(edge).capacity > 0 and prev[graph.get_edge(edge).v][0] == graph.size() and graph.get_edge(edge).u != graph.get_edge(edge).v:
                prev[graph.get_edge(edge).v] = [u, edge]
                if graph.get_edge(edge).v == to:
                    flag = 0
                    break
                Q.put(graph.get_edge(edge).v)
    if prev[to][0] == graph.size():
        return -1, []
    else:
        min_flow = 3e8
        ind = to
        path = [(ind, -1)]
        while prev[ind][0] != -1:
            pre = prev[ind][0]
            edge = prev[ind][1]
            path.append((pre, edge))
            if graph.get_edge(edge).capacity < min_flow:
                min_flow = graph.get_edge(edge).capacity
            ind = pre
        path.reverse()
        return min_flow, path

'''
def print_graph(graph):
    print(graph.graph)
    ind = 0
    for edge in graph.edges:
        print(f"Vertice {ind}: U {edge.u}, V {edge.v}, Capacity {edge.capacity}, Flow {edge.flow}")
        ind += 1
'''

if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
