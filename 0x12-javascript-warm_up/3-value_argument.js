#!/usr/bin/node
// Prints message based on no. of arguments

const [,, ...args] = process.argv;

if (args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
