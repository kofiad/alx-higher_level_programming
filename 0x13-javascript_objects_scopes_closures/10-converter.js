#!/usr/bin/node
/**
 * a function that converts a number from base 10 to another base passed as argument
 * @param {number} base base to be converted to
 */
exports.converter = function (base) {
  function toBase (n) {
    return n.toString(base);
  }
  return toBase;
};
