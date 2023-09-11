#!/usr/bin/node
const pro = require("process");
const first = `${pro.argv[2]} is ${pro.argv[3]}`;
first ? console.log(first) : console.log("No argument");
