#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

// The URL for the Star Wars films API
const url = argv[2];

// Send a GET request to the API
request.get(url, (err, response) => {
  if (!err) {
    const films = JSON.parse(response.body).results;
    let count = 0;

    for (const film of films) {
      if (film.characters.includes(
        'https://swapi-api.alx-tools.com/api/people/18/'
      )) {
        count += 1;
      }
    }

    console.log(count);
  }
});
