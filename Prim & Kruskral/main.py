import time
from matplotlib import pyplot as plt
from prettytable import PrettyTable
import random
import random
from graphviz import Digraph
import heapq

random.seed(666)
figure_num = 1

def generate_random_graph(num_nodes, num_edges):
    graph = {str(i): {} for i in range(num_nodes)}
    nodes = list(graph.keys())

    while num_edges > 0:
        u, v = random.sample(nodes, 2)
        if v not in graph[u]:
            weight = random.randint(1, 10)
            graph[u][v] = weight
            graph[v][u] = weight
            num_edges -= 1

    return graph

def draw_graph(graph, string):
    dot = Digraph()
    added_edges = set()
    for node in graph:
        dot.node(node)
        for neighbor, weight in graph[node].items():
            if (node, neighbor) not in added_edges and (neighbor, node) not in added_edges:
                dot.edge(node, neighbor, label=str(weight), dir='none')
                added_edges.add((node, neighbor))
    dot.render(string, view=True)

def generate_complete_graph(num_nodes):
    graph = {str(i): {} for i in range(num_nodes)}
    nodes = list(graph.keys())

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            weight = random.randint(1, 10)
            graph[nodes[i]][nodes[j]] = weight
            graph[nodes[j]][nodes[i]] = weight

    return graph

class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_root = self.find(i)
        j_root = self.find(j)
        if i_root == j_root:
            return False
        if self.rank[i_root] > self.rank[j_root]:
            self.parent[j_root] = i_root
        else:
            self.parent[i_root] = j_root
            if self.rank[i_root] == self.rank[j_root]:
                self.rank[j_root] += 1
        return True

def Prim(graph):
    visited = set()
    mst = []

    start_vertex = next(iter(graph))
    visited.add(start_vertex)
    edges = [
        (cost, start_vertex, end_vertex)
        for end_vertex, cost in graph[start_vertex].items()
    ]

    heapq.heapify(edges)

    while edges:
        cost, start_vertex, end_vertex = heapq.heappop(edges)
        if end_vertex not in visited:
            visited.add(end_vertex)
            mst.append((start_vertex, end_vertex, cost))
            for next_vertex, cost in graph[end_vertex].items():
                if next_vertex not in visited:
                    heapq.heappush(edges, (cost, end_vertex, next_vertex))
    return mst

def Kruskal(graph):
    mst = []
    ds = DisjointSet(len(graph))
    edges = [(cost, start_vertex, end_vertex) for start_vertex, edges in graph.items() for end_vertex, cost in edges.items()]
    edges.sort()

    for cost, start_vertex, end_vertex in edges:
        if ds.union(int(start_vertex), int(end_vertex)):
            mst.append((start_vertex, end_vertex, cost))
    
    return mst

def generate_mst_graph(graph, mst):
    mst_graph = {node: {} for node in graph}
    for edge in mst:
        start_vertex, end_vertex, weight = edge
        mst_graph[start_vertex][end_vertex] = weight
        mst_graph[end_vertex][start_vertex] = weight
    return mst_graph

nodes = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000]

precision = 5
graphs = []

prim_times = []
kruskal_times =[]

prim_mst = []
kruskal_mst = []

# Example
graph_1 = generate_random_graph(10, 11)
draw_graph(graph_1, 'Graph')

p = Prim(graph_1)
k = Kruskal(graph_1)

graph_prim = generate_mst_graph(graph_1, p)
graph_kruskal = generate_mst_graph(graph_1, k)

draw_graph(graph_prim, 'Prim MST')
draw_graph(graph_kruskal, 'Kruskal MST')

# Nodes
for i in nodes:
    graph = generate_random_graph(i, 2*i)
    graphs.append(graph)

    start_time = time.perf_counter()
    p = Prim(graph)
    end_time = time.perf_counter()
    prim_times.append(round((end_time - start_time), precision))
    prim_mst.append(p)

    start_time = time.perf_counter()
    k = Kruskal(graph)
    end_time = time.perf_counter()
    kruskal_times.append(round((end_time - start_time), precision))
    kruskal_mst.append(k)

def print_results():
  t = PrettyTable(['Minimum Spanning Tree / n', *nodes])
  t.add_row(["Prim", *prim_times])
  t.add_row(["Kruskal", *kruskal_times])
  print(t)

def plot_graphs():
  global figure_num

  plt.figure(figure_num)
  plt.plot(nodes, prim_times, label='Prim', color='red')
  plt.xlabel('Number of nodes, n')
  plt.ylabel('Time, (s)')
  plt.title('Prim')
  plt.grid()
  figure_num += 1

  plt.figure(figure_num)
  plt.plot(nodes, kruskal_times, label='Kruskal', color='violet')
  plt.xlabel('Number of nodes, n')
  plt.ylabel('Time, (s)')
  plt.title('Kruskal')
  plt.grid()
  figure_num += 1

  plt.figure(figure_num)
  plt.plot(nodes, prim_times, label='Prim', color='red')
  plt.plot(nodes, kruskal_times, label='Kruskal', color='violet')
  plt.xlabel('Number of nodes, n')
  plt.ylabel('Time, (s)')
  plt.title('Both MST algorithms')
  plt.grid()
  plt.legend()
  figure_num += 1

  plt.show()

if __name__ == '__main__':
    print_results()
    plot_graphs()