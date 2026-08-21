const fs = require('fs');
const html = fs.readFileSync('project.html', 'utf-8');
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/g);
if (scriptMatch) {
    scriptMatch.forEach(match => {
        const js = match.replace(/<\/?script>/g, '');
        try {
            new Function(js);
        } catch(e) {
            console.log("Syntax error in script:", e);
        }
    });
    console.log("Script checks completed.");
}
