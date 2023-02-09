import time
import matplotlib.pyplot as plt

def fibonacci(n):
    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)
     
    return F[0][0]
 
def multiply(F, M):
 
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])
     
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w
 
def power(F, n):
 
    M = [[1, 1],
         [1, 0]]
 
    for i in range(2, n + 1):
        multiply(F, M)
 
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
    
  plt.plot(values, time_arr,  color = 'red', marker = 'o', markersize = 5, 
          markeredgecolor = 'black', markerfacecolor = 'none')
  plt.xlabel('n-th Fibonacci Term')
  plt.ylabel('Time, s')
  plt.title('Matrix Power Algorithm')
  plt.grid(True)
  plt.show()
  