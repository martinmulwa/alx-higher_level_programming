#!/usr/bin/node

// Get the command-line arguments
const args = process.argv.slice(2);
const firstArgNum = parseInt(args[0], 10);
let num = firstArgNum;

// Check if the first argument is a number
if (isNaN(num)) {
  console.log('Missing size');
  num = 0;
}

// Print square of X's
for (let i = 0; i < num; i++) {
  console.log('X'.repeat(num));
}
