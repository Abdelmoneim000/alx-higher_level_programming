#!/usr/bin/node
const fs = require('fs');
const {argv} = require('process');
fs.readFile(argv[2], 'utf8', (err, data) => {
    console.log(data || err);
})
