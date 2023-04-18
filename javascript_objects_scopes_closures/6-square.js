#!/usr/bin/node
const square = require('./5-square');

module.exports = class Square extends square {
  charPrint (c) {
    if (typeof (c) !== 'string') {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let space = '';
      for (let s = 0; s < this.width; s++) {
        space += c;
      }
      console.log(space);
    }
  }
};
