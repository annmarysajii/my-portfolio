const fs = require('fs');
const html = fs.readFileSync('portfolio.html', 'utf-8');
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
if (scriptMatch) {
    try {
        new Function(scriptMatch[1]);
        console.log("Script syntax OK");
    } catch(e) {
        console.log("Syntax error in script:", e);
    }
}
