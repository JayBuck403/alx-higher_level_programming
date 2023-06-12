#!/usr/bin/node
const args = process.argv[2];
console.log(typeof args === 'undefined' ? 'No argument' : args);
