#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const [,, url, filePath] = process.argv;
const fileStream = fs.createWriteStream(filePath);

request(url).pipe(fileStream)
