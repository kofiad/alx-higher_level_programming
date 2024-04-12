#!/usr/bin/node
/**
 * class Rectangle that defines a rectangle
 * constructor takes 2 arguments: w and h
 * If w or h is equal to 0 or not a positive integer, create an empty object
 * an instance method called print() that prints the rectangle using the character X
 * an instance method called rotate() that exchanges the width and the height of the rectangle
 * an instance method called double() that multiples the width and the height of the rectangle by 2
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
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const holder = this.height;
    this.height = this.width;
    this.width = holder;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
