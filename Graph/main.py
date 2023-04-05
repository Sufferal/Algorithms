import networkx as nx
import collections
import matplotlib.pyplot as plt
import pydot
import collections
import time
import random
import prettytable
import numpy as np

# Define the DFS algorithm
def dfs(graph, start, target, visited=None, print_path=False):
    if visited is None:
        visited = set()

    visited.add(start)
    if(print_path):
      print(start, end=" -> ")

    if start == target:
        if(print_path):
          print("")
        return True

    for next in graph[start]:
        if next not in visited:
            if dfs(graph, next, target, visited, print_path):
                return True

    return False


def bfs(graph, start, target, print_path=False):
    visited, queue = set(), collections.deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        if(print_path):
          print(vertex, end=" -> ")

        if vertex == target:  
          if(print_path):
            print("")
          return True

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    print("Target node not reachable from the start node")
    return False

# # Create a balanced graph
# g1 = nx.Graph()
# g1.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (4, 9), (5, 10), (5, 11),
#                   (6, 12), (6, 13), (7, 14), (7, 15)])
# pos1 = nx.nx_pydot.graphviz_layout(g1, prog="dot")
# nx.draw(g1, pos=pos1, with_labels=True, font_color="white")
# plt.show()

# # Create an unbalanced graph
# g2 = nx.Graph()
# g2.add_edges_from([(1, 2), (1, 3), (1, 7), (2, 4), (3, 8), (4, 5), (5, 6), (6, 15), (6, 16), (7, 9), (7, 13), (8, 10), (9, 11), (9, 12), (11, 14)])
# pos2 = nx.nx_pydot.graphviz_layout(g2, prog="dot")
# nx.draw(g2, pos=pos2, with_labels=True, font_color="white")
# plt.show()

graph_balanced = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2, 8, 9],
    5: [2, 10, 11],
    6: [3, 12, 13],
    7: [3, 14, 15],
    8: [4],
    9: [4],
    10: [5],
    11: [5],
    12: [6],
    13: [6],
    14: [7],
    15: [7]
}
graph_unbalanced = {
    1: [2, 3, 7],
    2: [1, 4],
    3: [1, 8],
    4: [2, 5],
    5: [4, 6],
    6: [5, 15, 16],
    7: [1, 9, 13],
    8: [3, 10],
    9: [7, 11, 12],
    10: [8],
    11: [9, 14],
    12: [9],
    13: [7],
    14: [11],
    15: [6],
    16: [6]
}

# Run the DFS algorithm and print the result
dfs_balanced = dfs(graph_balanced, 1, 15)
bfs_balanced = bfs(graph_balanced, 1, 15)
dfs_unbalanced = dfs(graph_unbalanced, 1, 15)
bfs_unbalanced = bfs(graph_unbalanced, 1, 15)

def time_algorithms():
  random.seed(4)
  nodes_balanced = [random.randint(1, 15) for _ in range(5)]
  print("Balanced graph nodes: " + str(nodes_balanced))

  random.seed(3)
  nodes_unbalanced = [random.randint(1, 16) for _ in range(5)]
  print("Unbalanced graph nodes: " + str(nodes_unbalanced))

  num_nodes = [1, 2, 3, 4, 5]
  dfs_times_balanced = {n: {'time': 0, 'count': 0} for n in num_nodes}
  bfs_times_balanced = {n: {'time': 0, 'count': 0} for n in num_nodes}
  dfs_times_unbalanced = {n: {'time': 0, 'count': 0} for n in num_nodes}
  bfs_times_unbalanced = {n: {'time': 0, 'count': 0} for n in num_nodes}

  # Measure the time taken by DFS and BFS for each node and number of nodes
  for n in num_nodes:
    for i in nodes_balanced:
        # DFS 
        start_time = time.perf_counter()
        dfs_balanced = dfs(graph_balanced, 1, i)
        end_time = time.perf_counter()
        dfs_time = end_time - start_time
        dfs_times_balanced[n]['time'] += dfs_time
        dfs_times_balanced[n]['count'] += 1
        # BFS 
        start_time = time.perf_counter()
        bfs_balanced = bfs(graph_balanced, 1, i)
        end_time = time.perf_counter()
        bfs_time = end_time - start_time
        bfs_times_balanced[n]['time'] += bfs_time
        bfs_times_balanced[n]['count'] += 1
  
    for i in nodes_unbalanced:
        # DFS 
        start_time = time.perf_counter()
        dfs_unbalanced = dfs(graph_unbalanced, 1, i)
        end_time = time.perf_counter()
        dfs_time = end_time - start_time
        dfs_times_unbalanced[n]['time'] += dfs_time
        dfs_times_unbalanced[n]['count'] += 1

        # BFS 
        start_time = time.perf_counter()
        bfs_unbalanced = bfs(graph_unbalanced, 1, i)
        end_time = time.perf_counter()
        bfs_time = end_time - start_time
        bfs_times_unbalanced[n]['time'] += bfs_time
        bfs_times_unbalanced[n]['count'] += 1
  
  # Calculate the average time taken by DFS and BFS for each number of nodes
  dfs_times_balanced = [dfs_times_balanced[n]['time'] / dfs_times_balanced[n]['count'] for n in num_nodes]
  bfs_times_balanced = [bfs_times_balanced[n]['time'] / bfs_times_balanced[n]['count'] for n in num_nodes]
  dfs_times_unbalanced = [dfs_times_unbalanced[n]['time'] / dfs_times_unbalanced[n]['count'] for n in num_nodes]
  bfs_times_unbalanced = [bfs_times_unbalanced[n]['time'] / bfs_times_unbalanced[n]['count'] for n in num_nodes]
  
  # Print the results in a table
  t = prettytable.PrettyTable(['Graph / n', *num_nodes])
  t.add_row(['DFS Balanced', *dfs_times_balanced])
  t.add_row(['BFS Balanced', *bfs_times_balanced])
  t.add_row(['DFS Unbalanced', *dfs_times_unbalanced])
  t.add_row(['BFS Unbalanced', *bfs_times_unbalanced])
  print(t)
  
  print("")

  return num_nodes, dfs_times_balanced, bfs_times_balanced, dfs_times_unbalanced, bfs_times_unbalanced

def plot_results():
    num_nodes, dfs_times_balanced, bfs_times_balanced, dfs_times_unbalanced, bfs_times_unbalanced = time_algorithms()

    x_axis = np.arange(len(num_nodes))

    # Plot results for the balanced graph
    plt.bar(x_axis - 0.2, bfs_times_balanced, 0.4, label='BFS', color='orange')
    plt.bar(x_axis + 0.2, dfs_times_balanced, 0.4, label='DFS', color='purple')

    # Plot the graph
    plt.xticks(x_axis, num_nodes)
    plt.title('Balanced graph')
    plt.xlabel('Number of searched nodes')
    plt.ylabel('Time, (s)')
    plt.legend()
    plt.show()

    # Plot results for the unbalanced graph
    plt.bar(x_axis - 0.2, bfs_times_unbalanced, 0.4, label='BFS', color='orange')
    plt.bar(x_axis + 0.2, dfs_times_unbalanced, 0.4, label='DFS', color='purple')

    # Plot the graph
    plt.xticks(x_axis, num_nodes)
    plt.title('Unbalanced graph')
    plt.xlabel('Number of searched nodes')
    plt.ylabel('Time, (s)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # time_algorithms()
    plot_results()


