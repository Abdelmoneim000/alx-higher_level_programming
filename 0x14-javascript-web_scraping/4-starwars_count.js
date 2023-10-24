#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

// The URL for the Star Wars films API
const url = argv[2];

// Send a GET request to the API
request.get(url, (err, response) => {
  if (err) {
    console.error(err);
  } else {
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

/*
// Initialize a count variable
let count = 0;

// Check if the request was successful
if (response.status_code == 200) {
  // Parse the JSON response
  const data = JSON.parse(response);

  // Iterate through the films
  for (const film in data.results) {
    // Check if the character with ID 18 is in the "characters" list
    if ('https://swapi-api.alx-tools.com/api/people/18/' in film.characters) {
      count += 1;
    }
  }
} else {
  console.log('Failed to retrieve data from the API');
}
// Print the count
console.log('Count:', count);
*/
