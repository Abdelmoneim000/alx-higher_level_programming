#!/usr/bin/node
const pro = require("process");
const first = pro.argv[1];
first ? console.log(first) : console.log("No argument");
