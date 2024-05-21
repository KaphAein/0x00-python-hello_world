#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/${movieID}`'

request.get(url, (err, response, body) => {
 if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
