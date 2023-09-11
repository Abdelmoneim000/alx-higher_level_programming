#!/usr/bin/node
const pro = require("process");
const first = pro.argv[2];
first ? console.log(first) : console.log("No argument");
