#!/home/abod/.nvm/versions/node/v18.17.1/bin/node
const fs = require('fs');
const { argv } = require('process');
fs.writeFile(argv[1], argv[2]);
