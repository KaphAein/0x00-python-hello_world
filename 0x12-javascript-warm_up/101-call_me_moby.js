#!/usr/bin/node
// function that executes x times a function.

export.callMeMoby = function (x, theFunction) {
  for(let i = 0; i < x; i++) {
     theFunction();
  }
};
