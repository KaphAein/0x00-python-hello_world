#!/usr/bin/node
// Prints message based on no. of arguments

const numArgs = process.argv.length;

if (numArgs === 0) {
    console.log('No argument');
} else if (numArgs === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
