#!/usr/bin/node

// Get the command-line arguments
const args = process.argv.slice(2);

// Check if any commandline arguments were passed
if (args.length > 0) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
