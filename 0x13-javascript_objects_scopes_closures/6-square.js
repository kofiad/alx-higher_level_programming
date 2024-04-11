#!/usr/bin/node
/**
 * class Square that defines a square and inherits from Square of 5-square.js
 * an instance method called charPrint(c) that prints the rectangle using the character c
 * If c is undefined, use the character X
 */
const Square0 = require('./5-square');
class Square extends Square0 {
  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
