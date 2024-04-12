#!/usr/bin/node
const fs = require('fs');
const [,, a, b, c] = process.argv;

if (!(a && b && c)) process.exit(1);

const fa = fs.readFileSync(a);
const fb = fs.readFileSync(b);
fs.writeFileSync(c, fa + fb);
