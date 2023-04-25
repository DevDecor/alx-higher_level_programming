#!/usr/bin/node
// Reads the content of a file
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, data, body) => {
  if (err) return console.log(err);
  console.log(JSON.parse(body).title);
});
