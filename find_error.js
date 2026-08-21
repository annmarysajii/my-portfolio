const fs = require('fs');
const html = fs.readFileSync('project.html', 'utf8');
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/g);

if (scriptMatch) {
    scriptMatch.forEach((scriptStr, i) => {
        // extract inner content
        let content = scriptStr.replace(/<script>/, '').replace(/<\/script>/, '');
        try {
            new Function(content);
        } catch (e) {
            console.error(`Error in script block ${i + 1}:`, e.message);
            // find the line
            let lines = content.split('\n');
            for(let j=0; j<lines.length; j++){
                try {
                    new Function(lines.slice(0, j+1).join('\n'));
                } catch(err) {
                    if (err.message === 'Invalid or unexpected token') {
                        console.log(`Failing around line ${j}:`, lines[j]);
                    }
                }
            }
        }
    });
}
