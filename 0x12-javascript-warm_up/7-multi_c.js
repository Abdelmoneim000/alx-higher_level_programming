#!/usr/bin/node
const pro = require("process");
let num = parseInt(pro.argv[2]);
if (isNaN(num)) {
  console.log("Missing number of occurrences");
} else {
  while (num) {
    console.log("C is fun");
    num--;
  }
}
