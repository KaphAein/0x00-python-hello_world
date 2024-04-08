#!/usr/bin/node
// searches the second biggest integer in the list of arguments.
const (,, ...args) = process.argv;

if (args <= 1) {
  console.log(0);
} else {
  const list = args.sort();
  console.log(list.reverse()[1]);
}
