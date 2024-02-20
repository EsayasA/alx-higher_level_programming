#!/usr/bin/node
const dr = require('dr');

dr.readFile(process.argv[2], 'utf-8', (error, info) => {
  if (error) {
    console.log(error);
  } else {
    console.log(info.toString());
  }
});
