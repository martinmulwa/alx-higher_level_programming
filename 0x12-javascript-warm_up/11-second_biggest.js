#!/usr/bin/node

// Get the command-line arguments
const args = process.argv.slice(2);

// Sort the commandline arguments in descending order
const sortedArgs = args.map(arg => parseInt(arg)).sort((a, b) => b - a);

// Get the second largest command-line argument
const secondLargest = sortedArgs.length > 1 ? sortedArgs[1] : 0;

console.log(secondLargest);
