# python3
import sys
from collections import deque

class Edge:
    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

class FlowGraph:
    def __init__(self, n):
        self.edges = []
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Create forward and backward edges
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        # Add edges to the adjacency list
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
        # Update flow for both forward and backward edges
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow

def read_data():
    # Read input and create a FlowGraph
    data = sys.stdin.read().splitlines()
    vertex_count, edge_count = map(int, data[0].split())
    graph = FlowGraph(vertex_count)
    for line in data[1:]:
        u, v, capacity = map(int, line.split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph

def bfs(graph, from_, to, parent):
    visited = [False] * graph.size()
    queue = deque([from_])
    visited[from_] = True
    
    while queue:
        u = queue.popleft()
        for edge_id in graph.get_ids(u):
            edge = graph.get_edge(edge_id)
            # If there's remaining capacity and the node hasn't been visited
            if not visited[edge.v] and edge.capacity > edge.flow:
                parent[edge.v] = edge_id
                visited[edge.v] = True
                queue.append(edge.v)
                if edge.v == to:
                    return True
    return False

def max_flow(graph, from_, to):
    flow = 0
    parent = [-1] * graph.size()
    
    # Augment the flow while there is an augmenting path
    while bfs(graph, from_, to, parent):
        # Find the maximum flow we can push through the path found by BFS
        path_flow = float('Inf')
        v = to
        while v != from_:
            edge_id = parent[v]
            edge = graph.get_edge(edge_id)
            path_flow = min(path_flow, edge.capacity - edge.flow)
            v = edge.u

        # Update the flow along the path
        v = to
        while v != from_:
            edge_id = parent[v]
            graph.add_flow(edge_id, path_flow)
            v = graph.get_edge(edge_id).u

        # Add path flow to total flow
        flow += path_flow
    
    return flow

if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))