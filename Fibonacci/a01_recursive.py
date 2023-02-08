import time
import matplotlib.pyplot as plt

def fibonacci(n):
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

def get_time_fibonum(num):
  start = time.perf_counter()
  fibonacci(num)
  end = time.perf_counter()
  return end - start 
 
if __name__ == "__main__":
  values = [6, 7, 8, 10, 11, 14, 16, 18, 19, 20, 22, 24, 25, 28, 33, 34, 35, 37, 39, 40]
  time_arr = []

  for i in values:
    time_arr.append(get_time_fibonum(i))

  # for i in range(len(values)):
  #   print(values[i], '->', time_arr[i])

  plt.plot(values, time_arr,  color='red', marker='o', markersize=6, 
          markeredgecolor='black', markerfacecolor='none')
  plt.xlabel('n-th Fibonacci Term')
  plt.ylabel('Time, s')
  plt.title('Recursive Algorithm')
  plt.grid(True)
  plt.show()
  