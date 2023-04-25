#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    characters.forEach(character => {
      printCharacters(character);
    })
  }
});

function printCharacters (character) {
  request(character, function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
    }
  });
}
