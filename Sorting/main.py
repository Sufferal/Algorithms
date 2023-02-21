import random
import time
import matplotlib.pyplot as plt
import prettytable
import math

# Set the random seed for reproducibility
random.seed(666) 

# Generate a list of random integers of length n
def generate_random_list(n):
  return [random.randint(0, n) for _ in range(n)]

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
# Time the quick_sort function on a list of length n
def time_quick_sort(n):
    arr = generate_random_list(n)
    start = time.perf_counter()
    quick_sort(arr)
    end = time.perf_counter()
    return end - start

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
# Time the merge_sort function on a list of length n
def time_merge_sort(n):
    arr = generate_random_list(n)
    start = time.perf_counter()
    merge_sort(arr)
    end = time.perf_counter()
    return end - start

# Heap Sort
def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
# Time the heap_sort function on a list of length n
def time_heap_sort(n):
    arr = generate_random_list(n)
    start = time.perf_counter()
    heap_sort(arr)
    end = time.perf_counter()
    return end - start

# Introsort
def introsort(arr, depth_limit=None):
    if depth_limit is None:
        depth_limit = 2 * math.floor(math.log2(len(arr)))
    _introsort(arr, depth_limit)
def _introsort(arr, depth_limit):
    n = len(arr)
    if n <= 1:
        return
    elif depth_limit == 0:
        heap_sort(arr)
    else:
        p = partition(arr)
        _introsort(arr[:p], depth_limit - 1)
        _introsort(arr[p+1:], depth_limit - 1)
def partition(arr):
    pivot = arr[-1]
    i = -1
    for j in range(len(arr) - 1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[-1] = arr[-1], arr[i+1]
    return i+1
# Time the introsort function on a list of length n
def time_intro_sort(n):
    arr = generate_random_list(n)
    start = time.perf_counter()
    introsort(arr)
    end = time.perf_counter()
    return end - start

# List of list lengths to test
n_list = [10, 100, 1000, 10000, 25000, 50000, 100000, 150000]

# Time all three algorithms on lists of length
def print_times():
  quick_sort_times = []
  merge_sort_times = []
  heap_sort_times = []
  intro_sort_times = []

  for n in n_list:
    # Time quick_sort on a list of length n
    quick_sort_time = time_quick_sort(n)
    quick_sort_times.append(quick_sort_time)
    print(f"Quick Sort: List length = {n}; time = {quick_sort_time} seconds")

    # Time merge_sort on a list of length n
    merge_sort_time = time_merge_sort(n)
    merge_sort_times.append(merge_sort_time)
    print(f"Merge Sort: List length = {n}; time = {merge_sort_time} seconds")

    # Time heap_sort on a list of length n
    heap_sort_time = time_heap_sort(n)
    heap_sort_times.append(heap_sort_time)
    print(f"Heap Sort : List length = {n}; time = {heap_sort_time} seconds")

    # Time intro_sort on a list of length n
    intro_sort_time = time_intro_sort(n)
    intro_sort_times.append(intro_sort_time)
    print(f"Intro Sort: List length = {n}; time = {intro_sort_time} seconds")

  # Format the results
  quick_sort_times = [f"{time:.5f}" for time in quick_sort_times]
  merge_sort_times = [f"{time:.5f}" for time in merge_sort_times]
  heap_sort_times = [f"{time:.5f}" for time in heap_sort_times] 
  intro_sort_times = [f"{time:.5f}" for time in intro_sort_times]

  # Print the results in a table
  t = prettytable.PrettyTable(['Sorting Algorithm / n', *n_list])
  t.add_row(['Quick Sort', *quick_sort_times])
  t.add_row(['Merge Sort', *merge_sort_times])
  t.add_row(['Heap Sort', *heap_sort_times])
  t.add_row(['Intro Sort', *intro_sort_times])
  print(t)

# Plot the time taken by each algorithm on a graph
def plot_graphs():
  # Time each algorithm on a list of length n
  quick_sort_times = [time_quick_sort(n) for n in n_list]
  merge_sort_times = [time_merge_sort(n) for n in n_list]
  heap_sort_times = [time_heap_sort(n) for n in n_list]
  intro_sort_times = [time_intro_sort(n) for n in n_list]

  # Plot the results
  plt.plot(n_list, quick_sort_times, label="Quick Sort")
  plt.plot(n_list, merge_sort_times, label="Merge Sort")
  plt.plot(n_list, heap_sort_times, label="Heap Sort")
  plt.plot(n_list, intro_sort_times, label="Intro Sort")
  plt.title("Sorting Algorithms")
  plt.xlabel("Number of elements in a list")
  plt.ylabel("Time, (s)")
  plt.grid()
  plt.legend()
  plt.show()

def plot_graph(sort_name, sort_algo, sort_color="blue"):
  sort_times = []
  for n in n_list:
    arr = generate_random_list(n)
    start = time.perf_counter()
    sort_algo(arr)
    end = time.perf_counter()
    sort_times.append(end - start)

  plt.plot(n_list, sort_times, label=sort_name, color=sort_color)
  plt.title(sort_name)
  plt.xlabel("Number of elements in a list")
  plt.ylabel("Time, (s)")
  plt.grid()
  plt.show()

# Run the main function
if __name__ == "__main__":
  # print_times()

  plot_graphs()

  # plot_graph("Quick Sort", quick_sort, "blue")
  # plot_graph("Merge Sort", merge_sort, "orange")
  # plot_graph("Heap Sort", heap_sort, "green")
  # plot_graph("Intro Sort", introsort, "red")
