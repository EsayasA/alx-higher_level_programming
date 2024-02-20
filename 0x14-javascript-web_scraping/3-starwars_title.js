#!/usr/bin/node

const ask = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];
ask.get(url + id, function (error, ans, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
