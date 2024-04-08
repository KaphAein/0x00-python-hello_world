#!/usr/bin/node
// prints My number: <first argument converted in integer>

function add (a, b) {
  return (parseInt(a) + parseInt(b));
}

const [,, arg1, arg2] = process.argv;

console.log(add(arg1, arg2));
