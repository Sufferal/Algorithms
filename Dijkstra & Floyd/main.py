import math
import random
import numpy as np
import time
import random
import heapq
from prettytable import PrettyTable
from graphviz import Digraph
from matplotlib import pyplot as plt

# Generate random graph
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

# Generate sparse graph
def generate_sparse_graph(num_nodes, edge_density):
    max_edges = int(num_nodes * (num_nodes-1) / 2)
    num_edges = int(max_edges * edge_density)
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

# Generate complete graph
def generate_complete_graph(num_nodes):
    graph = {str(i): {} for i in range(num_nodes)}
    nodes = list(graph.keys())

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            weight = random.randint(1, 10)
            graph[nodes[i]][nodes[j]] = weight
            graph[nodes[j]][nodes[i]] = weight

    return graph

# Display graph
def display_graph(graph, string):
    dot = Digraph()
    added_edges = set()
    for node in graph:
        dot.node(node)
        for neighbor, weight in graph[node].items():
            if (node, neighbor) not in added_edges and (neighbor, node) not in added_edges:
                dot.edge(node, neighbor, label=str(weight), dir='none')
                added_edges.add((node, neighbor))
    dot.render(string, view=True)

# Dijkstra
def dijkstra(graph, start, target):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        if current_vertex == target:
            return distances[target]

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return -1  

# Floyd
def floyd(graph, start, target):
    if start not in graph or target not in graph:
        return -1

    dist = {}
    for i in graph:
        dist[i] = {}
        for j in graph:
            if i == j:
                dist[i][j] = 0
            elif i in graph and j in graph[i]:
                dist[i][j] = graph[i][j]
            else:
                dist[i][j] = float('inf')

    for k in graph:
        for i in graph:
            for j in graph:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    if dist[start][target] == float('inf'):
        return -1
    else:
        return dist[start][target]

