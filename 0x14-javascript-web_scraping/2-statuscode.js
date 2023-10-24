#!/usr/bin/env node
const request = require('request');
const { argv } = require('process');

request.get(argv[2], (error, response) => {
  error ? console.log(error) : console.log(`code: ${response.statusCode}`);
});
