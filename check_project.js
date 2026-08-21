const fs = require('fs');
const html = fs.readFileSync('project.html', 'utf8');

const scripts = html.match(/<script>(.*?)<\/script>/gs);
if (scripts) {
    scripts.forEach((script, idx) => {
        let code = script.replace(/<\/?script>/g, '');
        try {
            new Function(code);
            console.log(`Script ${idx} syntax OK`);
        } catch (e) {
            console.error(`Script ${idx} SYNTAX ERROR: ${e.message}`);
        }
    });
}
