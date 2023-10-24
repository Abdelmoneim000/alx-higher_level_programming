#!/usr/bin/node
const fs = require('fs');
fs.readFile(argv[1], 'utf8', (err, data) => {
    console.log(data || err);
})
