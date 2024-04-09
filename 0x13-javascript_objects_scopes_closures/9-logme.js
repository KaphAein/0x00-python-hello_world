#!/usr/bin/node
exports.logMe = function (item) {
  let n = 0;
  return function(itemn) { console.log(n++ + ': ' + item); };
};
