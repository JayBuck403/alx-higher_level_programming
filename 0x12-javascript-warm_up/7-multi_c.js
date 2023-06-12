#!/usr/bin/node
const times = Math.floor(Number(process.argv[2]));
if (isNaN(times)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
}
