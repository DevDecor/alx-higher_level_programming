#!/usr/bin/node
module.exports.converter = function (base) {
  return function (n) {
    return n.toString(base);
  };
};
