#!/usr/bin/node
// function that executes x times a function.

exports.addMeMaybe = function (number, theFunction) {
  for (let i = 0; i < number; i++) {
    number++;
    theFunction(number);
  }
};
