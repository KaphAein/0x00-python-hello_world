#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const [,, url, filePath] = process.argv;

request(url).pipe(fs.createWriteStream(filePath))
