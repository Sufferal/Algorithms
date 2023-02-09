import time
import matplotlib.pyplot as plt

def fibonacci(n):
  f = [0, 1] 

  for i in range(2, n + 1):
    f.append(f[i - 1] + f[i - 2])

  return f[n]

def get_time_fibonum(num):
  start = time.perf_counter()
  fibonacci(num)
  end = time.perf_counter()
  return end - start
 
if __name__ == "__main__":
  values = [2006, 2026, 2546, 3998, 5568, 8768, 9577, 12409, 14557, 14827, 23497, 24253, 27233,
            38982, 39359, 40879, 47018, 56137, 64163, 88847]
  time_arr = []
  
  for i in values:
    time_arr.append(get_time_fibonum(i))
  
  for i in range(len(values)):
    print(values[i], '->', time_arr[i])
  
  plt.plot(values, time_arr,  color = 'orange', marker = 'o', markersize = 5, 
          markeredgecolor = 'black', markerfacecolor = 'none')
  plt.xlabel('n-th Fibonacci Term')
  plt.ylabel('Time, s')
  plt.title('Dynamic Programming Algorithm')
  plt.grid(True)
  plt.show()
  