import math
import time
import matplotlib.pyplot as plt

# Eratosthenes Sieve
def algorithm_1(n):
    c = [True] * (n+1)
    c[1] = False
    i = 2
    while (i <= n):
        if (c[i] == True):
            j = 2*i
            while (j <= n):
                c[j] = False
                j = j+i
        i = i+1
    return c

# Simplified version of algorithm_1 
# does not check for already marked composite numbers
# no need to check if c[i] == True
def algorithm_2(n):
    c = [True] * (n+1)
    c[1] = False
    i = 2
    while (i <= n):
        j = 2*i
        while (j <= n):
            c[j] = False
            j = j+i
        i = i+1
    return c

# Eliminates composite numbers by marking their multiples
def algorithm_3(n):
    c = [True] * (n+1)
    c[1] = False
    i = 2
    while (i <= n):
        if (c[i] == True):
            j = i+1
            while (j <= n):
                if (j % i == 0):
                    c[j] = False
                j = j+1
        i = i+1
    return c

# Checks each number from 2 to n-1 to see if it is a factor of n
def algorithm_4(n):
    c = [True] * (n+1)
    c[1] = False
    i = 2
    while (i <= n):
        j = 1
        while (j < i):
            if (i % j == 0):
                c[i] = False
            j = j+1
        i = i+1
    return c

# Checks each number from 2 to the square root of n to see if it is a factor of n.
def algorithm_5(n):
    c = [True] * (n+1)
    c[1] = False
    i = 2
    while (i <= n):
        j = 2
        while (j <= math.sqrt(i)):
            if (i % j == 0):
                c[i] = False
            j = j+1
        i = i+1
    return c

# Measure execution time for different values of n
n_list = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

# Plot graph for a single algorithm
def plot_graph(algo_name, algo_func, algo_color="blue"):
  algo_times = []
  for n in n_list:
    start = time.perf_counter()
    algo_func(n)
    end = time.perf_counter()
    algo_times.append(end - start)

  plt.plot(n_list, algo_times, label=algo_name, color=algo_color)
  plt.title(algo_name)
  plt.xlabel("Number of elements in the list, (n)")
  plt.ylabel("Time, (s)")
  plt.grid()
  plt.show()

# Plot the results
def plot_graphs():
  times_1 = [] 
  times_2 = []
  times_3 = []
  times_4 = []
  times_5 = []

  # Run the algorithms and time them
  for n in n_list:
    t1_start = time.perf_counter()
    algorithm_1(n)
    t1_end = time.perf_counter()

    t2_start = time.perf_counter()
    algorithm_2(n)
    t2_end = time.perf_counter()

    t3_start = time.perf_counter()
    algorithm_3(n)
    t3_end = time.perf_counter()

    t4_start = time.perf_counter()
    algorithm_4(n)
    t4_end = time.perf_counter()

    t5_start = time.perf_counter()
    algorithm_5(n)
    t5_end = time.perf_counter()

    times_1.append(t1_end - t1_start)
    times_2.append(t2_end - t2_start)
    times_3.append(t3_end - t3_start)
    times_4.append(t4_end - t4_start)
    times_5.append(t5_end - t5_start)

  plt.plot(n_list, times_1, label='Algorithm 1')
  plt.plot(n_list, times_2, label='Algorithm 2')
  plt.plot(n_list, times_3, label='Algorithm 3')
  plt.plot(n_list, times_4, label='Algorithm 4')
  plt.plot(n_list, times_5, label='Algorithm 5')
  plt.xlabel('Number of elements in the list, (n)')
  plt.ylabel('Time, (s)')
  plt.title('Eratosthenes Sieve Algorithms')
  plt.legend()
  plt.grid()
  plt.show()

# Run the main function
if __name__ == "__main__":
  # plot_graph("Algorithm 1", algorithm_1, "blue")
  # plot_graph("Algorithm 2", algorithm_2, "orange")
  # plot_graph("Algorithm 3", algorithm_3, "green")
  # plot_graph("Algorithm 4", algorithm_4, "red")
  # plot_graph("Algorithm 5", algorithm_5, "purple")
  plot_graphs()
