#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const [,, url, filePath] = process.argv;

request(url)
  .on('error', (err) => console.error('Error:', err))  
  .pipe(fs.createWriteStream(filePath))
