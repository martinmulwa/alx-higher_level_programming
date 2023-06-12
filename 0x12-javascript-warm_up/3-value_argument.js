#!/usr/bin/node

// Get the command-line arguments
const args = process.argv.slice(2);
const firstArg = args[0];

// Print the first commandline argument if it exists
if (firstArg) {
  console.log(firstArg);
} else {
  console.log('No argument');
}
