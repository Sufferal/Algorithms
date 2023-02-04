function fiboRecursive(n) {
  if (n <= 1) {
    return 1;
  }

  return fiboRecursive(n - 1) + fiboRecursive(n - 2);
}
