#!/usr/bin/node
const pro = require("process");
let sum = 0;
function add(a, b) {
  return parseInt(a) + parseInt(b);
}

sum = add(pro.argv[2], pro.argv[3]);
console.log(sum);
