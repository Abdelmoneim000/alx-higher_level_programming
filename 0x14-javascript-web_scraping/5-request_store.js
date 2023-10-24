#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');
const request = require('request');

// The URL for the Star Wars films API
const url = argv[2];

// Send a GET request to the API
request.get(url, (err, response) => {
    if(err)
    {
        throw err;
    }
    else
    {
        const bod = response.body;
        fs.writeFile(argv[3], bod, (err) => {
            err ? console.log(err) : err;
        });
    }
});
