#!/usr/bin/node
/**
 *  a function that returns the number of occurrences in a list
 * @param {list} list              list of interest
 * @param {number} searchElement   element on interest
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
