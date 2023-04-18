#!/usr/bin/node
exports.esrever = function (list) {
  const li = [];
  for (let i = list.length - 1; i >= 0; i--) {
    li.push(list[i]);
  }
  return li;
};
