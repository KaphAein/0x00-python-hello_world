#!/usr/bin/node
const dict = require('./101-data.js').dict;
let newDict = {};

for (const key in dict) {
  const value = dict[key];
  newDict[value] = [];
}
for (const key in dict) {
  const value = dict[key];
  newDict[value].push(key);
}
for (const key in newDict) {
  newDict[key].sort((a, b) => a - b);
}
console.log(newDict);
