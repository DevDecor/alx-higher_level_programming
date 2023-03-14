#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!h || !w || w < 1 || h < 1) return;
    this.height = h;
    this.width = w;
  }
}
module.exports = Rectangle;
