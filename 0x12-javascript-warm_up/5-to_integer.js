#!/usr/bin/node
// prints My number: <first argument converted in integer>

const [,, ...args] = process.argv;

if (isNaN(parseInt(args[0]))) {
    console.log('Not a number')
} else {
    console.log(parseInt(args[0]))
