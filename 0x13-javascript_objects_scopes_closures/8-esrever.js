#!/usr/bin/node
exports.esrever = function (list) {
  const rlist = [];

  for (let i = 0; i < list.length; i++) {
    rlist[i] = list[list.length - i - 1];
  }
  return (rlist);
};
