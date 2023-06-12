#!/usr/bin/node

// Get the command-line arguments
const args = process.argv.slice(2);
const firstArgNum = parseInt(args[0], 10);
let num = firstArgNum;

// Check if the first argument is a number
if (isNaN(num)) {
  console.log('Missing number of occurrences');
  num = 0;
}

// Print 'C is fun' num times
for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
