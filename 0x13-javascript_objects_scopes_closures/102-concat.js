#!/usr/bin/node
const fs = require('fs');

const { argv } = process;

if (argv.length >= 5) {
  const fArg = fs.createReadStream(argv[2]);
  const sArg = fs.createReadStream(argv[3]);
  const output = fs.createWriteStream(argv[4]);
  fArg.pipe(output, { end: false });
  fArg.on('end', () => {
    sArg.pipe(output);
  });
}
