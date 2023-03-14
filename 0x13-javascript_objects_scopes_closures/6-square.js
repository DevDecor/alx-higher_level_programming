#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) return this.print();
    for (let i = 0; i < this.width; i++) {
      console.log(new Array(this.width).fill(c).join(''));
    }
  }
}

module.exports = Square;
