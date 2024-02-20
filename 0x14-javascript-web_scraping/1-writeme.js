#!/usr/bin/node
const fs = require('fs');
const f = process.argv[2];
const content = process.argv[3];
fs.writeFile(f, content, 'utf-8', function (error) {
  if (error) {
    console.log(error);
  }
});
