#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/:id'
const movieID = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title)
  }
});
