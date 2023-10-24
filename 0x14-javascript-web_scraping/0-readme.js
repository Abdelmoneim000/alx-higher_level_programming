#!/usr/bin/env node
const fs = require('fs');
const { argv } = require('process');
fs.readFile(argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
