#!/usr/bin/node
/**
 * class Rectangle that defines a rectangle
 * constructor takes 2 arguments w and h
 * If w or h is equal to 0 or not a positive integer, create an empty object
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      Object.assign(this, {});
    }
  }
}
module.exports = Rectangle;
