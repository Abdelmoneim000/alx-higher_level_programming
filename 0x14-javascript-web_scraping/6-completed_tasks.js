#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

// The URL for the Star Wars films API
const url = argv[2];

// Declare the object for user Tasks
const obj = {};
// Send a GET request to the API
request.get(url, (err, response) => {
  if (err) {
    throw err;
  } else {
    const bod = JSON.parse(response.body);
    for (const i of bod) {
      if (i.completed === true) {
        // Convert userId to a string
        const userId = i.userId.toString();
        // Initialize to 0 if undefined, then increment
        obj[userId] = (obj[userId] || 0) + 1;
      }
    }
  }
  console.log(obj);
});
