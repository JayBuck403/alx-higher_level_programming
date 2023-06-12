#!/usr/bin/node
const numero = Math.floor(Number(process.argv[2]));
console.log(isNaN(numero) ? 'Not a number' : `My number: ${numero}`);
