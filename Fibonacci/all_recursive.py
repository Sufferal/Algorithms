import matplotlib.pyplot as plt
import a01_recursive, a02_dynamic, a03_matrix_, a03_matrix_optimized, a04_binet, a05_spacetime, a06_modulo

if __name__ == "__main__":
  values = [6, 7, 8, 10, 11, 14, 16, 18, 19, 20, 22, 24, 25, 28, 33, 34, 35, 37, 39, 40]
  
  recursive_time_arr = [a01_recursive.get_time_fibonum(i) for i in values]
  dynamic_time_arr = [a02_dynamic.get_time_fibonum(i) for i in values]
  matrix_time_arr = [a03_matrix_.get_time_fibonum(i) for i in values]
  matrix_optimized_arr = [a03_matrix_optimized.get_time_fibonum(i) for i in values]
  binet_time_arr = [a04_binet.get_time_fibonum(i) for i in values]
  space_time_arr = [a05_spacetime.get_time_fibonum(i) for i in values]
  modulo_time_arr = [a06_modulo.get_time_fibonum(i) for i in values]

  for i in range(len(values)):
    print(values[i], '->', dynamic_time_arr[i])

  plt.plot(values, recursive_time_arr, color = 'red', label="Recursive")
  plt.plot(values, dynamic_time_arr, color = 'orange', label="Dynamic")
  plt.plot(values, matrix_time_arr, color = 'yellow', label="Matrix")
  plt.plot(values, matrix_optimized_arr, color = 'green', label="Matrix Optimized")
  plt.plot(values, binet_time_arr, color = 'blue', label="Binet")
  plt.plot(values, space_time_arr, color = 'violet', label="Spacetime")
  plt.plot(values, modulo_time_arr, color = 'brown', label="Modulo")
  plt.xlabel('n-th Fibonacci Term')
  plt.ylabel('Time, s')
  plt.title('All Other Algorithms vs Recursive')
  plt.grid(True)
  plt.legend()
  plt.show()
  

