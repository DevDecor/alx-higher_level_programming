#!/usr/bin/node
// Reads the content of a file
const request = require('request');

request(process.argv[2], (err, data) => {
  if (err) return console.log(`code ${err.status}`, err);
  console.log(data.statusCode);
});
