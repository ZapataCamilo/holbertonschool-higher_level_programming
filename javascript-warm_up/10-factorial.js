#!/usr/bin/node

function fac (a) {
  if (a < 0) {
    return (-1);
  } else if (a === 0 || isNaN(a)) {
    return (1);
  } return (a * fac(a - 1));
}

console.log(fac(+process.argv[2]));
