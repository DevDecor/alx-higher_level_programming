#!/usr/bin/node

function factorial (n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}

const arg1 = parseInt(process.argv[2]);
if (!arg1) console.log(1);
else {
  console.log(factorial(arg1));
}
