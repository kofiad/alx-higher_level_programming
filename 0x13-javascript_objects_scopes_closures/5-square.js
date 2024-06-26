#!/usr/bin/node
/**
 * class Square that defines a square and inherits from Rectangle of 4-rectangle.js
 * constructor takes 1 argument: size
 * constructor of Rectangle must be called (by using super())
 */
const Rectangle = require('./4-rectangle.js');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
