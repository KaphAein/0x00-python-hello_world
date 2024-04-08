#!/usr/bin/node
// prints My number: <first argument converted in integer>

const [,, ...args] = process.argv;

if (isNaN(parseInt(args[0]))) {
  console.log('Missing number of occurrences');
} else {
	for (let i = 0;
    console.log('C is fun' * parseInt(args[0]))
}
