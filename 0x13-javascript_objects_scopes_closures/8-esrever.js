#!/usr/bin/node
/**
 * a function that returns the reversed version of a list
 * @param {list} list list of interest
 */
exports.esrever = function (list) {
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return (reversedList);
};
