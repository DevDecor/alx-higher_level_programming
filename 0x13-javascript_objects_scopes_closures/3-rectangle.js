#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!h || !w || w < 1 || h < 1) return;
    this.width = w;
    this.height = h;
  }

  print () {
    const row = new Array(this.width).fill('X').join('');
    for (let i = 0; i < this.height; i++) console.log(row);
  }
}
module.exports = Rectangle;
