#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) return this.print();
    for (let i = 0; i < this.width; i++) {
      console.log(new Array(this.width).fill(c).join(''));
    }
  }
}

module.exports = Square;
