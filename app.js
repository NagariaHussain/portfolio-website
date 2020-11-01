console.log("Hello, node app");

const fs = require('fs');

fs.writeFileSync('files/data.json', "Hello, new file!");