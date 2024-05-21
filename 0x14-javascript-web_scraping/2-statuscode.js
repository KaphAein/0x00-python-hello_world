#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];

request.get(URL, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
