!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach(film => {
      if (film.characters.some(url => url.includes(`/api/people/${characterId}/`))) {
        count++;
      }
    });
    console.log(count);
  } else {
    console.log('Error code:', response.statusCode);
  }
});