def show_results():
  # Seed
  random.seed(123)

  times_floyd = list()
  times_dj = list()
  nodes = [10, 25, 50, 100]
  nodes_searched = list()
  node_search = list()
  digit_num = 6
  image_num = 1

  # 5-7 (100), 15-12 (100), 30-30 (100)
  graph_sparse = generate_sparse_graph(6, 2 / 5)
  graph_dense = generate_complete_graph(6)
  display_graph(graph_sparse, 'Sparse')
  display_graph(graph_dense, 'Dense')

  for i in nodes:
      current_times_dj = list()
      current_times_floyd = list()
      random_nodes = list()
      nodes_searched.append('Graph ' + str(i))
      node_search.append('Graph: ' + str(i))

      # Sparse graph
      nodes_searched.append('Sparse: ')
      node_search.append('Sparse: ')
      graph_sparse = generate_sparse_graph(i, 2 / i)

      if i / 5 >= 5:
          search = 5
      else:
          search = math.floor(i / 5)

      for j in range(search):
          start_node = str(random.randint((j + 1), (j + 1) * 2))
          end_node = str(random.randint((j + 1) * 3, (j + 1) * 5))

          # Dijkstra
          start_time = time.perf_counter()
          shortest_path_dj = dijkstra(graph_sparse, start_node, end_node)
          end_time = time.perf_counter()
          time_taken = end_time - start_time
          current_times_dj.append(round(time_taken, digit_num))

          # Floyd
          start_time = time.perf_counter()
          shortest_path_floyd = floyd(graph_sparse, start_node, end_node)
          end_time = time.perf_counter()
          time_taken = end_time - start_time
          current_times_floyd.append(round(time_taken, digit_num))

          random_nodes.append([start_node, end_node])
          nodes_searched.append(start_node + '-' + end_node + ' = ' + str(shortest_path_dj) + ' | ')
          node_search.append(start_node + '-' + end_node + ' | ')

      # Dense graph
      nodes_searched.append('Dense: ')
      node_search.append('Dense: ')
      graph_dense = generate_complete_graph(i)

      for j in random_nodes:
          start_node = j[0]
          end_node = j[1]

          # Dijkstra
          start_time = time.perf_counter()
          shortest_path_dj = dijkstra(graph_dense, start_node, end_node)
          end_time = time.perf_counter()
          time_taken = end_time - start_time
          current_times_dj.append(round(time_taken, digit_num))

          # Floyd
          start_time = time.perf_counter()
          shortest_path_floyd = floyd(graph_dense, start_node, end_node)
          end_time = time.perf_counter()
          time_taken = end_time - start_time
          current_times_floyd.append(round(time_taken, digit_num))

          nodes_searched.append(start_node + '-' + end_node + ' = ' + str(shortest_path_dj) + ' | ')
          node_search.append(start_node + '-' + end_node + ' | ')

      times_floyd.append(current_times_floyd)
      times_dj.append(current_times_dj)

  myTable = PrettyTable(['Graphs', *['Sparse graph', 'Dense graph']])
  myTable.add_row(["Dijkstra 10 nodes", *[times_dj[0][0:2], times_dj[0][2:4]]])
  myTable.add_row(["Floyd 10 nodes", *[times_floyd[0][0:2], times_floyd[0][2:4]]])
  myTable.add_row(["Dijkstra 25 nodes", *[times_dj[1][0:5], times_dj[1][5:10]]])
  myTable.add_row(["Floyd 25 nodes", *[times_floyd[1][0:5], times_floyd[1][5:10]]])
  myTable.add_row(["Dijkstra 50 nodes", *[times_dj[2][0:5], times_dj[2][5:10]]])
  myTable.add_row(["Floyd 50 nodes", *[times_floyd[2][0:5], times_floyd[2][5:10]]])
  myTable.add_row(["Dijkstra 100 nodes", *[times_dj[3][0:5], times_dj[3][5:10]]])
  myTable.add_row(["Floyd 100 nodes", *[times_floyd[3][0:5], times_floyd[3][5:10]]])

  print(myTable)

  arr = [i for i in range(5)]
  x = np.arange(1, len(arr)+1)

  # Dijkstra
  plt.figure(image_num)
  plt.bar(x-0.3, times_dj[1][0:5], 0.2, label='Sparse 25 ', color='blue')
  plt.bar(x-0.2, times_dj[2][0:5], 0.2, label='Sparse 50', color='green')
  plt.bar(x-0.1, times_dj[3][0:5], 0.2, label='Sparse 100', color='cyan')
  plt.bar(x+0.1, times_dj[1][5:10], 0.2, label='Dense 25', color='purple')
  plt.bar(x+0.2, times_dj[2][5:10], 0.2, label='Dense 50', color='orange')
  plt.bar(x+0.3, times_dj[3][5:10], 0.2, label='Dense 100', color='red')
  plt.xlabel('Nodes checked')
  plt.ylabel('Elapsed time, s')
  plt.title('Dijkstra shortest path')
  plt.legend()
  image_num += 1

  # Floyd
  plt.figure(image_num)
  plt.bar(x-0.3, times_floyd[1][0:5], 0.2, label='Sparse 25 ', color='blue')
  plt.bar(x-0.2, times_floyd[2][0:5], 0.2, label='Sparse 50', color='green')
  plt.bar(x-0.1, times_floyd[3][0:5], 0.2, label='Sparse 100', color='cyan')
  plt.bar(x+0.1, times_floyd[1][5:10], 0.2, label='Dense 25', color='purple')
  plt.bar(x+0.2, times_floyd[2][5:10], 0.2, label='Dense 50', color='orange')
  plt.bar(x+0.3, times_floyd[3][5:10], 0.2, label='Dense 100', color='red')
  plt.xlabel('Nodes checked')
  plt.ylabel('Elapsed time, s')
  plt.title('Floyd shortest path')
  plt.legend()
  image_num += 1

  # Both 50-100
  plt.figure(image_num)
  plt.bar(x-0.4, times_dj[2][0:5], 0.2, label='Dijkstra sparse 50 ', color='blue')
  plt.bar(x-0.3, times_dj[3][0:5], 0.2, label='Dijkstra sparse 100', color='green')
  plt.bar(x-0.2, times_floyd[2][0:5], 0.2, label='Floyd sparse 50', color='cyan')
  plt.bar(x+0.1, times_floyd[3][0:5], 0.2, label='Floyd sparse 100', color='purple')
  plt.bar(x+0.1, times_dj[2][5:10], 0.2, label='Dijkstra dense 50', color='orange')
  plt.bar(x+0.2, times_dj[3][5:10], 0.2, label='Dijkstra dense 100', color='red')
  plt.bar(x+0.3, times_floyd[2][5:10], 0.2, label='Floyd dense 50', color='yellow')
  plt.bar(x+0.4, times_floyd[3][5:10], 0.2, label='Floyd dense 100', color='brown')
  plt.xlabel('Nodes checked')
  plt.ylabel('Elapsed time, s')
  plt.title('Shortest path')
  plt.legend()
  image_num += 1

  plt.show()

if __name__ == '__main__':
    show_results()