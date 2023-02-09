import a01_recursive, a02_dynamic, a03_matrix_optimized, a04_binet, a05_spacetime, a06_modulo

x = 100

print(a02_dynamic.fibonacci(x), a03_matrix_optimized.fibonacci(x),
      a04_binet.fibonacci(x), a05_spacetime.fibonacci(x), a06_modulo.fibonacci(x))

print(a02_dynamic.get_time_fibonum(40))