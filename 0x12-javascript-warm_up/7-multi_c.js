#!/usr/bin/node
const args = process.argv[2];
if (!parseInt(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < args; i++) {
    console.log('C is fun');
  }
}
