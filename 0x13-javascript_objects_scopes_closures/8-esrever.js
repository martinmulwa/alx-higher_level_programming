#!/usr/bin/node

exports.esrever = function (list) {
  const n = list.length;
  let tmp;

  for (let i = 0; i < n / 2; i++) {
    tmp = list[i];
    list[i] = list[n - i - 1];
    list[n - i - 1] = tmp;
  }

  return list;
};
