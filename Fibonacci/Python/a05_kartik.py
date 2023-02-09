import time
import matplotlib.pyplot as plt

def fibonacci(n):
    if n > 0:
        n1, n2 = 1, 1
        if n > 3:
            for _ in range((n//3)):
                # << 2 => multiply by 4
                n1, n2 = n2, (n2 << 2)+n1  
        if n % 3 == 0:
            return n1
        elif n % 3 == 1:
            # >> 1   is divide by 2  'F1'
            return (n2 - n1) >> 1  
        elif n % 3 == 2:
             # >> 1   is divide by 2  'F2'
            return (n2 + n1) >> 1 
    else:
        return -1

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
  
  plt.plot(values, time_arr,  color = 'violet', marker = 'o', markersize = 5, 
          markeredgecolor = 'black', markerfacecolor = 'none')
  plt.xlabel('n-th Fibonacci Term')
  plt.ylabel('Time, s')
  plt.title('Kartik Algorithm')
  plt.grid(True)
  plt.show()
  