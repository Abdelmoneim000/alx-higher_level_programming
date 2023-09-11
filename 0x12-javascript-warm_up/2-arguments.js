#!/usr/bin/node
const pro = require("process");
const first = pro.argv[3];
first
  ? console.log("No argument")
  : console.log("Argument found");
