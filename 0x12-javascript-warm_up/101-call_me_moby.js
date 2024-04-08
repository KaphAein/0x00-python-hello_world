#!/usr/bin/node
// function that executes x times a function.

module.export.callMeMoby = function (x, theFunction) {
  for(let i = 0; i < x; i++) {
     theFunction();
  }
};
