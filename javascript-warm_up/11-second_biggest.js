#!/usr/bin/node

let largest = -Infinity;
let secondLargest = -Infinity;

for (let i = 2; i < process.argv.length; i++) {
  const current = parseInt(process.argv[i]);

  if (current > largest) {
    secondLargest = largest;
    largest = current;
  } else if (current > secondLargest && current !== largest) {
    secondLargest = current;
  }
}

if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(secondLargest);
}
