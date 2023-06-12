#!/usr/bin/node

// Get the command-line arguments
const args = process.argv.slice(2);
let num = parseInt(args[0], 10);
num = isNaN(num) ? 0 : num;

function factorial (n) {
  if (n <= 1) {
    return 1;
  }

  return n * factorial(n - 1);
}

// Print factorial of the first command-line argument
console.log(factorial(num));
