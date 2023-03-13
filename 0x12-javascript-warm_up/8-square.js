#!/usr/bin/node
const arg = parseInt(process.argv[2]);
if (!arg) console.log('Missing size');
else if (arg < 1) ;
else {
  for (let i = 0; i < arg; i++) {
    console.log(new Array(arg).fill('X').join(''));
  }
}
