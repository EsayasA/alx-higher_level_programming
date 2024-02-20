#!/usr/bin/node
const req = require('request');
const ul = process.argv[2];
req(ul, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
