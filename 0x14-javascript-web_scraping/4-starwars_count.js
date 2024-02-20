#!/usr/bin/node
const req = require('request');
req(process.argv[2], function (err, res, body) {
  if (!err) {
    const result = JSON.parse(body).result;
    console.log(result.reduce((c, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? c + 1
        : c;
    }, 0));
  }
});
