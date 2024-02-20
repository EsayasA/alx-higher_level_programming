#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
req.get(url + id, function (error1, ans, body) {
  if (error1) {
    console.log(error1);
  }
  const data = JSON.parse(body);
  const xx = data.characters;
  for (const k of xx) {
    req.get(k, function (error1, ans, body1) {
      if (error1) {
        console.log(error1);
      }
      const da1 = JSON.parse(body1);
      console.log(da1.name);
    });
  }
});
