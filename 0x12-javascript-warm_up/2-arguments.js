#!/usr/bin/node
const pro = require('process')
pro.argv.length <= 2 ? console.log("No argument") : console.log("Argument found");