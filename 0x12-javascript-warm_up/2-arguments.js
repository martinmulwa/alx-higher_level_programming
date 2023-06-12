#!/usr/bin/node

// Get the command-line arguments
const args = process.argv.slice(2);
const numArgs = args.length;

// Check if any commandline arguments were passed
if (numArgs === 0) {
  console.log('No argument');
} else if (numArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
