#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let v = '';
      for (let j = 0; j < this.width; j++) {
        v += 'X';
      }
      console.log(v);
    }
  }

  rotate () {
    const space = this.width;
    this.width = this.height;
    this.height = space;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
