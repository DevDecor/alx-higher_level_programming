#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!h || !w || w < 1 || h < 1) return;
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
