#!/usr/bin/node
const pro = require("process");
pro.argv.length <= 1
  ? console.log("No argument")
  : console.log("Argument found");
