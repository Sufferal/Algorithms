function fiboRecursive(n) {
  if (n <= 1) {
    return 1;
  }

  return fiboRecursive(n - 1) + fiboRecursive(n - 2);
}

function fiboDynamic(n) {
  let f = new Array(n + 2);
  let i;
  f[0] = 0;
  f[1] = 1;

  for (i = 2; i <= n; i++) {
    f[i] = f[i - 1] + f[i - 2];
  }

  return f[n];
}
