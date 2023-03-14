#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!h || !w || w < 1 || h < 1) return;
    this.height = h;
    this.width = w;
  }

  print () {
    const row = new Array(this.width).fill('X').join('');
    for (let i = 0; i < this.height; i++) console.log(row);
  }
}
module.exports = Rectangle;
