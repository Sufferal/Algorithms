import networkx as nx
import collections
import matplotlib.pyplot as plt

# Define the DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start, end=" ")

    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)
    return visited

# Define the BFS algorithm
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
  
    return visited

# # Create a graph
# G = nx.Graph()
# G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])
# # Set the seed for the random number generator
# seed = 1

# # Draw the graph
# pos = nx.spring_layout(G, seed)
# nx.draw(G, with_labels=True, font_color="white")
# # Show the graph
# plt.show()

graph_1 = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2],
    5: [2],
    6: [3],
    7: [3]
}

# Run the DFS algorithm and print the result
dfs_result = dfs(graph_1, 1)
print("\nDFS result:", dfs_result)
# Run the BFS algorithm and print the result
bfs_result = bfs(graph_1, 1)
print("\nBFS result:", bfs_result)


