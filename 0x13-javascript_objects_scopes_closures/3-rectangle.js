#!/usr/bin/node
/**
 * class Rectangle that defines a rectangle
 * constructor takes 2 arguments: w and h
 * If w or h is equal to 0 or not a positive integer, create an empty object
 * an instance method called print() that prints the rectangle using the character X
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

  print () {
    for (let i = 0; i <= this.height; i++) {
      let row = '';
      for (let j = 0; j <= this.width; j++) {
        row += '#';
      }
      console.log(row);
    }
  }
}
module.exports = Rectangle;
