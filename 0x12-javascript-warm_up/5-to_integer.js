#!/usr/bin/node
const pro = require("process");
const num = parseInt(pro.argv[2]);
const first = `My number: ${num}`;
isNaN(num) ? console.log("Not a number") : console.log(first);
