#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error1, ans, body) {
  if (!error1) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, j) {
  request(characters[j], function (error1, ans, body) {
    if (!error1) {
      console.log(JSON.parse(body).name);
      if (j + 1 < characters.length) {
        printCharacters(characters, j + 1);
      }
    }
  });
}
