#!/usr/bin/env node
const request = require('request');
const { argv } = require('process');

request.get(`https://swapi-api.alx-tools.com/api/films/${argv[2]}/`,
  (error, response) => {
    error ? console.log(error) : console.log(`${JSON.parse(response.body).title}`);
  });
