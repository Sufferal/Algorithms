import matplotlib.pyplot as plt
import a02_dynamic, a03_matrix_, a03_matrix_optimized, a04_binet, a05_spacetime, a06_modulo

if __name__ == "__main__":
  values = [2006, 2026, 2546, 3998, 5568, 8768, 9577, 12409, 14557, 14827, 23497, 24253, 27233,
            38982, 39359, 40879, 47018, 56137, 64163, 88847]
  
  dynamic_time_arr = [a02_dynamic.get_time_fibonum(i) for i in values]
  matrix_time_arr = [a03_matrix_.get_time_fibonum(i) for i in values]
  matrix_optimized_arr = [a03_matrix_optimized.get_time_fibonum(i) for i in values]
  binet_time_arr = [a04_binet.get_time_fibonum(i) for i in values]
  space_time_arr = [a05_spacetime.get_time_fibonum(i) for i in values]
  mod_time_arr = [a06_modulo.get_time_fibonum(i) for i in values]

  

  plt.plot(values, dynamic_time_arr, color = 'orange', label="Dynamic")
  plt.plot(values, matrix_time_arr, color = 'red', label="Matrix")
  plt.plot(values, matrix_optimized_arr, color = 'green', label="Matrix Optimized")
  plt.plot(values, binet_time_arr, color = 'blue', label="Binet")
  plt.plot(values, space_time_arr, color = 'violet', label="Space")
  plt.plot(values, mod_time_arr, color = 'brown', label="Modulo")
  plt.xlabel('n-th Fibonacci Term')
  plt.ylabel('Time, s')
  plt.title('All Algorithms')
  plt.grid(True)
  plt.legend()
  plt.show()
  

