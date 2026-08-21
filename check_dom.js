const fs = require('fs');
const html = fs.readFileSync('portfolio.html', 'utf-8');
const match = html.match(/<div class="awards">([\s\S]*?)<\/div>\s*<\/div>\s*<div class="rv d2">/);
if (match) {
    console.log("AWARDS INNER HTML:");
    console.log(match[1]);
} else {
    console.log("Could not find awards div in expected location!");
}
