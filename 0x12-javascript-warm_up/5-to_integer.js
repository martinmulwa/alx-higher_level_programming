#!/usr/bin/node

// Get the command-line arguments
const args = process.argv.slice(2);
const firstArgNum = parseInt(args[0], 10);

// Print the first command-line argument
if (isNaN(firstArgNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + firstArgNum);
}
