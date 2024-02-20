#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((c, mo) => {
      return mov.cha.find((cha) => cha.endsWith('/18/'))
        ? c + 1
        : c;
    }, 0));
  }
});
