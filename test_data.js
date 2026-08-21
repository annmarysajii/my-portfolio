const fs = require('fs');
const code = fs.readFileSync('scripts/data.js', 'utf8');
const window = {};
eval(code);
console.log("data.js OK");
