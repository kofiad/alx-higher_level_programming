#!/usr/bin/node
/**
 * a function that prints the number of arguments already printed and the new argument value.
 * @param {string} item new argument value
 */
let count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count += 1;
};
