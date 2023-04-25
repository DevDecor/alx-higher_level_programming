#!/usr/bin/node
// Reads the content of a file
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], { encoding: 'utf-8' }, (err) => {
  if (err) return console.log(err);
});
