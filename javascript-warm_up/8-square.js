#!/usr/bin/node

if (!process.argv[2]) {
  console.log('Missing size');
} else if (!parseInt(process.argv[2], 10)) {
  console.log('Missing size');
}
for (let i = 0; i < process.argv[2]; i++) {
  console.log('x'.repeat(process.argv[2]));
}
