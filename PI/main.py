import math
import prettytable
import time
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

def Bailey_Borwein_Plouffe(n):
    getcontext().prec = n + 10   
    
    pi = Decimal(0)
    k = 0
    while k <= n:
        pi += (Decimal(1)/(16**k)) * ((Decimal(4)/(8*k+1)) - (Decimal(2)/(8*k+4)) - (Decimal(1)/(8*k+5)) - (Decimal(1)/(8*k+6)))
        k += 1

    return str(pi)[n]

def Bellard(n):
    getcontext().prec = n + 10   # Set precision to get accurate results

    digit = Decimal(0)
    k = 0
    while k <= n:
        a = Decimal(1) / Decimal(16) ** k
        b1 = Decimal(4) / (Decimal(8) * k + Decimal(1))
        b2 = Decimal(2) / (Decimal(8) * k + Decimal(4))
        b3 = Decimal(1) / (Decimal(8) * k + Decimal(5))
        b4 = Decimal(1) / (Decimal(8) * k + Decimal(6))
        term = a * (b1 - b2 - b3 - b4)

        digit += term
        k += 1

    digit = int(digit * Decimal(10)**n) % 10

    return digit

def Gauss_Legendre(n):
    getcontext().prec = n + 10  
    
    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)
    
    for _ in range(n):
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - a_next)**2
        a = a_next
        p *= 2
    
    pi = (a + b)**2 / (4 * t)
    
    return str(pi)[n]  
    # return str(pi)[0:n+1]  

# Usage example
n_th_digit_list = [5, 50, 100, 500, 1000, 5000]
BBB_times = []
Gauss_Legendre_times = []
Bellard_times = []

for n_th_digit in n_th_digit_list:
    # Bailey_Borwein_Plouffe
    start_time = time.perf_counter()
    result = Bailey_Borwein_Plouffe(n_th_digit)
    end_time = time.perf_counter()
    BBB_times.append(end_time - start_time)

    # Gauss_Legendre
    start_time = time.perf_counter()
    result = Gauss_Legendre(n_th_digit)
    end_time = time.perf_counter()
    Gauss_Legendre_times.append(end_time - start_time)

    # Bellard
    start_time = time.perf_counter()
    result = Bellard(n_th_digit)
    end_time = time.perf_counter()
    Bellard_times.append(end_time - start_time)

def plot_graph(times, label):
  plt.plot(n_th_digit_list, times, label=label)
  plt.xlabel('N-th digit')
  plt.ylabel('Time, (s)')
  plt.title(label)
  plt.legend()
  plt.grid()
  plt.show()

def plot_graphs():
  plt.plot(n_th_digit_list, BBB_times, label='Bailey Borwein Plouffe')
  plt.plot(n_th_digit_list, Gauss_Legendre_times, label='Gauss Legendre')
  plt.plot(n_th_digit_list, Bellard_times, label='Bellard')
  plt.xlabel('N-th digit')
  plt.ylabel('Time, (s)')
  plt.title('All PI Algorithms')
  plt.legend()
  plt.grid()
  plt.show()

def print_results():
  # Format the results
  global BBB_times, Gauss_Legendre_times, Bellard_times

  BBB_times = [f"{time:.5f}" for time in BBB_times]
  Gauss_Legendre_times = [f"{time:.5f}" for time in Gauss_Legendre_times]
  Bellard_times = [f"{time:.5f}" for time in Bellard_times]

  # Print the results in a table
  t = prettytable.PrettyTable(['Algorithm / n', *n_th_digit_list])
  t.add_row(['Bailey Borwein Plouffe', *BBB_times])
  t.add_row(['Gauss Legendre', *Gauss_Legendre_times])
  t.add_row(['Bellard', *Bellard_times])
  print(t)

if __name__ == '__main__':
    # plot_graph(BBB_times, 'Bailey Borwein Plouffe')
    # plot_graph(Gauss_Legendre_times, 'Gauss Legendre')
    # plot_graph(Bellard_times, 'Bellard')
    # plot_graphs()
    print_results()

