#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!h || !w || w < 1 || h < 1) return;
    this.width = w;
    this.height = h;
  }

  print () {
    if (!this.height || !this.width) return;
    const row = new Array(this.width).fill('X').join('');
    for (let i = 0; i < this.height; i++) console.log(row);
  }

  rotate () {
    const x = this.height;
    this.height = this.width;
    this.width = x;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
