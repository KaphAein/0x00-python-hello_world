#!/usr/bin/node
// Prints message based on no. of arguments

const [,, ...args] = process.argv;

console.log(args[0] + ' is ' + args[1]);
