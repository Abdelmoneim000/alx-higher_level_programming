#!/usr/bin/node
const pro = require("process");
const num = parseInt(pro.argv[2]);
const char = "X";
let counter = num;
if (isNaN(num)) {
  console.log("Missing number of occurrences");
} else {
  while (counter) {
    console.log(`${char.repeat(num)}`);
    counter--;
  }
}
