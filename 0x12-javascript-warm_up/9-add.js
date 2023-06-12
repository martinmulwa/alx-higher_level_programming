#!/usr/bin/node

// Get the command-line arguments
const args = process.argv.slice(2);
const firstNum = parseInt(args[0], 10);
const secondNum = parseInt(args[1], 10);

function add (a, b) {
  return a + b;
}

// Print sum of the first 2 command-line arguments
console.log(add(firstNum, secondNum));
