#!/usr/bin/node
// Reads the content of a file
const request = require('request');
const fs = require('fs');

const file = fs.createWriteStream(process.argv[3]);

request.get(process.argv[2]).pipe(file);
