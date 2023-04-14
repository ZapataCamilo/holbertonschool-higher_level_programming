#!/usr/bin/node

const numArg = process.argv.slice(2);
const number = parseInt(numArg, 10);

if (!numArg[0]) {
  console.log('Not a number');
} else if (isNaN(number) === true) {
  console.log('Not a number');
} else if (typeof number === 'number') {
  console.log('My number: ', number);
}
